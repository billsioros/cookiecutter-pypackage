import functools
import pathlib
import shutil
import subprocess
import sys


def transactional(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        error_message = None

        try:
            for cmd in method(*args, **kwargs):
                subprocess.run(cmd, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as expected_error:
            error_message = 'Skipping \'%s\'... (%r)'.format(' '.join(args), expected_error)
        except Exception as unexpected_error:
            error_message = 'An unexpected error occurred! (%r)'.format(
                unexpected_error,
            )
        finally:
            if error_message is not None:
                raise ValueError(error_message)

    return wrapper


@transactional
def install_dependencies():
    yield 'poetry', 'shell'
    yield 'poetry', 'install'


@transactional
def initialize_repository():
    yield 'git', 'init'
    yield 'git', 'add', '.'
    yield 'git', 'commit', '-m', '\'feat: initial commit\''
    yield 'git', 'remote', 'add', 'origin', '{{cookiecutter.github_repository}}'


@transactional
def install_precommit_hooks():
    yield 'pre-commit', 'install', '--install-hooks'


def generate_license():
    try:
        cwd = pathlib.Path.cwd()

        shutil.move(str(cwd / 'licenses' / '{{cookiecutter.license}}.txt'), str(cwd / "LICENSE"))
        shutil.rmtree(str(cwd / 'licenses'))
    except Exception as exception:
        raise ValueError(
            "License generation failed ({0})".format(
                exception,
            )
        )


generate_license()

if '{{cookiecutter.skip_setup}}' == 'False':
    for task in [
        install_dependencies,
        initialize_repository,
        install_precommit_hooks,
    ]:
        try:
            task()
        except ValueError as value_error:
            print(value_error)  # noqa: WPS421
            sys.exit(1)
