# Terra 🤖

**Terra** is an Agile Project Management and Code Assistant system for AI agents across multiple environments. This methodology will help you generate Product Requirements Documents (PRDs) and Task Lists for prototypes and large projects with many features.

## 🚀  Getting started with Terra

### Requirements

- Windsurf/Roo VSCode extension/GitHub Copilot/Cursor
- Google Gemini Gems
- Mise or Python 3.6+

### Setup Gemini Gems

1.  Run `mise install` if Python is not already on your system.
2.  Run `mise run build` or `python scripts/build.py`.
3.  Open Google Gemini's Gem page.
4.  Create a new Gem.
4.  From the `build/gem` folder, the `agent-prompt.txt` should be pasted into the instructions box. All other txt files should be added to the Knowledge box.
5.  Start prompting.

### Setup Dev Agent Rules

1.  Run `mise install` if Python 3.13+ is not already on your system.
2.  Run `mise run build` or `python scripts/build.py`.
3.  Copy over applicable files from `build/ide-rules` based on your IDE(s) to your project folders.
4.  Start prompting. _(Note: Roo Code rules only)

## Project Document Generation

Terra guides users through planning software projects using an AI assistant, the "Agile Project Planner," facilitated by a Google Gemini Gem. This assistant helps generate `PRD.md` (Product Requirements Document) and `TASKS.md` (Task List) files. The process is driven by user-selected workflows and templates.

**Core Functionality:**

The AI assistant operates based on the following principles:
-   **Workflow Selection:** The user chooses one of three workflows:
    1.  **Prototyper:** For rapidly planning small-scale prototypes. Requires a `templates.txt` file with `<PROTO_PRD_TEMPLATE>` and `<TASKS_TEMPLATE>`.
    2.  **Product Developer Workflow (PDW):** For planning the foundational platform of a new, larger product. Requires a `templates.txt` file with `<PROD_PRD_TEMPLATE>` and `<TASKS_TEMPLATE>`.
    3.  **Feature Developer Workflow (FDW):** For planning a new feature for an existing product. Requires the main `PROD_PRD.md` of the existing platform and a `templates.txt` file with `<FEAT_PRD_TEMPLATE>` and `<TASKS_TEMPLATE>`.
-   **Template-Driven Generation:** The structure and content of the `PRD.md` and `TASKS.md` files are strictly based on templates provided by the user in a `templates.txt` file. These templates are typically derived from the examples in the `gem/` folder:
    -   [`PROD_PRD_TEMPLATE.md`](gem/PROD_PRD_TEMPLATE.md)
    -   [`FEAT_PRD_TEMPLATE.md`](gem/FEAT_PRD_TEMPLATE.md)
    -   [`PROTO_PRD_TEMPLATE.md`](gem/PROTO_PRD_TEMPLATE.md)
    -   [`TASKS_TEMPLATE.md`](gem/TASKS_TEMPLATE.md)
-   **Collaborative Process:** The AI engages in a dialogue with the user, asking clarifying questions and refining document drafts based on feedback.
-   **Output:** The final outputs are clean Markdown-formatted `PRD.md` and `TASKS.md` files, placed in the project's working directory (e.g., `project/PRD.md`, `project/TASKS.md`).

**Supporting Files:**
-   **Agent Prompts & Rules**:
    *   [`agent-prompt.md`](gem/agent-prompt.md): Provides the core instructions for the AI assistant.
    *   [`DEV-RULES.md`](ide-rules/DEV-RULES.md): Contains specific rules for AI development agents (like Roo) to follow, ensuring consistency.
-   **(Optional) `digest.txt`**: A summary of the current project state to provide quick context to the AI agent.

## References

I was heavily inspired by the [BMAD Method](https://github.com/bmadcode/BMAD-METHOD) and [claude-task-master](https://github.com/eyaltoledano/claude-task-master).

## License

This project is licensed under the MIT License. See [LICENSE](docs/LICENSE) for details.
