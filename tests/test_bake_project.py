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
                rmtree(str(result.project))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
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
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert (
            '{0}-{0}'.format(
                now.year,
            )
            in license_file_path.read()
        )


@pytest.mark.parametrize(
    "license_name,license_text",
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
def test_bake_selecting_license(cookies, license_name, license_text):
    with bake_in_temp_dir(cookies, extra_context={"license": license_name}) as result:
        assert license_text in result.project.join("LICENSE").read()
        assert license_name.upper() in result.project.join("pyproject.toml").read()


@pytest.mark.parametrize(
    "command", ["black --check .", "isort --check .", "flakehell lint", "pytest"]
)
def test_various_commands(cookies, command):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert run_inside_dir(command, str(result.project)) == 0
