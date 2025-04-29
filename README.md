# 🤖 AI Rules: Universal Agent Governance

Welcome to **AI Rules** — a unified ruleset system for AI agents across multiple environments!

> **Note:** [`RULES.md`](./RULES.md) is a functional equivalent that captures the spirit of these rules, but is not shortened or optimized for direct AI consumption.

## 🌍 Supported Environments

- **Cursor**: Code-assistant focused rules.
- **Roo**: Comprehensive project management and code quality rules.
- **Windsurf**: Uses the same rules as Roo.

---

## 🚦 Getting Started

1. **Clone this repository** to your local machine.
2. **Copy the rules file** for your environment:
   - For **Cursor**, use `.cursor/global.mdc`.
   - For **Roo**, use `.roo/rules-code/rules.md`.
   - For **Windsurf**, use `.windsurfrules` (identical to Roo).
3. **Apply the rules** according to your IDE/extension’s documentation.

---

## 📚 How the Rules Work

- **`.cursor/global.mdc`**: Concise, code-assistant-focused rules. Emphasizes working directly from the `project` folder for requirements, tasks, and state. Promotes clarity, minimal code, and always asks for clarification if requirements are unclear.

- **`.roo/rules-code/rules.md` & `.windsurfrules`**: Full project management and code quality rules. Require agents to:
  - Review `project/PRD.md` (architecture, style), `project/TASKS.md` (assignments), and `project/digest.txt` (state) before coding.
  - Present a plan before making changes.
  - Only work on assigned tasks.
  - Follow strict folder structure (`src/` for all code).
  - Write tests, document decisions, and update the README as needed.

---

## 🗂️ The `project` Folder: Your Source of Truth

- **`project/PRD.md`**: Product requirements, architecture, and style guide.
- **`project/TASKS.md`**: Task assignments and tracking.
- **(Optional) `project/digest.txt`**: Current project state or summary.

> 🗒️ Agents must consult these files before starting any work. This ensures all contributions are aligned with the latest requirements, assignments, and project status.

---

## 🚀 Workflow Overview

1. **Clone and configure**: Set up the rules file for your environment.
2. **Review `project/`**: Always check `PRD.md` and `TASKS.md` before starting.
3. **Follow the rules**: All code, decisions, and documentation must comply with the selected ruleset.
4. **Contribute with confidence**: The rules enforce quality, clarity, and strong project management.

---

> 💡 For detailed rules and process breakdowns, see [`RULES.md`](./RULES.md) and the environment-specific rule files.
