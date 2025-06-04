# post-hypermodern-python-cookiecutter

The last cookiecutter template you'll need.

This repository contains a [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for quickly scaffolding new Python projects with a modern (at the time ;) ) set of development tools and best practices.

The name is a reference to the [Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) series and its [cookiecutter template](https://github.com/cjolowicz/cookiecutter-hypermodern-python).

## Features

The generated project comes pre-configured with:

*   **Tool version management** managed by [Mise](https://mise.jdx.dev/) using lock files for consistent environments. Manages Python versions and the other tools used in the template.
*   **Predefined maintenance commands** with [Mise](https://mise.jdx.dev/) as well (linting, formatting, testing, etc.).
*   **Project management** using [Poetry](https://python-poetry.org/) for dependencies, virtualenvs, etc.
*   **Linting & formatting** provided by [Ruff](https://docs.astral.sh/ruff/) at warp speed.
*   **Type checking** by [Basedpyright](https://docs.basedpyright.com/latest/) with Pylance features and improved rules over its parent project.
*   **Testing** employing [Pytest](https://docs.pytest.org/) for unit/integration testing, with [Coverage.py](https://coverage.readthedocs.io/) for test coverage reports.
*   **Git hooks** configured via Mise for pre-push checks to give rapid feedback to the developer.
*   **GitHub Actions CI** including a basic Continuous Integration workflow for automated checks.
*   **Local isolated execution of CI tasks** leveraging [Act](https://github.com/nektos/act) to run your actions in a docker container.
*   **CLI framework integration (optional)** which includes a sample [Typer](https://typer.tiangolo.com/) command-line interface structure if opted in during generation.

## How to Use the Template

To use this cookiecutter template to generate a new project:

1.  **Install Cookiecutter**:
    It is recommended to install `cookiecutter` using [pipx](https://pypa.github.io/pipx/), which installs Python applications in isolated environments.

    ```bash
    pipx install cookiecutter
    ```

2.  **Generate a new project**:
    You can use it directly:

    ```bash
    cookiecutter gh:AliGhahraei/post-hypermodern-python-cookiecutter
    ```

    If you want to clone the repo explicitly, do so and navigate to the directory where you want to create your new project. Afterwards, run the following command, pointing to this repository's directory:

    ```bash
    cookiecutter /path/to/repo
    ```

    Cookiecutter will prompt you for several project-specific details (e.g., project name, author, Python version, whether to include a CLI example).

3.  **Post-Generation Setup**:
    After you answer the prompts, the template's hook will automatically:
    *   Initialize a Git repository in your new project (If it's not a repo already).
    *   Make an initial commit (If it's not a repo already).
    *   Run `mise run setup` to install project dependencies and configure Git hooks.

## Why yet another python cookiecutter template?

I use a specific set of tools in my projects nowadays, so I wanted to have my own template and share it in case someone wants to use it someday.
