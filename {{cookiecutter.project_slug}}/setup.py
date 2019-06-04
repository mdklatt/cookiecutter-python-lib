""" Setup script for the {{ cookiecutter.lib_name }} library.

"""
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


_config = {
    "name": "{{ cookiecutter.lib_name }}",
    "url": "{{ cookiecutter.project_url }}",
    "author": "{{ cookiecutter.author_name }}",
    "author_email": "{{ cookiecutter.author_email }}",
    "package_dir": {"": "src"},
    "packages": find_packages("src")
}


def main() -> int:
    """ Execute the setup commands.

    """
    def version():
        """ Get the local package version. """
        namespace = {}
        path = Path("src", _config["name"], "__version__.py")
        exec(path.read_text(), namespace)
        return namespace["__version__"]

    _config.update({
        "version": version(),
    })
    setup(**_config)
    return 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
