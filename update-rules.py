import os
import re
import subprocess # Added for the llm utility function

# --- Configuration ---
# NOTE: Paths are relative to the script's execution directory.
# Assumes the script is run from the root of the ai-rules repository.
source_file = "rules/CODE-RULES-CONDENSED.md"
target_files_full_overwrite = [
    "rules/github/.github/copilot-instructions.md",
    "rules/windsurf/.windsurfrules",
    "rules/roo/.roo/rules-code/rules.md",
]
target_file_partial_overwrite = "rules/cursor/.cursor/global.mdc"
llm_source_file = "rules/CODE-RULES.md" # Source for the llm utility
# --- End Configuration ---

def read_file_content(filepath):
  """Reads the entire content of a file."""
  try:
    with open(filepath, 'r', encoding='utf-8') as f:
      return f.read()
  except FileNotFoundError:
    print(f"Error: File not found at {filepath}")
    return None
  except Exception as e:
    print(f"Error reading file {filepath}: {e}")
    return None

def write_file_content(filepath, content):
  """Writes content to a file, overwriting it."""
  try:
    # Ensure directory exists if it's part of the path
    dir_path = os.path.dirname(filepath)
    if dir_path: # Only create if dirname is not empty (i.e., not a root file)
        os.makedirs(dir_path, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
      f.write(content)
    print(f"Successfully updated: {filepath}")
  except Exception as e:
    print(f"Error writing to file {filepath}: {e}")

def update_partial_overwrite_file(filepath, new_content_after_frontmatter):
  """Updates a file, preserving YAML frontmatter."""
  try:
    with open(filepath, 'r', encoding='utf-8') as f:
      lines = f.readlines()

    if not lines or not lines[0].strip() == '---':
      print(f"Warning: No YAML frontmatter start ('---') found in {filepath}. Overwriting entire file.")
      write_file_content(filepath, new_content_after_frontmatter)
      return

    frontmatter_end_index = -1
    for i, line in enumerate(lines):
      # Find the *second* '---' line which marks the end of frontmatter
      if i > 0 and line.strip() == '---':
        frontmatter_end_index = i
        break

    if frontmatter_end_index == -1:
      print(f"Warning: Could not find end of YAML frontmatter ('---') in {filepath}. Appending content after first line.")
      frontmatter = lines[0]
      # Ensure there's a newline between frontmatter and new content if needed
      if not new_content_after_frontmatter.startswith('\n'):
          new_content_after_frontmatter = '\n' + new_content_after_frontmatter
      full_content = frontmatter + new_content_after_frontmatter

    else:
      frontmatter_lines = lines[:frontmatter_end_index + 1]
      frontmatter = "".join(frontmatter_lines)
      # Ensure there's a newline between frontmatter and new content if needed
      # Handle cases: FM ends \n\n, FM ends \n, New starts \n
      if frontmatter.endswith('\n\n'):
          # If frontmatter already ends with double newline, remove leading newline from new content if present
          if new_content_after_frontmatter.startswith('\n'):
              new_content_after_frontmatter = new_content_after_frontmatter[1:]
      elif frontmatter.endswith('\n'):
          # If frontmatter ends with single newline, ensure one more newline unless new content starts with one
           if not new_content_after_frontmatter.startswith('\n'):
               new_content_after_frontmatter = '\n' + new_content_after_frontmatter
      else: # Frontmatter doesn't end with newline
          if not new_content_after_frontmatter.startswith('\n'):
              new_content_after_frontmatter = '\n' + new_content_after_frontmatter # Needs at least one separator

      full_content = frontmatter + new_content_after_frontmatter

    write_file_content(filepath, full_content)

  except FileNotFoundError:
    print(f"Warning: Target file not found at {filepath}. Creating new file (without frontmatter preservation).")
    # If the file doesn't exist, we can't preserve frontmatter, so just write the new content.
    write_file_content(filepath, new_content_after_frontmatter)
  except Exception as e:
    print(f"Error processing partial overwrite for {filepath}: {e}")

# --- New Function for LLM Utility ---
def update_llm_utility(source_md_file):
    """
    Reads content from source_md_file and (TODO) pipes it to the 'llm' command-line utility.
    """
    print(f"\nAttempting to process for llm utility: {source_md_file}")
    content = read_file_content(source_md_file)
    if content is None:
        print(f"Error: Could not read {source_md_file} for llm utility.")
        return

    print(f"Successfully read {len(content)} characters from {source_md_file}.")
    # print("TODO: Implement piping content to 'llm' command line utility.")
    # --- TODO: Implement the actual command line call below ---
    # Example using subprocess (replace with actual command and arguments):
    # try:
    #     process = subprocess.run(['llm', '--system', '-'], input=content, text=True, check=True, capture_output=True)
    #     print(f"'llm' utility processed content successfully.")
    #     # print("Output from llm:", process.stdout) # Optional: print llm output
    # except FileNotFoundError:
    #     print("Error: 'llm' command not found. Make sure it's installed and in your PATH.")
    # except subprocess.CalledProcessError as e:
    #     print(f"Error executing 'llm': {e}")
    #     print("Stderr:", e.stderr)
    # except Exception as e:
    #     print(f"An unexpected error occurred while running 'llm': {e}")
    # --- End TODO ---


# --- Main Execution ---
print("--- Starting Rule Update Script ---")
print(f"Assuming script is run from the project root: {os.getcwd()}") # Show current dir

print(f"\nReading source content from: {source_file}")
source_content = read_file_content(source_file)

if source_content is not None:
  # Process full overwrites
  print("\nProcessing full overwrite files...")
  for target_file in target_files_full_overwrite:
    write_file_content(target_file, source_content)

  # Process partial overwrite
  print("\nProcessing partial overwrite file (preserving frontmatter)...")
  update_partial_overwrite_file(target_file_partial_overwrite, source_content)

  # Process the llm utility update (currently placeholder)
  print("\nProcessing LLM utility update (TODO)...")
  update_llm_utility(llm_source_file)

  print("\n--- Script finished ---")
else:
  print("\n--- Script aborted due to error reading source file ---")

