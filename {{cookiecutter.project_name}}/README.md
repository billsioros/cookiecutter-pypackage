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
  <a href="https://app.fossa.com/projects/git%2Bgithub.com%2F{{cookiecutter.github_user}}%2F{{cookiecutter.project_name}}?ref=badge_shield">
    <img
      src="https://app.fossa.com/api/projects/git%2Bgithub.com%2F{{cookiecutter.github_user}}%2F{{cookiecutter.project_name}}.svg?type=shield"
      alt="FOSSA Status"
    />
  </a>
</p>

## :bulb: Example

```python
>>> from {{cookiecutter.package_name}} import {{cookiecutter.package_name}}
```

## :rocket: Features

- TODO

## :book: Documentation

The project's documentation can be found [here](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/).

## :cd: Installation

```bash
pip install {{cookiecutter.project_name}}
```

## :heart: Support the project

Feel free to [**Buy me a coffee! ???**](https://www.buymeacoffee.com/{{cookiecutter.github_user}}).

## :sparkles: Contributing

If you would like to contribute to the project, please go through the [Contributing Guidelines](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/latest/CONTRIBUTING/) first.

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## :bookmark_tabs: Citation

```bibtex
{% raw %}@misc{{% endraw %}{{ cookiecutter.project_name }},
  author = {% raw %}{{% endraw %}{{ cookiecutter.author }}{% raw %}}{% endraw %},
  title = {% raw %}{{% endraw %}{{ cookiecutter.project_description }}{% raw %}}{% endraw %},
  year = {% raw %}{{% endraw %}{% now 'utc', '%Y' %}{% raw %}}{% endraw %},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}{% raw %}}}{% endraw %}
}
```

## :label: Credits

This project was generated with [`billsioros/cookiecutter-pypackage`](https://github.com/billsioros/cookiecutter-pypackage) cookiecutter template.
