""" Test the python-lib Cookiecutter template.

A template project is created in a temporary directory, the library is
installed into a self-contained virtualenv environment, and the library test 
suite is run.

"""
from contextlib import contextmanager
from os import chdir
from os import getcwd
from shlex import split
from shutil import rmtree
from subprocess import check_call
from tempfile import mkdtemp


def main():
    """ Execute the test.
    
    """
    @contextmanager
    def tmpdir():
        """ Enter a self-deleting temporary directory. """
        cwd = getcwd()
        tmp = mkdtemp()
        try:
            chdir(tmp)
            yield tmp
        finally:
            rmtree(tmp)
            chdir(cwd)
        return

    template = getcwd()
    with tmpdir():
        cookiecutter = "cookiecutter {:s} --no-input".format(template)
        check_call(split(cookiecutter))
        chdir("pylib")
        virtualenv = "virtualenv venv"
        check_call(split(virtualenv))
        install = "venv/bin/pip install ."
        for name in "requirements.txt", "requirements-test.txt":
            install = " ".join((install, "--requirement={:s}".format(name)))
        check_call(split(install))
        pytest = "venv/bin/python -m pytest --verbose test"
        check_call(split(pytest))
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())