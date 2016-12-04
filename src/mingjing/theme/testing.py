# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingjing.theme


class MingjingThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mingjing.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingjing.theme:default')


MINGJING_THEME_FIXTURE = MingjingThemeLayer()


MINGJING_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGJING_THEME_FIXTURE,),
    name='MingjingThemeLayer:IntegrationTesting'
)


MINGJING_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGJING_THEME_FIXTURE,),
    name='MingjingThemeLayer:FunctionalTesting'
)


MINGJING_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGJING_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MingjingThemeLayer:AcceptanceTesting'
)
