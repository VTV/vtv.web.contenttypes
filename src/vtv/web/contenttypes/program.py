# -*- coding: utf-8 -*-

from zope import schema

from plone.directives import dexterity, form
from plone.namedfile.field import NamedBlobImage

from vtv.web.contenttypes import _


class IProgram(form.Schema):
    """ A TV show.
    """

    image = NamedBlobImage(
        title=_(u"Image"),
        description=_(u'help_image',
                      default=u""),
        required=True,
        )

    thumbnail = NamedBlobImage(
        title=_(u"Thumbnail"),
        description=_(u'help_thumbnail',
                      default=u""),
        required=True,
        )

    api_url = schema.TextLine(
        title=_(u"API URL"),
        description=_(u'help_api_url',
                      default=u"URL to access the list of recent shows."),
        required=True,
        )


class Program(dexterity.Item):
    pass
