{% if cookiecutter.create_example_cli == 'y' -%}
from typer.testing import CliRunner

from {{ cookiecutter.module_name }}.main import app

runner = CliRunner()


def test_hello_command():
    result = runner.invoke(app, ["World"])
    assert result.exit_code == 0
    assert "Hello World" in result.stdout
{% else -%}
def test_placeholder():
    """
    A placeholder test for projects without a CLI example.
    """
    assert True
{% endif -%}
