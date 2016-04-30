# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys
import copy

from tank_test.tank_test_base import *

from tank import PathManager

class TestBasePaths(TankTestBase):

    def setUp(self):
        super(TestBasePaths, self).setUp()

    def test_get_cache_root(self):
        """
        Tests get_cache_root
        """
        p = PathManager.get_global_root(PathManager.CACHE)
        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun", "Caches"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Caches/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun/caches"))


        p = PathManager.get_global_root(PathManager.CACHE, PathManager.CORE_V17)

        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Caches/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun"))

    def test_get_data_root(self):
        """
        Tests get_cache_root
        """

        p = PathManager.get_global_root(PathManager.PERSISTENT)

        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun", "Data"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Application Support/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun/data"))


        p = PathManager.get_global_root(PathManager.PERSISTENT, PathManager.CORE_V17)

        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Application Support/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun"))

    def test_get_log_root(self):
        """
        Tests get_cache_root
        """

        p = PathManager.get_global_root(PathManager.LOGGING)

        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun", "Log"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Logs/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun/log"))


        p = PathManager.get_global_root(PathManager.LOGGING, PathManager.CORE_V17)

        if sys.platform == "win32":
            self.assertEqual(p, os.path.join(os.environ["APPDATA"], "Shotgun"))
        if sys.platform == "darwin":
            self.assertEqual(p, os.path.expanduser("~/Library/Logs/Shotgun"))
        if sys.platform == "linux2":
            self.assertEqual(p, os.path.expanduser("~/.shotgun"))


    def test_get_site_cache_root(self):
        """
        Tests site cache root
        """

        for mode in [PathManager.CACHE, PathManager.PERSISTENT, PathManager.LOGGING]:


            site_path = PathManager.get_site_root("http://sg-internal", mode)
            global_path = PathManager.get_global_root(mode)
            self.assertEqual(os.path.dirname(site_path), global_path)
            self.assertEqual(os.path.basename(site_path), "sg-internal")

            site_path = PathManager.get_site_root("http://foo.int", mode)
            self.assertEqual(os.path.basename(site_path), "foo.int")

            site_path = PathManager.get_site_root("https://my-site.shotgunstudio.com", mode)
            self.assertEqual(os.path.basename(site_path), "my-site")


            legacy_site_path = PathManager.get_site_root("http://sg-internal", mode, PathManager.CORE_V17)
            legacy_global_path = PathManager.get_global_root(mode, PathManager.CORE_V17)

            self.assertEqual(os.path.dirname(legacy_site_path), legacy_global_path)
            self.assertEqual(os.path.basename(legacy_site_path), "sg-internal")

            legacy_site_path = PathManager.get_site_root("http://foo.int", mode, PathManager.CORE_V17)
            self.assertEqual(os.path.basename(legacy_site_path), "foo.int")

            legacy_site_path = PathManager.get_site_root("https://my-site.shotgunstudio.com", mode, PathManager.CORE_V17)
            self.assertEqual(os.path.basename(legacy_site_path), "my-site.shotgunstudio.com")




    # @ todo - add tests for project/ pipleine config level methods