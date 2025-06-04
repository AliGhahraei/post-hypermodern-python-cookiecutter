from subprocess import run
from pathlib import Path

PROJECT_DIRECTORY = Path().cwd()

WARNING = '\033[93m'
EMPHASIZE = '\033[92m'
END = '\033[0m'


def warning(msg):
    print(f'{WARNING}{msg}{END}')


def emphasize(msg):
    print(f'\n{EMPHASIZE}{msg}{END}')


def initialize_git():
    """Initializes a git repository and makes an initial commit."""
    if not (PROJECT_DIRECTORY / ".git").exists():
        emphasize("Initializing git repository...")
        run("git init", shell=True, check=True)
        run("git add .", shell=True, check=True)
        run('git commit -m "Initial commit from cookiecutter template"', shell=True, check=True)
        print("Git repository initialized.")


def setup_project():
    """Sets up project dependencies and git hooks using mise."""
    emphasize("Setting up project with mise (installing dependencies and git hooks)...")
    warning("NOTE: this will also trust the mise config for your project: https://mise.jdx.dev/cli/trust.html")
    run("mise trust .", shell=True, check=True)
    run("mise run setup", shell=True, check=True)
    print("Project setup complete.")


if __name__ == "__main__":
    initialize_git()
    setup_project()

    emphasize("\nProject generation complete!")
    print("Next steps:")
    print(f"  `cd {PROJECT_DIRECTORY.name}`")
    print("  `mise check` (to run linting, formatting, typing, and tests)")
    print("  `git push` (if/after you initialized a remote)")
