import os
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd()


def initialize_git():
    """Initializes a git repository and makes an initial commit."""
    if not (PROJECT_DIRECTORY / ".git").exists():
        print("Initializing git repository...")
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "Initial commit from cookiecutter template"')
        print("Git repository initialized.")


def setup_project():
    """Sets up project dependencies and git hooks using mise."""
    print("Setting up project with mise (installing dependencies and git hooks)...")
    print("Note: this will also trust the mise config for your project: https://mise.jdx.dev/cli/trust.html")
    os.system("mise trust .")
    os.system("mise run setup")
    print("Project setup complete.")


if __name__ == "__main__":
    initialize_git()
    setup_project()

    print("\nProject generation complete!")
    print("Next steps:")
    print(f"  `cd {PROJECT_DIRECTORY.name}`")
    print("  `mise check` (to run linting, formatting, typing, and tests)")
    print("  `git push` (if you initialized a remote repository)")
