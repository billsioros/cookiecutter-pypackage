# Contributing

Hello and thank you for considering contributing to **{{cookiecutter.project_name}}**!

Reading and following these guidelines will help us make the contribution process easy and effective for everyone involved.

## Code of Conduct

By participating and contributing to this project, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Help

In case all you need is an answer to a question, please refrain from opening an issue and instead visit the project's [discussion page]({{ cookiecutter.github_repository }}/discussions/categories/q-a).

## Getting Started

Contributions are made to this repository via Issues and Pull Requests (PRs). A few general guidelines that cover both:

- Search for existing Issues and PRs before creating your own.
- We work hard to make sure issues are handled in a timely manner but, depending on the impact, it could take a while to investigate the root cause. A friendly ping in the comment thread to the submitter or a contributor can help draw attention if your issue is blocking.

### Issues

[Issues]({{ cookiecutter.github_repository }}/issues) should be used to report problems with the library or request a new feature or documentation change. When you create a new Issue, a template will be loaded that will guide you through collecting and providing the required information.

If you find an Issue that addresses the problem you're having, please add your own reproduction information to the existing issue rather than creating a new one. Adding a [reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) can also help in indicating to our maintainers that a particular problem is affecting more than just the reporter.

### Pull Requests

PRs can be a quick way to get your fix or improvement slated for the next release. In general, PRs should:

- Only fix/add the functionality in question **OR** address wide-spread whitespace/style issues, not both.
- Address a single concern in the least number of changed lines as possible.
- Be accompanied by a complete Pull Request template (loaded automatically when a PR is created).
- Add [unit or integration tests]({{ cookiecutter.github_repository }}/tree/master/tests) for added or changed functionality.
- Any code related changes should be accompanied by corresponding changes to the project's documentation.
- If your pull request introduces a new feature, the corresponding `README` [section](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_name}}/latest/#features) must be updated to reflect this.
- Write clear, concise commit message(s) using the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format. [Why?](#writing-your-commit-message)
- This project only accepts pull requests related to open issues. In case there is no relevant open issue, feel free to [create one]({{ cookiecutter.github_repository }}/issues/new/choose).

For changes that address core functionality or would require breaking changes (e.g. a major release), it's best to open an Issue to discuss your proposal first. This is not required but can save time creating and reviewing changes.

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

1. Fork the repository to your own Github account
2. Clone the project to your machine
3. Create a branch locally with a succinct but descriptive name
4. Commit changes to the branch
5. Push changes to your fork
6. [Open a PR in our repository]({{ cookiecutter.github_repository }}/compare) and follow the PR template so that we can efficiently review the changes

## Setting up a local development environment

The following sections assume that you have already locally [cloned the repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Installing Poetry

The **{{cookiecutter.project_name}}** project utilizes the [Poetry](https://python-poetry.org/) Python package manager. [Having installed Poetry](https://python-poetry.org/docs/#installation) in the **global** namespace you may now run `poetry shell` to create a brand new [virtual environment](https://docs.python.org/3/tutorial/venv.html) and `poetry install`, in order to install the project's dependencies (development dependencies as well).

### Installing pre-commit hooks

The project utilizes the [pre-commit](https://pre-commit.com/) framework. Having [created a virtual environment and installed the required dependencies](#installing-poetry), you may run `pre-commit install --install-hooks` to install the [git hook scripts]({{ cookiecutter.github_repository }}/blob/master/.pre-commit-config.yaml).

### Testing via `pytest`

> We are using [pytest](https://github.com/pytest-dev/pytest) to automate testing on multiple environments.

The test suite can be run using `poetry run poe test`.

#### (Optional) Installing pyenv

[pyenv](https://github.com/pyenv/pyenv) is used, in the context of the **{{cookiecutter.project_name}}** project, in order to determine the project's compatibility with various versions of Python. Installing `pyenv` is not strictly required, but it is recommended.

Having installed `pyenv` in the **global** namespace, you may now run the following snippet, in order to install Python 3.7, 3.8 and 3.9, which, at the time of writing this document, are the only Python versions, supported by **{{cookiecutter.project_name}}**.

```bash
pyenv install 3.7.10 3.8.9 3.9.4
pyenv local 3.7.10 3.8.9 3.9.4
```

Feel free to read more about using `pyenv`, in the context of `poetry`, [here](https://blog.jayway.com/2019/12/28/pyenv-poetry-saviours-in-the-python-chaos/).

### Performing development operations via `poethepoet`

> We are using [poethepoet](https://github.com/nat-n/poethepoet), to perform various development oriented tasks.

Formatting, type-checking, running the test suite, as well as a few other operations, can be performed by running `poe <task>`. Please run `poe --help` (or `poetry run poe --help`), to list all available operations.

### Documenting your changes

**{{cookiecutter.project_name}}** utilizes [MkDocs](https://www.mkdocs.org/) to build and deploy its documentation to [GitHub Pages](https://pages.github.com/). The documentation is auto-generated from the [python docstrings](https://www.python.org/dev/peps/pep-0257/#id15) throughout the source code. As a result, any code related change should be accompanied by a corresponding change to the method's / class's docstring.

Having made your changes, please run `poe docs` and make sure that no error is being raised on build time. Afterwards, open `http://localhost:8000/` in your browser of choice and make sure that the documentation renders correctly.

### Writing your commit message

The project's version number and [Changelog]({{ cookiecutter.github_repository }}/blob/master/CHANGELOG.md), depend on a consistent commit history. As a result, your commit message's format is extremely important. Before opening a pull request, please make sure that your commits strictly follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format].

### Creating a pull request

Make sure you review our [Pull Request Guidelines](#pull-requests), before initiating a PR.
