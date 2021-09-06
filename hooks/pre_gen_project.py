import re
import sys

PROJECT_REGEX = re.compile(r'^[A-Za-z0-9_.-]+$')
PACKAGE_REGEX = re.compile(r'^[a-z][a-z0-9\-\_]+[a-z0-9]$')
SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)


def validate_project_name() -> None:
    """Ensure that `project` parameter is valid.

    Valid inputs include only alphanumeric characters, as well as '_', '.', '-'

    Raises:
        ValueError: If `project` is not a valid Python module name
    """
    if PROJECT_REGEX.fullmatch('{{cookiecutter.project_name}}') is None:
        message = 'ERROR: `{0}` is not a valid GitHub repository name.'.format(
            '{{cookiecutter.project_name}}',
        )
        raise ValueError(message)


def validate_package_name() -> None:
    """Ensure that `package_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Raises:
        ValueError: If `package_name` is not a valid Python module name
    """
    if PACKAGE_REGEX.fullmatch('{{cookiecutter.package_name}}') is None:
        message = 'ERROR: `{0}` is not a valid Python package name.'.format(
            '{{cookiecutter.package_name}}',
        )
        raise ValueError(message)


def validate_semver() -> None:
    """Ensure `version` is in semver notation.

    Raises:
        ValueError: If `version` is not in semver notation
    """
    if SEMVER_REGEX.fullmatch('{{cookiecutter.version}}') is None:
        message = 'ERROR: `{0}` is not in semver notation (https://semver.org/)'.format(
            '{{cookiecutter.version}}',
        )
        raise ValueError(message)


def validate_skip_setup() -> None:
    """Ensure `skip_setup` is boolean.

    Raises:
        ValueError: If `skip_setup` is not boolean
    """
    if '{{cookiecutter.skip_setup}}' not in {'False', 'True'}:
        message = 'ERROR: `{0}` is not a boolean value'.format(
            '{{cookiecutter.skip_setup}}',
        )
        raise ValueError(message)


VALIDATORS = [
    validate_skip_setup,
    validate_project_name,
    validate_package_name,
    validate_semver,
]

for validator in VALIDATORS:
    try:
        validator()
    except ValueError as ex:
        print(ex)  # noqa: WPS421
        sys.exit(1)
