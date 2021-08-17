![{{cookiecutter.project_name}}](https://raw.githubusercontent.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/master/docs/img/logo.png)

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
  <a href="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/ci.yml">
    <img
      src="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/ci.yml/badge.svg"
      alt="CI"
    />
  </a>
  <a href="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/cd.yml">
    <img
      src="https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions/workflows/cd.yml/badge.svg"
      alt="CI"
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
      src="https://img.shields.io/badge/Gitpod-Open-blue?logo=gitpod"
      alt="Open on Gitpod"
    />
  </a>
</p>

## Example Usage

```python
>>> from {{cookiecutter.project_name}} import {{cookiecutter.project_name}}, Track
>>> with {{cookiecutter.project_name}}(SPOTIFY_ID, SPOTIFY_SECRET):
>>>     result = next(Track.search("SAINt JHN 5 Thousand Singles", limit=1))
>>> result
<Track "SAINt JHN - 5 Thousand Singles">
>>> result.url
'https://open.spotify.com/track/0fFWxRZGKR7HDW2xBMOZgW'
>>> result.download("SAINt JHN - 5 Thousand Singles.mp3")
PosixPath('SAINt JHN - 5 Thousand Singles.mp3')
```

Feel free to check the [examples](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/tree/master/examples) folder for more use cases!

## Features

- Searching for
  - Tracks
  - Playlists
  - Albums
- Downloading
  - Tracks
  - Playlists
  - Albums

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
