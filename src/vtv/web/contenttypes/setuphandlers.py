# -*- coding:utf-8 -*-
from five import grok

from Products.CMFPlone.interfaces import INonInstallable


class HiddenProfiles(grok.GlobalUtility):

    grok.implements(INonInstallable)
    grok.provides(INonInstallable)
    grok.name('vtv.web.contenttypes.program')

    def getNonInstallableProfiles(self):
        profiles = ['vtv.web.contenttypes.program:uninstall', ]
        return profiles
