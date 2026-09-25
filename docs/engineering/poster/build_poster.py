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
d.text((80, 60), "Vibe Coding 工作流", font=F(84), fill=INK)
d.text((84, 170), "一个人 + 一个 Agent 的软件开发闭环 · 猫咪导师带你走一遍", font=F(34, False), fill=GRAY)
paste_cat(cat_teacher, 1640, 10)
bubble(1080, 40, 1600, 210, "不知道从哪开始？在项目里敲 /vibe，我会把你放到正确的车道上，告诉你下一条命令是什么。", (1650, 150), size=27)

# =================== SETUP BAND ===================
panel(80, 300, 1920, 560, "setup", "第 0 步 · 地基", "每个仓库只做一次，之后所有 skill 都靠它们")
node(430, 430, 560, 160, "setup", cmd="/setup-matt-pocock-skills", label="issue 存哪、术语表放哪", note="个人项目选 Local markdown")
arrow([(715, 430), (785, 430)])
node(1105, 430, 620, 160, "setup", cmd="/setup-feedback-loops", label="typecheck · lint · test · smoke\n日志 · 浏览器 · 一键全跑", note="每个检查都要亲眼看它变红一次")
text(1450, 350, "为什么先搭反馈回路？", F(28), fill=LANES["setup"]["dark"])
text(1450, 392, "tdd 要跑测试、verify 要起应用、diagnosing-bugs 要读日志。没有回路，每个 skill 都在猜。", F(25, False), fill=GRAY, maxw=440, spacing=1.35)

# =================== BUILD LANE (left) ===================
BX0, BY0, BX1, BY1 = 80, 630, 1240, 2010
panel(BX0, BY0, BX1, BY1, "build", "① BUILD 车道 · 我有个想法", "90% 的时间你在这里")

node(660, 700, 220, 70, "build", label="★ 想法", cmd=None)
arrow([(660, 735), (660, 770)])
diamond(660, 830, 300, 110, "build", "这件事多大？")

# three branches
cols = {"S": 250, "M": 660, "L": 1070}
arrow([(585, 830), (250, 830), (250, 905)])
arrow([(735, 830), (1070, 830), (1070, 905)])
arrow([(660, 885), (660, 905)])
edge_label(250, 930, "S · 一句话说得清，没疑问", LANES["build"]["dark"])
edge_label(660, 930, "M · 一次坐下能做完，但有疑问", LANES["build"]["dark"])
edge_label(1070, 930, "L · 要做好几个晚上", LANES["build"]["dark"])

# S column
node(250, 1060, 330, 170, "build", label="直接说一句话", note="“给导出加 --json，\ntest first”\nagent 自己会用 tdd")
arrow([(250, 1145), (250, 1440)])
# M column
node(660, 1050, 350, 150, "build", cmd="/grill-with-docs", note="一轮轮追问你，顺手写\nCONTEXT.md 和 ADR")
arrow([(660, 1125), (660, 1175)])
node(660, 1240, 350, 130, "build", cmd="/implement", note="同一个窗口，\n中间不要 clear")
arrow([(660, 1305), (660, 1440)])
# L column
node(1070, 1030, 350, 110, "build", cmd="/grill-with-docs", note="说不清的绕一圈 prototype")
arrow([(1070, 1085), (1070, 1110)])
node(1070, 1160, 350, 100, "build", cmd="/to-spec", note="不再提问，只综合成 spec")
arrow([(1070, 1210), (1070, 1235)])
node(1070, 1300, 350, 130, "build", cmd="/to-tickets", note="垂直切片 + 阻塞关系\n（前三步同一窗口）")
arrow([(1070, 1365), (1070, 1385)])
node(1070, 1425, 350, 80, "build", cmd="/clear → /implement", cmd_size=26, note="每张票一个新窗口")
# one unbroken window marker for M and L grill→tickets

# converge into implement internals box
d.line([(1070, 1465), (1070, 1470)], fill=INK, width=6)
d.line([(250, 1470), (1070, 1470)], fill=INK, width=6)
d.line([(250, 1440), (250, 1470)], fill=INK, width=6)
arrow([(660, 1470), (660, 1500)])

IX0, IY0, IX1, IY1 = 130, 1505, 1190, 1795
rbox(IX0, IY0, IX1, IY1, (245, 249, 255), LANES["build"]["edge"], r=28, width=4)
d.text((IX0 + 24, IY0 + 14), "/implement 里面发生了什么（自动，你只需要读结果）", font=F(30), fill=LANES["build"]["dark"])
chain = [("tdd", "先红后绿\n一片一片做"), ("verify", "真的跑起来\n截图为证"), ("test-audit", "测试守不守逻辑？\n给你 Claims 清单"), ("code-review", "规范 + spec\n(+ security)"), ("commit", "结尾给你\nChecks run 台账")]
cx = IX0 + 130
for i, (c, n) in enumerate(chain):
    node(cx, IY0 + 110, 190, 66, "build", cmd=c, cmd_size=28)
    text(cx, IY0 + 160, n, F(23, False), fill=GRAY, align="center", spacing=1.3)
    if i < len(chain) - 1:
        arrow([(cx + 98, IY0 + 110), (cx + 122, IY0 + 110)], width=5, head=16)
    cx += 220
text(IX0 + 24, IY0 + 236, "FAIL 和幸存的 mutant 都会退回 tdd 变成新的红测试；有 FAIL 不许进 review。", F(24, False), fill=GRAY)

# clipboard cat + bubble (bottom of build panel)
paste_cat(cat_clip, 120, 1770)
bubble(400, 1835, 1200, 1990, "读 test-audit 的 Claims 清单！每条是一句业务规则。测试和代码可能编码了同一个误解、一起全绿一起错，工具查不出来，你一眼能看出来。", (395, 1910), size=27)

# =================== RIGHT COLUMN ===================
RX0, RX1 = 1300, 1920

# FIX
panel(RX0, 630, RX1, 1110, "fix", "② FIX 车道 · 坏了")
diamond(1610, 720, 280, 100, "fix", "知道原因吗？")
arrow([(1470, 720), (1435, 720), (1435, 790)])
edge_label(1435, 758, "知道", LANES["fix"]["dark"], 22)
node(1440, 860, 250, 130, "fix", label="说一句，加 test first", note="失败测试→修→绿")
arrow([(1750, 720), (1785, 720), (1785, 790)])
edge_label(1785, 758, "不知道 / 偶发 / 变慢", LANES["fix"]["dark"], 22)
node(1780, 860, 250, 130, "fix", cmd="/diagnosing-bugs", cmd_size=22, note="六个阶段\n不许先猜")
paste_cat(cat_det, 1330, 935)
bubble(1545, 925, 1900, 1090, "没有一条能变红的复现命令，就不许推理。这是整个 skill 的核心。", (1540, 1005), size=25)

# REVIEW
panel(RX0, 1170, RX1, 1560, "review", "③ REVIEW · 合并 / 上线前")
node(1690, 1270, 430, 130, "review", cmd="/code-review main", cmd_size=30, note="两个子代理并行：\nStandards 轴 + Spec 轴")
arrow([(1690, 1335), (1690, 1355)])
node(1690, 1425, 430, 140, "review", cmd="security-review", cmd_size=30, note="碰路由/鉴权/查询/env/依赖\n时自动跑；上线前手动跑一次")
paste_cat(cat_shield, 1308, 1270)
bubble(1330, 1500, 1900, 1550, "只查五件事，但那五件事就是独立开发者被黑的原因。", (1400, 1445), size=22)

# TIDY
panel(RX0, 1620, RX1, 2010, "tidy", "④ TIDY · 每隔几天")
node(1690, 1715, 430, 120, "tidy", cmd="/improve-codebase-architecture", cmd_size=23, note="HTML 报告：哪些浅模块该加深，\n选一个，它追问你")
arrow([(1690, 1775), (1690, 1800)])
node(1690, 1865, 430, 130, "tidy", label="新想法 → 回到 ① BUILD", note="diagnosing-bugs 说“没有接缝”\n也来这里")
paste_cat(cat_broom, 1305, 1720)
bubble(1330, 1945, 1900, 1998, "扫一扫，agent 改东西就不用跳七个文件了。", (1400, 1895), size=22)

# =================== SESSION BAND: refocus / handoff / takeover ===================
panel(80, 2080, 1920, 2480, "focus", "会话出问题了？三招", "同一个窗口走神 · 主动换地方 · 旧会话没了")
paste_cat(cat_dizzy, 130, 2170)
SX = [520, 1000, 1480]
node(SX[0], 2215, 420, 120, "focus", cmd="/refocus", label="还在，走神了，不换窗口")
node(SX[1], 2215, 420, 120, "focus", cmd="/handoff", label="还在，工作要挪地方")
node(SX[2], 2215, 420, 120, "focus", cmd="/takeover", label="旧会话没了 / 太长不敢信")
text(SX[0], 2295, "从磁盘重读 spec、ticket、CONTEXT.md 和你口头的决定，对着 diff 找漏做 / 多做 / 做反，有歧义问你一轮，答案回写到票里。先 refocus 再 compact。", F(23, False), fill=INK, maxw=400, align="center", spacing=1.4)
text(SX[1], 2295, "走的那个会话写一份可携带的小文件到临时目录：换目录、换工具、分叉一个支线，或者去做 prototype 再回来。没有东西要搬就不需要它。", F(23, False), fill=INK, maxw=400, align="center", spacing=1.4)
text(SX[2], 2295, "额度用完、崩了、关了窗口、在别的工具里聊的。新会话自己读记录（ID / 导出 / 链接 / handoff 文件），最多 10 句复述项目，问你一次确认，确认前只读不改。", F(23, False), fill=INK, maxw=400, align="center", spacing=1.4)

# =================== BOTTOM: context rules + stuck ===================
panel(80, 2550, 980, 3020, "setup", "上下文规则（记住这 7 条就够）")
rules = [("grill → spec → tickets", "", "同一个窗口，别 clear"),
         ("每张票之间", "/clear", "，开新窗口"),
         ("走神了", "/refocus", "，在 compact 之前"),
         ("换目录 / 换工具 / 分叉", "/handoff", ""),
         ("旧会话没了", "/takeover", " 它的记录"),
         ("要跑代码才能定", "/handoff", " → prototype → 带答案回来"),
         ("没听懂它在说什么", "/wait-what", "")]
y = 2610
for a, cmd, rest in rules:
    d.text((120, y), a, font=F(27), fill=INK)
    x = 470
    if cmd:
        d.text((x, y + 2), cmd, font=MONO(26), fill=LANES["build"]["dark"]); x += MONO(26).getlength(cmd)
    if rest:
        d.text((x, y), rest, font=F(27, False), fill=LANES["build"]["dark"])
    y += 56

panel(1020, 2550, 1920, 3020, "fix", "改了三次还不对？停！")
text(1060, 2600, "别让它改第五次。先扔掉半成品，/clear，写下一句话：", F(26, False), fill=INK, maxw=820)
rbox(1060, 2660, 1880, 2730, (255, 255, 255), LANES["fix"]["edge"], r=18, width=3)
text(1470, 2678, "输入 ___ 的时候，我期望 ___，但实际是 ___", F(28), fill=LANES["fix"]["dark"], align="center")
text(1060, 2755, "写不出来 → 不是 bug，是需求没对齐 → /refocus 或 /grill-with-docs\n写得出来 → 先把它变成一个失败的测试：\n    改一下就绿 → 之前没有反馈回路（tdd）\n    还是红 / 修好又坏别的 → 真 bug（/diagnosing-bugs）\n    每次要碰五个文件 → 没有接缝（④ TIDY）", F(24, False), fill=INK, spacing=1.45)

# =================== FOOTER ===================
d.line([(80, 3080), (1920, 3080)], fill=(210, 200, 185), width=3)
text(80, 3110, "第一次试用：在一个空仓库里敲 /vibe，它会给你一张 First run 卡，9 步走完整个闭环，并陪你核对每一步的输出。", F(27), fill=INK, maxw=1840)
text(80, 3165, "完整手册：skills/engineering/vibe/WORKFLOW.md   ·   23 个精选 skill，12 个你敲，11 个 agent 自己会用   ·   github.com/awangs1986/popcodeskills", F(24, False), fill=GRAY, maxw=1840)
text(80, 3220, "口诀：先对齐，再写 spec；红了再绿；跑起来看；读 Claims；合并前 review；每周扫一扫；走神 refocus，断了 takeover。", F(28), fill=LANES["build"]["dark"], maxw=1840)

img.save(str(HERE.parent / "vibe-workflow-poster.png"), optimize=True)
print("saved")
