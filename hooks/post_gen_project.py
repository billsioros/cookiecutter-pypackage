import pathlib
import shutil


def generate_license():
    try:
        cwd = pathlib.Path.cwd()

        shutil.move(str(cwd / 'licenses' / '{{cookiecutter.license}}.txt'), str(cwd / 'LICENSE'))
        shutil.rmtree(str(cwd / 'licenses'))
    except Exception as exception:
        raise RuntimeError(
            'License generation failed ({0})'.format(
                exception,
            )
        )


generate_license()
