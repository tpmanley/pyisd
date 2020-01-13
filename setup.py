# NOTE: See the README file for a list of dependencies to install.

import sys

try:
    from setuptools import setup, Extension
except ImportError:
    print("No setuptools found, attempting to use distutils instead.")
    from distutils.core import setup, Extension

# TODO: Ideally we would detect missing python-dev and libgcrypt-dev to give better errors.

zigbee_crypt = Extension('zigbee_crypt',
                         sources = ['zigbee_crypt/zigbee_crypt.c'],
                         libraries = ['gcrypt'],
                         include_dirs = ['/usr/local/include', '/usr/include', '/sw/include/', 'zigbee_crypt'],
                         library_dirs = ['/usr/local/lib', '/usr/lib','/sw/var/lib/']
                         )

setup(name        = 'pyisd',
      version     = '1.0',
      description = 'Tools for working with SiLabs Network Analyzer files',
      author = 'Tom Manley',
      author_email = 'tom.manley@gmail.com',
      scripts = ['scripts/pyisd.py'],
      ext_modules = [zigbee_crypt],
      )

