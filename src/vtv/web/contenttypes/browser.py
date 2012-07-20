# -*- coding: utf-8 -*-

from five import grok

from vtv.web.contenttypes.program import IProgram

grok.templatedir('templates')


class View(grok.View):
    """ Default view of Programs.
    """
    grok.context(IProgram)
    grok.require('zope2.View')
