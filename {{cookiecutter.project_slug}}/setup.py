""" Setup script for the {{ cookiecutter.lib_name }} library.

"""
from setuptools import Command
from setuptools import find_packages
from setuptools import setup
from distutils import log
from os.path import join
from subprocess import check_call
from subprocess import CalledProcessError


_CONFIG = {
    "name": "{{ cookiecutter.lib_name }}",
    "author": "{{ cookiecutter.author_name   }}",
    "author_email": "{{ cookiecutter.author_email }}",
    "url": "",
    "package_dir": {"": "src"},
    "packages": find_packages("src")}


def _version():
    """ Get the local package version.

    """
    path = join("src", _CONFIG["name"], "__version__.py")
    namespace = {}
    with open(path) as stream:
        exec(stream.read(), namespace)
    return namespace["__version__"]


class _CustomCommand(Command):
    """ Abstract base class for a custom setup command.

    """
    # Each user option is a tuple consisting of the option's long name (ending
    # with "=" if it accepts an argument), its single-character alias, and a
    # description.
    description = ""
    user_options = []  # this must be a list

    def initialize_options(self):
        """ Set the default values for all user options.

        """
        return

    def finalize_options(self):
        """ Set final values for all user options.

        This is run after all other option assignments have been completed
        (e.g. command-line options, other commands, etc.)

        """
        return

    def run(self):
        """ Execute the command.

        Raise SystemExit to indicate failure.

        """
        raise NotImplementedError


class UpdateCommand(_CustomCommand):
    """ Custom setup command to pull from a remote branch.

    """
    description = "update from a remote branch"
    user_options = [
        ("remote=", "r", "remote name [default: tracking remote]"),
        ("branch=", "b", "branch name [default: tracking branch]")]

    def initialize_options(self):
        """ Set the default values for all user options.

        """
        self.remote = ""  # default to tracking remote
        self.branch = ""  # default to tracking branch
        return

    def run(self):
        """ Execute the command.

        """
        args = {"remote": self.remote, "branch": self.branch}
        cmdl = "git pull --ff-only {remote:s} {branch:s}".format(**args)
        try:
            check_call(cmdl.split())
        except CalledProcessError:
            raise SystemExit(1)
        log.info("package version is now {:s}".format(version()))
        return


def main():
    """ Execute the setup commands.

    """
    _CONFIG["version"] = _version()
    _CONFIG["cmdclass"] = {"update": UpdateCommand}
    setup(**_CONFIG)
    return 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
