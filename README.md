python_shebang Description
==========================
This package provides a command that can be run from the shebang line of a
script that will find an appropriate python interpreter to run it.

This is similar to /usr/bin/env but also allows specifying the version of python
and python modules that are required.


Installation
============
Since the shebang parsing does not use expand the path, this script needs needs
to be installed in a fixed well known location (recommend /usr/bin)


Dependencies
============
python_shebang is written to be able to run under any python version 2.6 or
higher using only modules in the python standard library.


Examples
========
Here is a shebang line that will run the script with a python2.6 interpreter
that has both the foo and bar modules:

```#!/usr/bin/python_shebang version:2.6 module:foo module:bar```

This shebang line will run the script with a python 3 interpreter that has
the paramiko module:

```#!/usr/bin/python_shebang version:3 module:paramiko```

