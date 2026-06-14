# Caveman Commit

Generate conventional commit message for staged changes.

Rules:
- Subject ≤50 chars
- Format: `type(scope): description`
- Types: feat, fix, refactor, docs, test, chore
- No filler, no "this commit", no periods at end
- Body optional, only if truly needed

Run `git diff --cached` to see staged changes, then output only the commit message (no explanation).
