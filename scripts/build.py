import os
import shutil

# Define base paths
GEM_SOURCE_DIR = "gem"
IDE_RULES_SOURCE_DIR = "ide-rules"
BUILD_DIR = "build"
BUILD_GEM_DIR = os.path.join(BUILD_DIR, "gem")
BUILD_IDE_RULES_DIR = os.path.join(BUILD_DIR, "ide-rules")

# Files to be processed for templates.txt
TEMPLATE_FILES_INFO = [
    {"path": os.path.join(GEM_SOURCE_DIR, "FEAT_PRD_TEMPLATE.md"), "tag": "FEAT_PRD_TEMPLATE"},
    {"path": os.path.join(GEM_SOURCE_DIR, "PROD_PRD_TEMPLATE.md"), "tag": "PROD_PRD_TEMPLATE"},
    {"path": os.path.join(GEM_SOURCE_DIR, "PROTO_PRD_TEMPLATE.md"), "tag": "PROTO_PRD_TEMPLATE"},
    {"path": os.path.join(GEM_SOURCE_DIR, "TASKS_TEMPLATE.md"), "tag": "TASKS_TEMPLATE"},
    {"path": os.path.join(GEM_SOURCE_DIR, "OPERATIONAL_GUIDELINES_TEMPLATE.md"), "tag": "OPERATIONAL_GUIDELINES_TEMPLATE"},
]

AGENT_PROMPT_SOURCE = os.path.join(GEM_SOURCE_DIR, "agent-prompt.md")
AGENT_PROMPT_DEST = os.path.join(BUILD_GEM_DIR, "agent-prompt.txt")
TEMPLATES_DEST = os.path.join(BUILD_GEM_DIR, "templates.txt")

DEV_RULES_SOURCE = os.path.join(IDE_RULES_SOURCE_DIR, "DEV-RULES.md")

CURSOR_RULES_PREPEND = """---
description: Apply this rule to the entire repository
globs:
alwaysApply: true
---

"""

WINDSURF_RULES_PREPEND = """---
trigger: always_on
---

"""

def create_directories():
    """Clean and create necessary build directories."""
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
        print(f"Removed existing build directory: {os.path.abspath(BUILD_DIR)}")
    print(f"Build directory is: {os.path.abspath(BUILD_DIR)}\n")

    os.makedirs(BUILD_GEM_DIR, exist_ok=True)
    print(f"Successfully created directory: {os.path.abspath(BUILD_GEM_DIR)}")
    os.makedirs(BUILD_IDE_RULES_DIR, exist_ok=True)
    print(f"Successfully created directory: {os.path.abspath(BUILD_IDE_RULES_DIR)}")

    # Create subdirectories for IDE rules
    os.makedirs(os.path.join(BUILD_IDE_RULES_DIR, ".cursor", "rules"), exist_ok=True) # .cursor now under ide-rules
    os.makedirs(os.path.join(BUILD_IDE_RULES_DIR, ".github"), exist_ok=True)
    os.makedirs(os.path.join(BUILD_IDE_RULES_DIR, ".roo", "rules-code"), exist_ok=True) # Updated Roo path
    os.makedirs(os.path.join(BUILD_IDE_RULES_DIR, ".windsurf", "rules"), exist_ok=True)
    print(f"  Created subdirectories within {os.path.abspath(BUILD_IDE_RULES_DIR)} for .cursor/rules, .github, .roo/rules-code, .windsurf\n")


def build_agent_prompt():
    """Copy agent-prompt.md to agent-prompt.txt."""
    try:
        shutil.copyfile(AGENT_PROMPT_SOURCE, AGENT_PROMPT_DEST)
        print(f"Successfully generated '{os.path.abspath(AGENT_PROMPT_DEST)}'\n")
    except FileNotFoundError:
        print(f"Error: Source file not found - {os.path.abspath(AGENT_PROMPT_SOURCE)}")
    except Exception as e:
        print(f"Error copying {AGENT_PROMPT_SOURCE}: {e}")

def build_templates_file():
    """Merge specified markdown files into templates.txt, wrapped in tags."""
    abs_templates_dest = os.path.abspath(TEMPLATES_DEST)
    print(f"Processing '{GEM_SOURCE_DIR}' directory into '{abs_templates_dest}'")
    try:
        with open(TEMPLATES_DEST, "w", encoding="utf-8") as outfile:
            for file_info in TEMPLATE_FILES_INFO:
                source_path = file_info["path"]
                abs_source_path = os.path.abspath(source_path)
                tag_name = file_info["tag"]
                try:
                    with open(source_path, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        outfile.write(f"<{tag_name}>\n")
                        outfile.write(content)
                        outfile.write(f"\n</{tag_name}>\n\n") # Add a newline for separation
                    print(f"  Appending content from '{source_path}' (as '{tag_name}') to '{abs_templates_dest}'")
                except FileNotFoundError:
                    print(f"  Warning: Template source file not found - {abs_source_path}. Skipping.")
                except Exception as e:
                    print(f"  Error reading {abs_source_path}: {e}. Skipping.")
        print(f"Finished processing '{GEM_SOURCE_DIR}'.\n")
    except Exception as e:
        print(f"Error writing to {abs_templates_dest}: {e}\n")

def build_rules_files():
    """Create IDE-specific rule files based on DEV-RULES.md."""
    print(f"Processing IDE rules files from '{os.path.abspath(IDE_RULES_SOURCE_DIR)}'...")
    abs_dev_rules_source = os.path.abspath(DEV_RULES_SOURCE)
    try:
        with open(DEV_RULES_SOURCE, "r", encoding="utf-8") as f_dev_rules:
            dev_rules_content = f_dev_rules.read()
        print(f"  Read content from '{abs_dev_rules_source}'")

        # Cursor rules
        cursor_rules_path = os.path.join(BUILD_IDE_RULES_DIR, ".cursor", "rules", "global.mdc") # .cursor now under ide-rules
        abs_cursor_rules_path = os.path.abspath(cursor_rules_path)
        with open(cursor_rules_path, "w", encoding="utf-8") as f_cursor:
            f_cursor.write(CURSOR_RULES_PREPEND)
            f_cursor.write(dev_rules_content)
        print(f"  Successfully created '{abs_cursor_rules_path}'")

        # GitHub Copilot instructions
        github_rules_path = os.path.join(BUILD_IDE_RULES_DIR, ".github", "copilot-instructions.md")
        abs_github_rules_path = os.path.abspath(github_rules_path)
        with open(github_rules_path, "w", encoding="utf-8") as f_github:
            f_github.write(dev_rules_content)
        print(f"  Successfully created '{abs_github_rules_path}'")

        # Roo rules
        roo_rules_path = os.path.join(BUILD_IDE_RULES_DIR, ".roo", "rules-code", "rules.md") # Updated Roo path
        abs_roo_rules_path = os.path.abspath(roo_rules_path)
        with open(roo_rules_path, "w", encoding="utf-8") as f_roo:
            f_roo.write(dev_rules_content)
        print(f"  Successfully created '{abs_roo_rules_path}'")

        # Windsurf rules
        windsurf_rules_path = os.path.join(BUILD_IDE_RULES_DIR, ".windsurf", "rules", "rules.md")
        abs_windsurf_rules_path = os.path.abspath(windsurf_rules_path)
        with open(windsurf_rules_path, "w", encoding="utf-8") as f_windsurf:
            f_windsurf.write(WINDSURF_RULES_PREPEND)
            f_windsurf.write(dev_rules_content)
        print(f"  Successfully created '{abs_windsurf_rules_path}'")
        print("Finished processing IDE rules files.\n")

    except FileNotFoundError:
        print(f"Error: DEV-RULES.md not found at {abs_dev_rules_source}. Skipping rule file generation.\n")
    except Exception as e:
        print(f"Error during rule file generation: {e}\n")


def main():
    """Main function to run the build process."""
    print("Starting build process...\n")
    print(f"Using resolved asset folder root: {os.path.abspath('.')}\n")


    create_directories()
    build_agent_prompt()
    build_templates_file()
    build_rules_files()
    print("Build process completed.")

if __name__ == "__main__":
    main()