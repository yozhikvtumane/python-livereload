"""
    livereload
    ~~~~~~~~~~

    A python version of livereload.

    :copyright: (c) 2013 - 2015 by Hsiaoming Yang
    :license: BSD, see LICENSE for more details.
"""

__version__ = '2.4.0'
__author__ = 'Hsiaoming Yang <me@lepture.com>'
__homepage__ = 'https://github.com/lepture/python-livereload'

from .server import Server, shell

__all__ = ('Server', 'shell')
