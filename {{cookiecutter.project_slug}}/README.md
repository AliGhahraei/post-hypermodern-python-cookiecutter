# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Usage

```bash
{{ cookiecutter.project_slug.replace('-', '_') }} --help
```

## Development

To set up a development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
   cd {{ cookiecutter.project_slug }}
   ```
2. Setup up everything for your dev environment using `mise`:
   ```bash
   mise setup
   ```
3. Run all checks locally and fast (tests, type checks, linting, formatting, etc.):
   ```bash
   mise check
   ```
4. (Optional) Run the CI GitHub Action locally (same as above, but slower and more accurate)
   ``` bash
   mise local_ci
   ```

## License

This project is licensed under the {{ cookiecutter.license }} License.
