import functools
import json
import subprocess
from urllib.request import urlopen


def subprocess_safe(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except (subprocess.CalledProcessError, FileNotFoundError) as expected_error:
            print(f"Skipping \"{' '.join(args)}\"... ({expected_error})")
        except Exception as unexpected_error:
            print(f"An unexpected error occurred! ('{unexpected_error}')")

    return wrapper


def run(cmd):
    subprocess.run(cmd, check=True)


def http_get(url):
    try:
        with urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.URLError:
        raise ValueError(f"Failed to fetch URL '{url}'")


@subprocess_safe
def install_dependencies():
    run(["poetry", "shell"])
    run(["poetry", "install"])


@subprocess_safe
def initialize_repository():
    run(["git", "init"])
    run(["git", "add", "."])
    run(["git", "commit", "-m", "'feat: initial commit'"])
    run(["git", "remote", "add", "origin", "{{cookiecutter.github_repository}}"])


@subprocess_safe
def install_precommit_hooks():
    run(["pre-commit", "install", "--install-hooks"])


JOBS = [install_dependencies, initialize_repository, install_precommit_hooks]

for job in JOBS:
    job()
