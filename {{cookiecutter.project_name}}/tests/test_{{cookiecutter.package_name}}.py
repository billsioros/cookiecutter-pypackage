"""Tests concerning the `{{ cookiecutter.package_name }}` module."""

from {{cookiecutter.package_name}}.{{cookiecutter.package_name}} import factorial


def test_{{ cookiecutter.package_name }}():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
