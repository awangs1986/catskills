# Askcat data format

`template.html` renders whatever object you assign to `window.ASKCAT`. Every string is plain text unless noted; the template escapes it. Write all human-facing strings in the user's language; keep skill names, commands, and paths as they are.

```js
window.ASKCAT = {
  "lang": "zh-CN",                       // BCP-47 tag; sets <html lang>
  "title": "…",                          // page title
  "subtitle": "…",                       // one line under the title
  "generated": "2026-09-25",             // date you built it
  "source": "awangs1986/popcodeskills",  // where the skills came from
  "cat": { "name": "…" },                // what the guide calls itself

  "labels": {                            // UI strings, in the user's language
    "search": "…", "searchHint": "…", "youType": "…", "agentUses": "…", "beta": "…",
    "when": "…", "see": "…", "example": "…", "tip": "…", "working": "…", "broken": "…",
    "tried": "…", "progress": "…", "picker": "…", "pickerIntro": "…", "restart": "…",
    "result": "…", "firstRun": "…", "glossary": "…", "openFile": "…", "chapters": "…",
    "noMatch": "…"
  },

  "intro": {
    "heading": "…",
    "paragraphs": ["…", "…"],            // two or three short paragraphs: what a skill is, how you use one, what this page is
    "bubble": "…"                        // the cat's opening line
  },

  "chapters": [
    {
      "id": "start",                     // stable slug, used for anchors
      "title": "…",
      "blurb": "…",                      // two sentences
      "mood": "teacher",                 // one of the cat moods below
      "bubble": "…",                     // what the cat says at the top of the chapter
      "skills": [
        {
          "name": "vibe",                // exactly the skill's name
          "invoke": "you",               // "you" (user types it) or "agent" (model reaches for it; user can type it too)
          "beta": false,                 // true for in-progress skills
          "oneLiner": "…",               // what it does, one sentence, plain words
          "when": "…",                   // the situation that calls for it
          "see": "…",                    // what a run looks like: what it asks, what it writes, what it produces
          "example": "…",                // one realistic prompt; starts with the command for "you" skills
          "tip": "…",                    // the one thing people get wrong, or the habit that makes it pay off
          "working": "…",                // one-line tell of a good run
          "broken": "…",                 // one-line tell of a bad run
          "file": "skills/engineering/vibe/SKILL.md"   // path or URL to the skill's own file
        }
      ]
    }
  ],

  "picker": {
    "start": "q1",
    "questions": [
      {
        "id": "q1",
        "text": "…",
        "options": [
          { "label": "…", "next": "q2" },              // another question
          { "label": "…", "skill": "diagnosing-bugs", "prompt": "…" }   // a leaf: a skill on the page plus a prompt to type
        ]
      }
    ]
  },

  "firstRun": [
    { "step": 1, "type": "/setup-matt-pocock-skills", "watch": "…" }   // 'watch' = what a good result looks like
  ],

  "glossary": [
    { "term": "spec", "plain": "…" }
  ],

  "footer": "…"                          // one line: where the full handbook is, how to regenerate
};
```

## Cat moods

The template draws the cat itself; a mood only changes its accessories and expression. Use the one that fits the chapter:

| mood | looks like | use for |
| --- | --- | --- |
| `teacher` | glasses, pointer | start here, setup, glossary |
| `builder` | hard hat, pencil | build lane |
| `detective` | deerstalker, magnifier | fix lane, diagnosing |
| `guard` | helmet, shield | review, security |
| `sweeper` | headscarf, broom | tidy, architecture |
| `dizzy` | swirl eyes, stars | sessions going wrong: refocus, handoff, takeover |
| `reader` | clipboard, tick | test-audit, verify, cattytest, anything that produces a list to read |

## Constraints the template relies on

- `chapters[].id` and `skills[].name` are unique; anchors are `#chapter-<id>` and `#skill-<name>`.
- Every `picker` leaf's `skill` names a skill that appears in some chapter.
- `labels` must be complete; the template does not ship defaults in any language.
- Keep the whole object under roughly 150 KB; the page should open instantly from disk.
