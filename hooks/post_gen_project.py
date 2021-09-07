import datetime
import functools
import json
import pathlib
import subprocess
import sys
from urllib.error import URLError
from urllib.request import urlopen


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


def http_get(url):
    try:
        with urlopen(url) as response:
            return json.loads(response.read())
    except URLError:
        raise ValueError(f'Failed to fetch URL \'{url}\'')


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
        url = 'https://api.github.com/licenses'

        chosen_license = None
        for available_license in http_get(url):
            if available_license['key'] == '{{cookiecutter.license}}':
                chosen_license = available_license

        chosen_license = http_get(chosen_license['url'])

        license_body = chosen_license['body']

        year = datetime.datetime.utcnow().strftime('%Y')

        license_body = license_body.replace('[year]', f'{year}-{year}')
        license_body = license_body.replace(
            '[fullname]', '{{cookiecutter.author}} ({{cookiecutter.github_user}})'
        )

        with (pathlib.Path.cwd() / 'LICENSE') as license_file:
            license_file.write_text(license_body)
    except Exception as exception:
        raise ValueError(exception)


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
