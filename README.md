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

> An up-to-date instance of the cookicutter template can be found [here](https://github.com/billsioros/cookiecutter-pypackage-instance)

## :rocket: Features

* Dependency tracking using [`Poetry`](https://python-poetry.org/)
* Test automation with [`Tox`](https://github.com/tox-dev/tox)
* Multi-version documentation extracted from source code provided by [`MkDocs`](https://github.com/mkdocs/mkdocs/), [`mkdocstrings`](https://github.com/mkdocstrings/mkdocstrings/), [`Material for MkDocs`](https://github.com/squidfunk/mkdocs-material) and [`mike`](https://github.com/jimporter/mike) and hosted on [`GitHub Pages`](https://pages.github.com/)
* Automated dependency and security updates with [`Renovate`](https://renovate.whitesourcesoftware.com/) and [`Dependabot`](https://dependabot.com/)
* Formatting provided by [`black`](https://github.com/psf/black) and [`isort`](https://github.com/PyCQA/isort)
* Testing setup with [`pytest`](https://github.com/pytest-dev/pytest)
* Coverage reports with [`Coverage.py`](https://github.com/nedbat/coveragepy) and [`Codecov`](https://docs.codecov.com/docs)
* Static type checking by [`mypy`](https://github.com/python/mypy)
* Security checks with [`CodeQL`](https://github.com/github/codeql-action)
* Linting provided by [`Flakehell`](https://github.com/flakehell/flakehell) and [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide)
* Git hooks managed by [`pre-commit`](https://pre-commit.com/).
* Development tasks (lint, format, test, etc) provided by [`Poe The Poet`](https://github.com/nat-n/poethepoet)
* CI facilitated by [`Github Actions`](https://github.com/features/actions)
* Automated CHANGELOG generation, [`GitHub releases`](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) and [`PyPI releases`](https://pypi.org/) facilitated by [`Python Semantic Release`](https://github.com/relekang/python-semantic-release)
* Preview documentation changes introduced via a PR on [`surge`](https://surge.sh/)
* Automatically fix typos in your source code and documentation via [`Misspell Fixer`](https://github.com/sobolevn/misspell-fixer-action)
* Beautiful [`YAML issue templates`](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository#creating-issue-forms)
* Informative [`PR template`](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) and [`Security Policy`](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
* Inform new contributors about the project's guidelines using [`First Interaction`](https://github.com/actions/first-interaction)
* Add informative comments on issues & PRs based on assigned labels using [`Label Commenter`](https://github.com/peaceiris/actions-label-commenter)
* Manage project labels with [`GitHub Labeler`](crazy-max/ghaction-github-labeler@v3.1.1)
* License scanning provided by [`FOSSA`](https://fossa.com/)
* Automatically update the copyright year span using [`Update License Year`](https://github.com/FantasticFiasco/action-update-license-year)
* Pre-configured funding on [`Buy Me a Coffee`](https://www.buymeacoffee.com/)
* Automatically close stale issues/PRs using [`Stale Bot`](https://github.com/apps/stale)
* Ready-to-use configuration to recognize the effors of [`All Contributors`](https://allcontributors.org/)
* Ready-to-use configuration to automate code reviews using [`deepsource`](https://deepsource.io/)
* Ready-to-use `.editorconfig` and `.gitignore`
* Be always ready to code using automated dev environments hosted on [`Gitpod`](https://www.gitpod.io/)

> The template supports Python 3.7 or higher.

## :book: Documentation

The project's documentation can be found [here](https://billsioros.github.io/cookiecutter-pypackage/).

## :heart: Support the project

Feel free to [**Buy me a coffee! ☕**](https://www.buymeacoffee.com/billsioros).

## :sparkles: Contributing

If you would like to contribute to the project, please go through the [Contributing Guidelines](https://billsioros.github.io/cookiecutter-pypackage/latest/CONTRIBUTING/) first.
