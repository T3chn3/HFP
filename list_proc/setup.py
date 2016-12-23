#contains metadata for your distutils

from distutils.core import setup

setup( #setup used to assign metadata fields
name = 'list_proc'
version = '1.0.0'
py_modules = ['list_proc']
author = 'jbihms'
author_email = 'myemail@yahoo.com'
)

#python3 setup.py sdist to build distro

#install distro"sudo python3 setup.py install"

