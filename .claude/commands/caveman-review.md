# Caveman Review

Review the current diff or PR changes. Output one-line findings only.

Format per finding: `L{line}: {🔴 bug|🟡 nit|🟢 ok}: {issue}`

Rules:
- No prose, no summaries
- Red = must fix, Yellow = optional, Green = praise worth noting
- Max 10 lines total
- Code unchanged in suggestions

Run `git diff HEAD` (or against base branch if on a feature branch) and review.
