import pathlib
import shutil


def generate_license():
    try:
        cwd = pathlib.Path.cwd()

        shutil.move(str(cwd / "licenses" / "{{cookiecutter.license}}.txt"), str(cwd / "LICENSE"))
        shutil.rmtree(str(cwd / "licenses"))
    except Exception as exception:
        msg = f"License generation failed ({exception})"
        raise RuntimeError(
            msg,
        )


generate_license()
