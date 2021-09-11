<h1 align="center">🐍🍪 Yet another Python cookiecutter</h1>

<p align="center"><em>A strongly opinionated, bleeding-edge Python template</em></p>

<p align="center">
  <a href="https://github.com/billsioros/cookiecutter-pypackage/actions/workflows/ci.yml">
    <img
      src="https://github.com/billsioros/cookiecutter-pypackage/actions/workflows/ci.yml/badge.svg"
      alt="CI"
    />
  </a>
  <a href="https://github.com/billsioros/cookiecutter-pypackage/actions/workflows/cd.yml">
    <img
      src="https://github.com/billsioros/cookiecutter-pypackage/actions/workflows/cd.yml/badge.svg"
      alt="CD"
    />
  </a>
  <a href="https://results.pre-commit.ci/latest/github/billsioros/cookiecutter-pypackage/master">
    <img
      src="https://results.pre-commit.ci/badge/github/billsioros/cookiecutter-pypackage/master.svg"
      alt="pre-commit.ci status"
    />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img
      src="https://img.shields.io/github/license/billsioros/cookiecutter-pypackage"
      alt="GitHub"
    />
  </a>
  <a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fbillsioros%2Fcookiecutter-pypackage-instance?ref=badge_shield">
    <img
      src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fbillsioros%2Fcookiecutter-pypackage-instance.svg?type=shield"
      alt="FOSSA Status"
    />
  </a>
  <a href="https://www.buymeacoffee.com/billsioros">
    <img
      src="https://img.shields.io/badge/Buy%20me%20a-coffee-FFDD00.svg?style=flat&logo=buymeacoffee"
      alt="Buy me a coffee">
  </a>
</p>

## :bulb: Quickstart

Install the latest Cookiecutter

```
pip install -U cookiecutter
```

and generate a `Python` package project:

```
cookiecutter gh:billsioros/cookiecutter-pypackage
```

## :rocket: Features

* Dependency tracking using [`Poetry`](https://python-poetry.org/)
* Test automation with [`Tox`](https://github.com/tox-dev/tox)
* Documentation with [`MkDocs`](https://github.com/mkdocs/mkdocs/), [`Material for MkDocs`](https://github.com/squidfunk/mkdocs-material) and [`GitHub Pages`](https://pages.github.com/)
* Automated dependency and security updates with [`Renovate`](https://renovate.whitesourcesoftware.com/)
* Formatting provided by [Black][black] and [Isort][isort]
* Testing setup with [Pytest][pytest]
* Coverage reports on [Codecov][codecov]
* Static type checking by [Mypy][mypy]
* Security checks with [`CodeQL`](https://github.com/github/codeql-action)
* Linting provided by [`Flakehell`](https://github.com/flakehell/flakehell) and [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide)
* Automatic documentation from source code via [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings/)
* Git hooks managed by [`pre-commit`](https://pre-commit.com/).
* Development tasks (lint, format, test, etc) provided by [`Poe The Poet`](https://github.com/nat-n/poethepoet)
* Manage project labels with [`GitHub Labeler`](crazy-max/ghaction-github-labeler@v3.1.1)
* CI facilitated by [`Github Actions`](https://github.com/features/actions)
* CD facilitated by [`Github Actions`](https://github.com/features/actions) and [`Python Semantic Release`](https://github.com/relekang/python-semantic-release)
  * Automated CHANGELOG auto-generation
  * Automated [`GitHub releases`](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
  * Automated releases to [`PyPI`](https://pypi.org/)

The template supports Python 3.6, 3.7, 3.8, and 3.9.

## :book: Documentation

The project's documentation can be found [here](https://billsioros.github.io/cookiecutter-pypackage/).

## :heart: Support the project

Feel free to [**Buy me a coffee! ☕**](https://www.buymeacoffee.com/billsioros).

## :sparkles: Contributing

If you would like to contribute to the project, please go through the [Contributing Guidelines](https://billsioros.github.io/cookiecutter-pypackage/latest/CONTRIBUTING/) first.
