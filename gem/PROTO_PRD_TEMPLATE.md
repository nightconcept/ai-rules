# [Project Name] - Product Requirements Document (Prototype)

## 1. Introduction

* **Project Idea:** [Briefly describe the core concept of the project.]
* **Problem/Need:** [What problem does this project aim to solve or what primary need does it address?]
* **Prototype Goal:** [What is the main goal for this specific prototype? e.g., "Prove concept X," "Build a basic interactive demo of Y functionality," "Test integration with Z service."]

## 2. Core Features / User Stories

[List the essential functionalities required for this prototype. Focus on what the user should be able to do. If applicable, use a command-like structure for CLI tools or distinct actions.]

* **Feature 1: [Name of Feature/User Story]**
  * Description: [Brief description of the feature.]
  * User Action(s): [What does the user do?]
  * Outcome(s): [What is the expected result or output?]
  * *(For CLI/Commands, consider:)*
    * Command: `[command_name]`
    * Key Inputs: `[e.g., argument, flag, file]`
    * Expected Output: `[e.g., console message, file created, state change]`

* **Feature 2: [Name of Feature/User Story]**
  * Description: [...]
  * User Action(s): [...]
  * Outcome(s): [...]

* *(Add more features as needed for the prototype)*

## 3. Technical Specifications

* **Primary Language(s):** [e.g., Go, Python, JavaScript (Svelte)]
* **Key Frameworks/Libraries:** [e.g., Urfave/cli, specific UI libraries, data handling libraries]
* **Database (if any):** [e.g., None for prototype, SQLite, specific cloud DB]
* **Key APIs/Integrations (if any):** [e.g., GitHub API, external data source]
* **Deployment Target (if applicable for prototype):** [e.g., Local executable, basic web server]
* **High-Level Architectural Approach:** [Briefly describe the intended structure. e.g., "CLI application with modular commands," "Single-page web application with a Go backend," "Series of scripts."]
* **Critical Technical Decisions/Constraints:** [Any specific choices made or limitations to observe for this prototype.]

## 4. Project Structure

[Propose a basic file and directory layout for the prototype. This can be a simple tree structure.]

/project-root
  /src
  main.[ext]
  /scripts
  /docs
    PRD.md
    TASKS.md
README.md
[config_file_example.toml]

* `src/`: [Description]
* `docs/`: [Description]
* `[other_important_file_or_dir]`: [Description]

## 5. File Descriptions (If applicable)

[Briefly explain any key configuration files, input files, or important output files the prototype will use or generate.]

* **`[filename1.ext]`**: [Purpose, format (e.g., TOML, JSON, plain text), key contents/structure.]
* **`[filename2.ext]`**: [Purpose, format, key contents/structure.]

## 6. Future Considerations / Out of Scope (for this prototype)

* **Out of Scope for Prototype:**
  * [Feature/Aspect X - e.g., "User authentication," "Advanced error reporting," "Scalability beyond N users/requests"]
  * [Feature/Aspect Y]
* **Potential Future Enhancements (Post-Prototype):**
  * [Idea 1]
  * [Idea 2]

## 7. Project-Specific Coding Rules (Optional)

[Define any specific coding standards, style guides, or conventions to be followed for this prototype. This could include language version, formatting tools, naming conventions, etc. This section will inform the "rules files" for the AI coding process.]

* **Language Version:** [e.g., Go 1.21+, Python 3.10+]
* **Formatting:** [e.g., `gofmt`, `black`, `prettier`]
* **Linting:** [e.g., `golangci-lint`, `pylint`, `eslint` with specific config]
* **Key Principles:** [e.g., "Prefer clarity over conciseness," "Follow SOLID principles where applicable," "Minimize external dependencies for prototype."]
* **Naming Conventions:** [e.g., `camelCase` for functions, `PascalCase` for types in Go; `snake_case` in Python]
* **Testing (if applicable for prototype):** [e.g., "Basic unit tests for core logic," "No formal testing required for this speed prototype."]
