# Terra

**Terra** is an Agile Project Management and Code Assistant system for AI agents across multiple environments. This methodology will help you generate Product Requirements Documents (PRDs) and Task Lists for prototypes and large projects with many features.

## Getting Started

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

## Working with Terra

Terra guides users through planning software projects using an AI assistant, the "Agile Project Planner," facilitated by a Google Gemini Gem. This assistant helps generate `PRD.md` (Product Requirements Document) and `TASKS.md` (Task List) files. The process is driven by user-selected workflows and templates.

-   **Gemini Workflows:** The user chooses one of three workflows:
    1.  **Prototyper:** For rapidly planning small-scale prototypes.
    2.  **Product Developer Workflow (PDW):** For planning the foundations of a new, larger product that will be iterated on with modular features developed by the Feature Development Workflow.
    3.  **Feature Developer Workflow (FDW):** For planning a new feature for an existing product. Requires a product `PRD.md` of an existing product. A digest from gitingest is recommended.
-   **Collaborative Process:** The AI engages in a dialogue with the user, asking clarifying questions and refining document drafts based on feedback.
-   **Output:** The final outputs are clean Markdown-formatted `PRD.md` and `TASKS.md` files, to be placed in the project's `docs/` directory or features `docs/feat/<feat_name>`.


## References

I was heavily inspired by the [BMAD Method](https://github.com/bmadcode/BMAD-METHOD) and [claude-task-master](https://github.com/eyaltoledano/claude-task-master).

## License

This project is licensed under the MIT License. See [LICENSE](docs/LICENSE) for details.
