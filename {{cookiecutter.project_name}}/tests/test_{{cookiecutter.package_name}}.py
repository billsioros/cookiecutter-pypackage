"""Tests concerning the `{{ cookiecutter.package_name }}` module."""

from {{cookiecutter.package_name}}.{{cookiecutter.package_name}} import factorial


def test_{{ cookiecutter.package_name }}():
    assert factorial(5) == 120
