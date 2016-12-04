# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from mingjing.theme.testing import MINGJING_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingjing.theme is properly installed."""

    layer = MINGJING_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingjing.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingjing.theme'))

    def test_browserlayer(self):
        """Test that IMingjingThemeLayer is registered."""
        from mingjing.theme.interfaces import (
            IMingjingThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IMingjingThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGJING_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['mingjing.theme'])

    def test_product_uninstalled(self):
        """Test if mingjing.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingjing.theme'))

    def test_browserlayer_removed(self):
        """Test that IMingjingThemeLayer is removed."""
        from mingjing.theme.interfaces import IMingjingThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMingjingThemeLayer, utils.registered_layers())
