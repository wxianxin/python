# python packaging

#. from . import xxx

#. setup.py
#. MANIFEST.in  # To include static files
#. main functions included in __init__.py
#. Add custom steps in the process of installation:

################################################################################
# setup.py
```
from setuptools import setup, find_packages
from setuptools.command.install import install
Class PostInstallCommand(install):
    def run(self):

        xxxxxx
        xxxxxx

        install.run(self)

setup(...,
      cmdclass={'install': PostInstallCommand,},
      )
```
################################################################################
# __init__.py
```
ROOT_PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
os.environ['ROOT_PATH'] = ROOT_PATH
```
################################################################################
################################################################################
################################################################################


#. pip install -e . # This will create a link in regular package storage path. This link points the original files. If you as the developer change some code, you (almost) will not reinstall the package.
