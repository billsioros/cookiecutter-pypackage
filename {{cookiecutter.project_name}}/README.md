<h1 align="center">{{ cookiecutter.project_name.replace('-', ' ').title() }}</h1>

<p align="center"><em>{{ cookiecutter.project_description }}</em></p>

<p align="center">
  <a href="https://www.python.org/">
    <img
      src="https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}"
      alt="PyPI - Python Version"
    />
  </a>
  <a href="https://pypi.org/project/{{cookiecutter.project_name}}/">
    <img
      src="https://img.shields.io/pypi/v/{{cookiecutter.project_name}}"
      alt="PyPI"
    />
  </a>
  <a href="{{ cookiecutter.github_repository }}/actions/workflows/ci.yml">
    <img
      src="{{ cookiecutter.github_repository }}/actions/workflows/ci.yml/badge.svg"
      alt="CI"
    />
  </a>
  <a href="{{ cookiecutter.github_repository }}/actions/workflows/cd.yml">
    <img
      src="{{ cookiecutter.github_repository }}/actions/workflows/cd.yml/badge.svg"
      alt="CD"
    />
  </a>
  <a href="https://results.pre-commit.ci/latest/github/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/master">
    <img
      src="https://results.pre-commit.ci/badge/github/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/master.svg"
      alt="pre-commit.ci status"
    />
  </a>
  <a href="https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}">
    <img
      src="https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg?token=coLOL0j6Ap"
      alt="Test Coverage"/>
  </a>
  <a href="https://opensource.org/licenses/{{cookiecutter.license.upper()}}">
    <img
      src="https://img.shields.io/pypi/l/{{cookiecutter.project_name}}"
      alt="PyPI - License"
    />
  </a>
  <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url={{ cookiecutter.github_repository }}">
    <img
      src="https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode"
      alt="Open in GitHub Codespaces"
    />
  </a>
  <a href="https://github.com/billsioros/cookiecutter-pypackage">
    <img
      src="https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat&logo=cookiecutter"
      alt="Cookiecutter Template">
  </a>
  <a href="https://app.renovatebot.com/dashboard#github/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}">
    <img
      src="https://img.shields.io/badge/renovate-enabled-brightgreen.svg?style=flat&logo=renovatebot"
      alt="Renovate - Enabled">
  </a>
  <a href="https://www.buymeacoffee.com/{{cookiecutter.github_user}}">
    <img
      src="https://img.shields.io/badge/Buy%20me%20a-coffee-FFDD00.svg?style=flat&logo=buymeacoffee"
      alt="Buy me a coffee">
  </a>
  <a href="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/dependency_review.yml">
    <img
      src="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/dependency_review.yml/badge.svg"
      alt="Dependency Review"
    />
  </a>
</p>

## :cd: Installation

```bash
pip install {{cookiecutter.project_name}}
```

In order to locally set up the project please follow the instructions below:

```shell
# Set up the GitHub repository
git init
git config --local user.name {{cookiecutter.author}}
git config --local user.email {{cookiecutter.email}}
git add .
git commit -m "feat: initial commit"
git remote add origin {{cookiecutter.github_repository}}

# Create a virtual environment using poetry and install the required dependencies
poetry shell
poetry install

# Install pre-commit hooks
pre-commit install --install-hooks
pre-commit autoupdate
```

## :book: Documentation

The project's documentation can be found [here](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/).

## :heart: Support the project

Feel free to [**Buy me a coffee! ☕**](https://www.buymeacoffee.com/{{cookiecutter.github_user}}).

## :sparkles: Contributing

If you would like to contribute to the project, please go through the [Contributing Guidelines](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/latest/CONTRIBUTING/) first.

## :label: Credits

This project was generated with [`billsioros/cookiecutter-pypackage`](https://github.com/billsioros/cookiecutter-pypackage) cookiecutter template.
