# Feedback loops

The commands that tell an agent whether what it just did is right. Written by `/setup-feedback-loops`; edit freely. Skills that run checks (`implement`, `tdd`, `diagnosing-bugs`, `verify`) read this file first.

Every loop below has been seen going **red** on a deliberate fault before being listed here.

## typecheck

- Command: `<e.g. npm run typecheck>`
- Duration: `<e.g. 3s>`
- Notes: `<strict mode on; any file-level exceptions and why>`

## lint

- Command: `<e.g. npm run lint>`
- Single file: `<e.g. npx eslint <path>>`
- Duration: `<…>`

## test

- Full suite: `<e.g. npm test>` (`<duration>`)
- Single file: `<e.g. npm run test:file -- <path>>` (`<duration>`)
- Watch, if useful: `<…>`
- Notes: `<fixtures location, anything that must be running first>`

## format

- Check: `<e.g. npm run format:check>`
- Fix: `<e.g. npm run format>`

## smoke

- Command: `<e.g. npm run smoke>`
- Asserts: `<what one thing it checks>`

## dev logs

- Start with logging: `<e.g. npm run dev:log>`
- Read: `<e.g. tail -n 100 .logs/dev.log>`
- Notes: `<port, env vars needed>`

## browser (web apps only)

- Headless: `<e.g. npx playwright test smoke.spec.ts>`
- Harness browser tool, if any: `<name>`
- Base URL: `<e.g. http://localhost:3000>`

## guardrail

- Pre-commit runs: `<typecheck, lint, test on staged>`
- CI runs: `<check, on push>` or `none (no remote)`

## everything

- `<e.g. npm run check>` runs typecheck, lint, format:check, and the full suite, in that order. `<duration>`
