from PIL import Image, ImageDraw, ImageFont
import re, math, os
from pathlib import Path

W, H = 2000, 3320
BG = (255, 248, 236)
INK = (47, 42, 38)
GRAY = (120, 112, 104)

HERE = Path(__file__).resolve().parent
FONTS = Path(os.environ.get("POSTER_FONTS", HERE / "fonts"))
MONO_PATH = os.environ.get("POSTER_MONO", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf")
def F(size, bold=True):
    return ImageFont.truetype(str(FONTS / ("NotoSansSC-700-full.ttf" if bold else "NotoSansSC-400-full.ttf")), size)
def MONO(size):
    return ImageFont.truetype(MONO_PATH, size)

LANES = {
    "setup":  dict(fill=(238, 236, 231), edge=(120, 112, 104), dark=(90, 84, 78)),
    "build":  dict(fill=(222, 235, 255), edge=(59, 111, 214), dark=(35, 75, 160)),
    "fix":    dict(fill=(255, 226, 220), edge=(217, 83, 79),  dark=(160, 50, 46)),
    "review": dict(fill=(221, 243, 228), edge=(58, 157, 93),  dark=(30, 110, 60)),
    "tidy":   dict(fill=(235, 226, 255), edge=(123, 92, 214), dark=(85, 60, 160)),
    "focus":  dict(fill=(255, 241, 194), edge=(217, 164, 0),  dark=(150, 110, 0)),
}

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- text helpers ----------
def tokens(s):
    return re.findall(r"[A-Za-z0-9_/\-\.:,'\(\)\+→←=<>#\*]+|\s+|.", s)

def wrap(s, font, maxw):
    lines, cur = [], ""
    for t in tokens(s):
        if t == "\n":
            lines.append(cur); cur = ""; continue
        if font.getlength(cur + t) <= maxw or cur == "":
            cur += t
        else:
            lines.append(cur.rstrip()); cur = t.lstrip()
    lines.append(cur)
    return [l for l in lines]

def text(x, y, s, font, fill=INK, maxw=None, align="left", spacing=1.35, anchor_center=False):
    lines = wrap(s, font, maxw) if maxw else s.split("\n")
    lh = int(font.size * spacing)
    for i, l in enumerate(lines):
        lw = font.getlength(l)
        if align == "center":
            xx = x - lw / 2
        elif align == "right":
            xx = x - lw
        else:
            xx = x
        d.text((xx, y + i * lh), l, font=font, fill=fill)
    return y + len(lines) * lh

def text_h(s, font, maxw, spacing=1.35):
    return len(wrap(s, font, maxw)) * int(font.size * spacing)

# ---------- shapes ----------
def rbox(x0, y0, x1, y1, fill, edge, r=26, width=5):
    d.rounded_rectangle((x0, y0, x1, y1), radius=r, fill=fill, outline=edge, width=width)

def panel(x0, y0, x1, y1, lane, title, subtitle=None):
    c = LANES[lane]
    rbox(x0, y0, x1, y1, (255, 255, 255), c["edge"], r=34, width=6)
    # title tab
    tf = F(40)
    tw = tf.getlength(title) + 60
    d.rounded_rectangle((x0 + 30, y0 - 34, x0 + 30 + tw, y0 + 34), radius=20, fill=c["edge"])
    d.text((x0 + 60, y0 - 27), title, font=tf, fill=(255, 255, 255))
    if subtitle:
        d.text((x0 + 30 + tw + 24, y0 - 20), subtitle, font=F(30, False), fill=c["dark"])

def node(cx, cy, w, h, lane, cmd=None, label=None, note=None, cmd_size=34):
    c = LANES[lane]
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    rbox(x0, y0, x1, y1, c["fill"], c["edge"], r=22, width=5)
    parts = []
    if cmd: parts.append(("cmd", cmd))
    if label: parts.append(("lab", label))
    if note: parts.append(("note", note))
    # measure
    total = 0; measured = []
    for kind, s in parts:
        if kind == "cmd":
            f = MONO(cmd_size); hh = int(f.size * 1.3)
        elif kind == "lab":
            f = F(30); hh = text_h(s, f, w - 40)
        else:
            f = F(26, False); hh = text_h(s, f, w - 40, 1.3)
        measured.append((kind, s, f, hh)); total += hh
    y = cy - total / 2
    for kind, s, f, hh in measured:
        col = c["dark"] if kind == "cmd" else (INK if kind == "lab" else GRAY)
        text(cx, y, s, f, fill=col, maxw=w - 40, align="center", spacing=1.3)
        y += hh
    return (x0, y0, x1, y1)

def diamond(cx, cy, w, h, lane, label):
    c = LANES[lane]
    pts = [(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)]
    d.polygon(pts, fill=c["fill"], outline=c["edge"], width=5)
    f = F(32)
    lines = label.split("\n")
    lh = int(f.size * 1.25)
    y = cy - (len(lines) - 1) * lh / 2
    for l in lines:
        d.text((cx, y), l, font=f, fill=c["dark"], anchor="mm"); y += lh

def arrow(pts, color=INK, width=6, head=22):
    d.line(pts, fill=color, width=width, joint="curve")
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    ang = math.atan2(y1 - y0, x1 - x0)
    a1 = (x1 - head * math.cos(ang - 0.5), y1 - head * math.sin(ang - 0.5))
    a2 = (x1 - head * math.cos(ang + 0.5), y1 - head * math.sin(ang + 0.5))
    d.polygon([(x1, y1), a1, a2], fill=color)

def edge_label(x, y, s, color=GRAY, size=26):
    f = F(size)
    w = f.getlength(s) + 24
    d.rounded_rectangle((x - w / 2, y - 20, x + w / 2, y + 20), radius=14, fill=(255, 255, 255), outline=color, width=3)
    d.text((x - (w - 24) / 2, y - 17), s, font=f, fill=color)

# ---------- cats ----------
def load_cat(path, height):
    im = Image.open(path).convert("RGBA")
    # flood-fill background from corners to magenta, then key out
    from PIL import ImageDraw as ID
    key = (255, 0, 255, 255)
    for xy in [(2, 2), (im.width - 3, 2), (2, im.height - 3), (im.width - 3, im.height - 3)]:
        ID.floodfill(im, xy, key, thresh=45)
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if r > 230 and g < 40 and b > 230:
                px[x, y] = (0, 0, 0, 0)
    bbox = im.getbbox(); im = im.crop(bbox)
    s = height / im.height
    return im.resize((int(im.width * s), height), Image.LANCZOS)

def paste_cat(cat, x, y):
    img.paste(cat, (int(x), int(y)), cat)

def bubble(x0, y0, x1, y1, s, tail, size=28, fill=(255, 255, 255), edge=INK):
    # tail: (tx, ty) point outside box
    d.rounded_rectangle((x0, y0, x1, y1), radius=26, fill=fill, outline=edge, width=4)
    tx, ty = tail
    # pick base on nearest side
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    if tx > x1:   base = [(x1 - 2, cy - 22), (x1 - 2, cy + 22)]
    elif tx < x0: base = [(x0 + 2, cy - 22), (x0 + 2, cy + 22)]
    elif ty > y1: base = [(cx - 22, y1 - 2), (cx + 22, y1 - 2)]
    else:         base = [(cx - 22, y0 + 2), (cx + 22, y0 + 2)]
    d.polygon([base[0], base[1], (tx, ty)], fill=fill, outline=edge, width=4)
    d.polygon([base[0], base[1], (tx, ty)], fill=fill)
    # redraw inner edge fix
    d.line([base[0], (tx, ty)], fill=edge, width=4); d.line([base[1], (tx, ty)], fill=edge, width=4)
    f = F(size)
    lines = wrap(s, f, (x1 - x0) - 50)
    lh = int(size * 1.4)
    y = cy - len(lines) * lh / 2 + 4
    for l in lines:
        d.text((x0 + 25, y), l, font=f, fill=INK); y += lh

cat_teacher = load_cat((HERE / "cats" / "cat_teacher.png"), 330)
cat_det = load_cat((HERE / "cats" / "cat_detective.png"), 165)
cat_clip = load_cat((HERE / "cats" / "cat_clipboard.png"), 240)
cat_broom = load_cat((HERE / "cats" / "cat_broom.png"), 170)
cat_dizzy = load_cat((HERE / "cats" / "cat_dizzy.png"), 190)
cat_shield = load_cat((HERE / "cats" / "cat_shield.png"), 170)

# =================== HEADER ===================
d.text((80, 60), "The Vibe Coding Workflow", font=F(72), fill=INK)
d.text((84, 160), "One developer + one agent, a closed loop  ·  with a cat guide", font=F(30, False), fill=GRAY)
paste_cat(cat_teacher, 1640, 10)
bubble(1140, 40, 1600, 210, "Not sure where to start? Type /vibe in the project. I'll put you on the right lane and name the next command.", (1650, 150), size=27)

# =================== SETUP BAND ===================
panel(80, 300, 1920, 560, "setup", "Step 0 · Foundations", "once per repo; every skill after this depends on them")
node(430, 430, 560, 160, "setup", cmd="/setup-matt-pocock-skills", label="where issues live, where the glossary goes", note="solo project: pick Local markdown")
arrow([(715, 430), (785, 430)])
node(1105, 430, 620, 160, "setup", cmd="/setup-feedback-loops", label="typecheck · lint · test · smoke\nlogs · browser · one command for all", note="watch every check go red once")
text(1450, 350, "Why feedback loops first?", F(28), fill=LANES["setup"]["dark"])
text(1450, 392, "tdd runs tests, verify boots the app, diagnosing-bugs reads logs. Without loops, every skill is guessing.", F(25, False), fill=GRAY, maxw=440, spacing=1.35)

# =================== BUILD LANE (left) ===================
BX0, BY0, BX1, BY1 = 80, 630, 1240, 2010
panel(BX0, BY0, BX1, BY1, "build", "① BUILD lane · I have an idea", "90% of your time is here")

node(660, 700, 220, 70, "build", label="★ an idea", cmd=None)
arrow([(660, 735), (660, 770)])
diamond(660, 830, 300, 110, "build", "How big is it?")

# three branches
cols = {"S": 250, "M": 660, "L": 1070}
arrow([(585, 830), (250, 830), (250, 905)])
arrow([(735, 830), (1050, 830), (1050, 905)])
arrow([(660, 885), (660, 905)])
edge_label(250, 930, "S · one clear sentence", LANES["build"]["dark"])
edge_label(660, 930, "M · one sitting, open questions", LANES["build"]["dark"])
edge_label(1050, 930, "L · several evenings", LANES["build"]["dark"])

# S column
node(250, 1060, 330, 170, "build", label="Just say it", note="\u201cadd --json to export,\ntest first\u201d\nthe agent uses tdd itself")
arrow([(250, 1145), (250, 1440)])
# M column
node(660, 1050, 360, 150, "build", cmd="/grill-with-docs", note="asks in rounds; writes\nCONTEXT.md and ADRs")
arrow([(660, 1125), (660, 1175)])
node(660, 1240, 350, 130, "build", cmd="/implement", note="same window,\ndon't clear in between")
arrow([(660, 1305), (660, 1440)])
# L column
node(1050, 1030, 360, 110, "build", cmd="/grill-with-docs", note="stuck? try a prototype")
arrow([(1050, 1085), (1050, 1110)])
node(1050, 1160, 360, 100, "build", cmd="/to-spec", note="synthesis, no questions")
arrow([(1050, 1210), (1050, 1235)])
node(1050, 1300, 360, 130, "build", cmd="/to-tickets", note="slices + blocking edges\n(steps 1 to 3: one window)")
arrow([(1050, 1365), (1050, 1385)])
node(1050, 1425, 360, 80, "build", cmd="/clear → /implement", cmd_size=26, note="a fresh window per ticket")

# converge into implement internals box
d.line([(1050, 1465), (1050, 1470)], fill=INK, width=6)
d.line([(250, 1470), (1050, 1470)], fill=INK, width=6)
d.line([(250, 1440), (250, 1470)], fill=INK, width=6)
arrow([(660, 1470), (660, 1500)])

IX0, IY0, IX1, IY1 = 130, 1505, 1190, 1795
rbox(IX0, IY0, IX1, IY1, (245, 249, 255), LANES["build"]["edge"], r=28, width=4)
d.text((IX0 + 24, IY0 + 14), "What happens inside /implement (automatic; you only read the results)", font=F(30), fill=LANES["build"]["dark"])
chain = [("tdd", "red, then green\none slice at a time"), ("verify", "really runs it\nscreenshot as proof"), ("test-audit", "do tests guard logic?\nyou get a Claims list"), ("code-review", "standards + spec\n(+ security)"), ("commit", "ends with a\nChecks run ledger")]
cx = IX0 + 130
for i, (c, n) in enumerate(chain):
    node(cx, IY0 + 110, 190, 66, "build", cmd=c, cmd_size=28)
    text(cx, IY0 + 160, n, F(23, False), fill=GRAY, align="center", spacing=1.3)
    if i < len(chain) - 1:
        arrow([(cx + 98, IY0 + 110), (cx + 122, IY0 + 110)], width=5, head=16)
    cx += 220
text(IX0 + 24, IY0 + 236, "Every FAIL and surviving mutant goes back to tdd as a new red test. No review while a FAIL is open.", F(24, False), fill=GRAY)

# clipboard cat + bubble (bottom of build panel)
paste_cat(cat_clip, 120, 1770)
bubble(400, 1835, 1200, 1990, "Read test-audit's Claims list! Each line is one business rule. The test and the code can share the same misunderstanding and be green together; no tool catches that. You can, at a glance.", (395, 1910), size=26)

# =================== RIGHT COLUMN ===================
RX0, RX1 = 1300, 1920

# FIX
panel(RX0, 630, RX1, 1110, "fix", "② FIX lane · it broke")
diamond(1610, 720, 280, 100, "fix", "Know the cause?")
arrow([(1470, 720), (1435, 720), (1435, 790)])
edge_label(1435, 758, "yes", LANES["fix"]["dark"], 22)
node(1435, 860, 260, 130, "fix", label="Say it, test first", note="red → fix → green")
arrow([(1750, 720), (1785, 720), (1785, 790)])
edge_label(1785, 758, "no / flaky / slow", LANES["fix"]["dark"], 22)
node(1785, 860, 260, 130, "fix", cmd="/diagnosing-bugs", cmd_size=22, note="six phases,\nno guessing first")
paste_cat(cat_det, 1330, 935)
bubble(1545, 925, 1900, 1090, "No command that goes red on the bug, no theorising. That rule is the whole skill.", (1540, 1005), size=25)

# REVIEW
panel(RX0, 1170, RX1, 1560, "review", "③ REVIEW · before merge")
node(1690, 1270, 430, 130, "review", cmd="/code-review main", cmd_size=30, note="two sub-agents in parallel:\nStandards axis + Spec axis")
arrow([(1690, 1335), (1690, 1355)])
node(1690, 1425, 430, 140, "review", cmd="security-review", cmd_size=30, note="auto on auth / routes / queries;\nonce more before shipping")
paste_cat(cat_shield, 1308, 1270)
bubble(1330, 1500, 1900, 1550, "Five checks. That is how solo apps get hacked.", (1400, 1445), size=22)

# TIDY
panel(RX0, 1620, RX1, 2010, "tidy", "④ TIDY · every few days")
node(1690, 1715, 430, 120, "tidy", cmd="/improve-codebase-architecture", cmd_size=23, note="report of shallow modules;\npick one, it grills you")
arrow([(1690, 1775), (1690, 1800)])
node(1690, 1865, 430, 130, "tidy", label="idea → back to ① BUILD", note="\u201cno seam\u201d from a diagnosis\nlands here too")
paste_cat(cat_broom, 1305, 1720)
bubble(1330, 1945, 1900, 1998, "Sweep: no more seven-file hops per change.", (1400, 1895), size=22)

# =================== SESSION BAND: refocus / handoff / takeover ===================
panel(80, 2080, 1920, 2510, "focus", "Session trouble? Three moves", "drifting in this window · leaving on purpose · the old session is gone")
paste_cat(cat_dizzy, 130, 2170)
SX = [520, 1000, 1480]
node(SX[0], 2215, 420, 120, "focus", cmd="/refocus", label="still open, drifting, staying here")
node(SX[1], 2215, 420, 120, "focus", cmd="/handoff", label="still open, the work is moving")
node(SX[2], 2215, 420, 120, "focus", cmd="/takeover", label="session gone / too long to trust")
text(SX[0], 2295, "Re-reads spec, ticket, CONTEXT.md and your spoken decisions from disk, diffs them against the work (dropped / drifted / contradicted), asks one round, saves the answers to the ticket. Then compact.", F(23, False), fill=INK, maxw=440, align="center", spacing=1.35)
text(SX[1], 2295, "The outgoing session writes a small portable file to the temp dir: new directory, new tool, a forked side task, a prototype detour. Nothing travelling? You don't need it.", F(23, False), fill=INK, maxw=440, align="center", spacing=1.35)
text(SX[2], 2295, "Quota gone, crashed, closed, or another tool. The new session reads the record itself (ID / export / URL / handoff), retells the project in 10 sentences at most, asks once. Read-only until you confirm.", F(23, False), fill=INK, maxw=440, align="center", spacing=1.35)

# =================== BOTTOM: context rules + stuck ===================
panel(80, 2550, 980, 3020, "setup", "Context rules (these seven are enough)")
rules = [("grill → spec → tickets", "", "one window, don't clear"),
         ("between tickets", "/clear", ", fresh window"),
         ("agent drifted", "/refocus", ", before compact"),
         ("new dir / tool / fork", "/handoff", ""),
         ("old session gone", "/takeover", " its record"),
         ("needs running code", "/handoff", " → prototype → answer back"),
         ("didn't follow it", "/wait-what", "")]
y = 2610
for a, cmd, rest in rules:
    d.text((120, y), a, font=F(27), fill=INK)
    x = 470
    if cmd:
        d.text((x, y + 2), cmd, font=MONO(26), fill=LANES["build"]["dark"]); x += MONO(26).getlength(cmd)
    if rest:
        d.text((x, y), rest, font=F(27, False), fill=LANES["build"]["dark"])
    y += 56

panel(1020, 2550, 1920, 3020, "fix", "Wrong three times? Stop!")
text(1060, 2600, "No fifth attempt. Discard it, /clear, and write one sentence:", F(26, False), fill=INK, maxw=820)
rbox(1060, 2660, 1880, 2730, (255, 255, 255), LANES["fix"]["edge"], r=18, width=3)
text(1470, 2678, "When I input ___, I expect ___, but I get ___", F(28), fill=LANES["fix"]["dark"], align="center")
text(1060, 2755, "Can't write it → not a bug, misaligned requirements → /refocus or /grill-with-docs\nCan write it → turn it into one failing test first:\n    green after one fix → there was no feedback loop (tdd)\n    stays red / fixing it breaks something else → real bug (/diagnosing-bugs)\n    every attempt touches five files → no seam (④ TIDY)", F(24, False), fill=INK, spacing=1.45)

# =================== FOOTER ===================
d.line([(80, 3080), (1920, 3080)], fill=(210, 200, 185), width=3)
text(80, 3110, "First time? Type /vibe in an empty repo: a First run card walks 9 steps through the whole loop and checks each step with you.", F(27), fill=INK, maxw=1840)
text(80, 3165, "Full handbook: skills/engineering/vibe/WORKFLOW.md   ·   24 curated skills, 13 you type, 11 the agent reaches for   ·   github.com/awangs1986/popcodeskills", F(24, False), fill=GRAY, maxw=1840)
text(80, 3220, "Mantra: align, then spec; red, then green; run it; read the Claims; review before merge; sweep weekly; drifting → refocus, dead → takeover.", F(26), fill=LANES["build"]["dark"], maxw=1840)

img.save(str(HERE.parent / "vibe-workflow-poster.png"), optimize=True)
print("saved")
