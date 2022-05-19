"""Command-line interface."""
import click
import sys

if sys.version_info[:2] >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version(__package__)

del metadata, sys  # optional


@click.command()
@click.version_option(__version__)
def main() -> None:
    """{{cookiecutter.project_name}}."""


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
