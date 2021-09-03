import re
import sys

MODULE_REGEX = re.compile(r"^[a-z][a-z0-9\-\_]+[a-z0-9]$")
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

module_name = "{{ cookiecutter.project_name }}"
version = "{{ cookiecutter.version }}"


def validate_project_name() -> None:
    """Ensure that `project_name` parameter is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.

    Raises:
        ValueError: If module_name is not a valid Python module name
    """
    if MODULE_REGEX.fullmatch(module_name) is None:
        message = f"ERROR: The project name `{module_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_semver() -> None:
    """Ensure version in semver notation.

    Raises:
        ValueError: If version is not in semver notation
    """
    if SEMVER_REGEX.fullmatch(version) is None:
        message = f"ERROR: The `{version}` is not in semver notation (https://semver.org/)"
        raise ValueError(message)


for validator in [validate_project_name, validate_semver]:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
