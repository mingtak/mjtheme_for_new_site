# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class ViewMacro(BrowserView):

    template = ViewPageTemplateFile("template/view_macro.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        return self.template()

