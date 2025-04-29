{ pkgs, inputs, ... }:
let
  # Import the unstable channel
  pkgs-unstable = import inputs.nixpkgs-unstable { system = pkgs.stdenv.system; };

  # Define the specific Python interpreter we want to use from unstable
  pythonPkg = pkgs-unstable.python313;

in
{
  packages = [
    # Include code2prompt from unstable
    pkgs-unstable.code2prompt

    # Create a Python environment containing llm and its plugins
    (pythonPkg.withPackages (ps: [
      # Add the base llm package
      ps.llm
      # Add the llm-gemini plugin package
      ps.llm-gemini
      # You can add other llm plugins here too, e.g.:
      # ps.llm-claude
    ]))
  ];

  # Configure the default Python environment for the shell
  languages.python = {
    enable = true;
    # Use the same Python interpreter defined above for consistency
    package = pythonPkg;
  };

}