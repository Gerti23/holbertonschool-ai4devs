# Workflow Baseline

Date: 2026-03-28  
Repository: holbertonschool-ai4devs

## Current IDE Setup
- IDE: VS Code 1.109.5 (Linux / WSL)
- AI assistant: GitHub Copilot Chat (`github.copilot-chat` 0.37.9)
- Version control: Git 2.34.1
- Runtime/tools available: Python 3.10.12, npm 10.9.2
- Typical project utilities used: Markdown for specs, terminal commands for validation and git workflow

## Current Workflow
1. Read task requirements and identify expected output file(s).
2. Create or update project markdown/code files in the target directory.
3. Run quick command-line validation checks (versions, file presence, basic command output).
4. Review deliverable against rubric/acceptance criteria.
5. Commit and push changes once requirements are satisfied.

## Pain Points
- Requirement interpretation drift: small formatting mismatches can fail strict graders.
- Manual consistency checks: repeated section-by-section validation in markdown tasks is time-consuming.
- Iterative correction overhead: multiple rounds of tiny edits are needed when rubric checks are rigid.
- Environment mismatch issues: extension installation behavior differs between WSL and local desktop contexts.

## Productivity Metrics (Baseline)
- Average task completion time: 25–40 minutes per documentation task.
- Bug/issue fix turnaround (for failed checks): 10–20 minutes per iteration.
- First-pass acceptance rate: ~60% of tasks pass without revision.
- Weekly commit volume: ~15–25 commits/week.
- Rework rate: ~30–40% of tasks require at least one corrective edit.

## Baseline Summary
Current workflow is functional and relatively fast for small tasks, but productivity is reduced by strict-format failures and repeated manual verification. Improving template standardization and automated pre-submission checks should reduce rework and improve first-pass acceptance.
