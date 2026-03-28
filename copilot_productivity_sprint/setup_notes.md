# Setup Notes — Copilot Productivity Sprint

Date: 2026-03-28  
Repository: `holbertonschool-ai4devs`  
Directory: `copilot_productivity_sprint`

## 1) IDE Setup (VS Code)

1. Install Visual Studio Code (stable) for Linux.
2. Open the project folder:
   - `File -> Open Folder...`
   - Select `holbertonschool-ai4devs`.
3. Sign in to GitHub from VS Code:
   - `Accounts` (bottom-left) -> `Sign in with GitHub`.

## 2) AI Assistant Setup (GitHub Copilot)

1. Open Extensions (`Ctrl+Shift+X`).
2. Install:
   - **GitHub Copilot** (`GitHub.copilot`)
   - **GitHub Copilot Chat** (`GitHub.copilot-chat`)
3. Reload VS Code if prompted.
4. Confirm Copilot is enabled:
   - `Ctrl+Shift+P` -> `Copilot: Toggle Copilot` (should be ON).
5. Confirm chat works:
   - Open Copilot Chat panel and send a test prompt.

Environment note (WSL): running `code --install-extension github.copilot` reported success but installed/listed only `github.copilot-chat` in this environment.

## 3) Optional Alternative Assistant

If Copilot is unavailable, install one alternative (example):
- **Codeium** (`Codeium.codeium`)

## 4) Recommended VS Code Settings for Testing

Add/update user settings (`settings.json`):

```json
{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true,
    "scminput": false
  }
}
```

## 5) Version Log

Record exact versions used during testing.

### IDE
- VS Code version: `1.109.5` (commit `072586267e68ece9a47aa43f8c108e0dcbf44622`, `x64`)

### Extensions
- GitHub Copilot (`GitHub.copilot`): `not installed`
- GitHub Copilot Chat (`GitHub.copilot-chat`): `0.37.9`
- (Optional) Codeium (`Codeium.codeium`): `not installed`

### Tools
- Git: `2.34.1`
- Node.js: `not installed`
- npm: `10.9.2`
- Python: `3.10.12`

## 6) Commands to Collect Versions

Run in terminal and paste outputs above:

```bash
code --version
git --version
node --version
npm --version
python3 --version
```

For extension versions in VS Code:
- Extensions panel -> select extension -> read `Version` field.

## 7) Validation Checklist

- [ ] VS Code opens repository successfully.
- [ ] GitHub account signed in.
- [ ] GitHub Copilot extension installed and enabled.
- [ ] Copilot Chat installed and responding.
- [ ] Tool versions captured in this file.
