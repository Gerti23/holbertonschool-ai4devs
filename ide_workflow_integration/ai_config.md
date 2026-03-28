# AI Assistant Configuration

Date: 2026-03-28  
Scope: `ide_workflow_integration`

## Purpose
Define AI-assisted coding behavior in this project for consistent style, safer reviews, and faster documentation workflows.

## Assistant Setup
1. Install and enable GitHub Copilot and GitHub Copilot Chat in VS Code.
2. Sign in with GitHub account in VS Code.
3. Keep inline suggestions enabled in editor settings.
4. Store project-level AI behavior in `.copilot-settings.yaml` (repo root for this directory).

## Config Files Added
- `.copilot-settings.yaml` (project root)

## Language-Specific Rules
- Python:
  - Formatter style aligned with `black`
  - Prefer explicit type hints for public functions
  - Favor small, testable functions
- JavaScript:
  - Style aligned with Airbnb conventions
  - Require semicolons
  - Prefer `const` over `let` when values are not reassigned
- Markdown:
  - Use concise headings
  - Keep checklist/acceptance sections explicit and uniform

## Specialized AI Workflows
### 1) Code Review Workflow
- Goal: Catch defects early before commit.
- Focus areas: security, performance, readability, and edge cases.
- Trigger: Run on demand before PR/commit.

### 2) Documentation Generator Workflow
- Goal: Produce/refresh task specs and setup docs quickly.
- Outputs: structured markdown with sections for requirements, inputs, outputs, and acceptance criteria.
- Trigger: Run when creating benchmark tasks, setup notes, or workflow summaries.

## Validation Checklist
- [ ] AI suggestions visible in editor.
- [ ] Chat can answer project questions.
- [ ] `.copilot-settings.yaml` exists and is readable.
- [ ] Language rules and workflows are present in config.
