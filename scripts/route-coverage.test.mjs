import test from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { routeCoverageProblems } from "./route-coverage.mjs";
const repo = join(dirname(fileURLToPath(import.meta.url)), "..");

test("every promoted skill is classified and the curated kit agrees with invocation metadata", () => {
  assert.deepEqual(routeCoverageProblems(repo), []);
});

test("a newly promoted skill cannot silently miss the dispatcher map", () => {
  const root = mkdtempSync(join(tmpdir(), "cat-routes-"));
  const put = (path, text) => {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    writeFileSync(join(root, path), text);
  };
  try {
    put("skills/engineering/vibe/SKILL.md", "---\nname: vibe\ndisable-model-invocation: true\n---\n");
    put("skills/engineering/new-skill/SKILL.md", "---\nname: new-skill\n---\n");
    put("skills/engineering/vibe/ROUTES.md", "| `vibe` | kit | Route requests |\n");
    put("skills/engineering/vibe/WORKFLOW.md", "**You type these** (user-invoked):\n| `/vibe` | Route |\n**The agent reaches for these** (model-invoked):\n**Deliberately left out**\n");
    assert.ok(routeCoverageProblems(root).some((p) => p.includes("new-skill has no route classification")));
    put("skills/engineering/vibe/ROUTES.md", "| `vibe` | kit | Route requests |\n| `new-skill` | full-map | Use the full map |\n");
    assert.deepEqual(routeCoverageProblems(root), []);
    put("skills/engineering/vibe/ROUTES.md", "| `vibe` | kit | Route requests |\n| `new-skill` | kit | New work |\n");
    assert.ok(routeCoverageProblems(root).some((p) => p.includes("kit skill new-skill is missing")));
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("research is not described as excluded by the full router", () => {
  const router = readFileSync(join(repo, "skills/engineering/ask-matt/SKILL.md"), "utf8");
  assert.doesNotMatch(router, /deliberately leaves out[^.\n]*`research`/);
});

test("public build guidance prefers the spec route and keeps old calls as compatibility", () => {
  const routes = readFileSync(join(repo, "skills/engineering/vibe/ROUTES.md"), "utf8");
  assert.match(routes, /^\| `implement-spec` \| kit \|/m);
  assert.match(routes, /^\| `implement` \| full-map \| Compatibility /m);
  const paths = [
    "README.md", "README.zh-CN.md", "skills/engineering/README.md",
    "skills/engineering/vibe/SKILL.md", "skills/engineering/vibe/WORKFLOW.md",
    "skills/engineering/ask-matt/SKILL.md", "skills/productivity/askcat/SKILL.md",
    "docs/engineering/poster/build_poster.py", "docs/engineering/poster/build_poster_zh.py",
    "docs/engineering/to-spec.md", "docs/engineering/to-tickets.md", "docs/engineering/vibe.md",
    "docs/productivity/askcat.md",
  ];
  for (const path of paths) {
    const content = readFileSync(join(repo, path), "utf8");
    assert.match(content, /implement-spec/, path);
    for (const line of content.split("\n")) {
      if (!/\/implement(?![a-z0-9-])|`implement`|\[implement\]/.test(line)) continue;
      const catalogEntry = /^- \*\*\[implement\]\([^)]*implement\/SKILL\.md\)/.test(line);
      assert.ok(catalogEntry || /compatibility/i.test(line), `${path}: unexpected old build recommendation: ${line}`);
    }
  }
});
