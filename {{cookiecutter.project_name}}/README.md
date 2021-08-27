<h1 align="center">🐍 {{ cookiecutter.project_name.replace('-', ' ').title() }}</h1>

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
  <a href="https://opensource.org/licenses/MIT">
    <img
      src="https://img.shields.io/pypi/l/{{cookiecutter.project_name}}"
      alt="PyPI - License"
    />
  </a>
  <a href="https://gitpod.io/from-referrer/">
    <img
      src="https://img.shields.io/badge/Open%20on-Gitpod-blue?logo=gitpod&style=flat"
      alt="Open on Gitpod"
    />
  </a>
  <a href="https://github.com/billsioros/cookiecutter-pypackage">
    <img
      src="https://img.shields.io/badge/cookiecutter-template-D4AA00.svg?style=flat&logo=cookiecutter"
      alt="Cookiecutter Template">
  </a>

</p>

## Example Usage

```python
>>> from {{cookiecutter.package_name}} import {{cookiecutter.package_name}}
```

## Features

- TODO

## Documentation

The project's documentation can be found [here](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/).

## Installation

```bash
pip install {{cookiecutter.project_name}}
```

## Supporting the project

Feel free to [**Buy me a coffee! ☕**](https://www.buymeacoffee.com/{{cookiecutter.github_user}}).

## Contributing

If you would like to contribute to the project, please go through the [Contributing Guidelines](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/latest/CONTRIBUTING/) first.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [billsioros/cookiecutter-pypackage](https://github.com/billsioros/cookiecutter-pypackage) cookiecutter template.
