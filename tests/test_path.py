# -*- coding: utf-8 -*-
import logging

from testtools import TestCase

from auxlib import logz
from auxlib.path import open_package_file, PackageFile

log = logging.getLogger(__name__)


class PathTests(TestCase):

    @classmethod
    def setUpClass(cls):
        logz.set_root_level(logging.INFO)
        logz.attach_stderr(logging.DEBUG)
        assert not logz.attach_stderr()

    @classmethod
    def tearDownClass(self):
        logz.detach_stderr()
        assert not logz.detach_stderr()

    def test_find_real_file(self):
        fh = open_package_file('requirements/test.txt', None)
        lines = fh.readlines()
        fh.close()
        assert any(line.startswith('testtools') for line in lines)

    def test_find_python_file_in_package(self):
        with PackageFile('path.py', 'auxlib') as fh:
            lines = fh.readlines()
            assert any(line.startswith(b'class PackageFile(object):') for line in lines)

    # TODO: Write tests for "look for file in site-packages"
    # def test_find_python_file_in_site_packages(self):
    #     # with PackageFile('__init__.py', 'testtools') as fh:  # package resource file
    #     # with PackageFile('LICENSE', 'py.test') as fh:  # real file
    #     with PackageFile('PKG-INFO', 'pytest') as fh:
    #         lines = fh.readlines()
    #         assert any(line.startswith('__version__') for line in lines)
    #     assert False
