import contextlib
import datetime
import os
import shlex
import subprocess

import pytest
from cookiecutter.utils import rmtree


@contextlib.contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    Args:
        dirpath ([string]): path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


@contextlib.contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        if result.exception is not None:
            with contextlib.suppress(FileNotFoundError):
                rmtree(str(result.project_path))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project_path is not None
        assert result.project_path.is_dir()

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert ".github" in found_toplevel_files
        assert "docs" in found_toplevel_files
        assert "src" in found_toplevel_files
        assert "tests" in found_toplevel_files
        assert ".all-contributorsrc" in found_toplevel_files
        assert ".deepsource.toml" in found_toplevel_files
        assert ".editorconfig" in found_toplevel_files
        assert ".gitignore" in found_toplevel_files
        assert ".gitpod.Dockerfile" in found_toplevel_files
        assert ".gitpod.yml" in found_toplevel_files
        assert ".pre-commit-config.yaml" in found_toplevel_files
        assert "CHANGELOG.md" in found_toplevel_files
        assert "LICENSE" in found_toplevel_files
        assert "mkdocs.yml" in found_toplevel_files
        assert "pyproject.toml" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "renovate.json" in found_toplevel_files
        assert "tox.ini" in found_toplevel_files


def test_bake_withspecialchars(cookies):
    """Ensure that a `project_name` with double quotes is invalid"""
    with bake_in_temp_dir(cookies, extra_context={"project_name": 'name "quote" name'}) as result:
        assert result.exit_code != 0
        assert result.exception is not None


def test_bake_with_apostrophe(cookies):
    """Ensure that a `project_name` with apostrophes is invalid"""
    with bake_in_temp_dir(cookies, extra_context={"project_name": "O'connor"}) as result:
        assert result.exit_code != 0
        assert result.exception is not None


def test_year_compute_in_license_file(cookies):
    with bake_in_temp_dir(cookies) as result:
        timespan = '{0}-{0}'.format(
            datetime.datetime.utcnow().year,
        )

        license_text = (result.project_path / "LICENSE").read_text()

        assert timespan in license_text


@pytest.mark.parametrize(
    "license_name,license_text_span",
    [
        ("mit", "MIT"),
        (
            "bsd-2-clause",
            "Redistributions of source code must retain the above copyright notice",
        ),
        ("apache-2.0", "Licensed under the Apache License, Version 2.0"),
        ("gpl-3.0", "GNU GENERAL PUBLIC LICENSE"),
    ],
)
def test_bake_selecting_license(cookies, license_name, license_text_span):
    with bake_in_temp_dir(cookies, extra_context={"license": license_name}) as result:
        license_text = (result.project_path / "LICENSE").read_text()

        assert license_text_span in license_text

        pyproject_toml_text = (result.project_path / "pyproject.toml").read_text()

        assert license_name.upper() in pyproject_toml_text


@pytest.mark.parametrize(
    "command", ["black --check .", "isort --check .", "flakehell lint", "pytest"]
)
def test_various_commands(cookies, command):
    with bake_in_temp_dir(cookies) as result:
        assert result.exception is None
        assert result.exit_code == 0
        assert result.project_path is not None
        assert result.project_path.is_dir()
        assert run_inside_dir(command, str(result.project_path)) == 0
