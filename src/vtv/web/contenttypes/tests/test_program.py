# -*- coding: utf-8 -*-

import unittest2 as unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID

from vtv.web.contenttypes.program import IProgram
from vtv.web.contenttypes.testing import INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
        self.folder.invokeFactory('vtv.web.program', 'p1')
        self.p1 = self.folder['p1']

    def test_adding(self):
        self.assertTrue(IProgram.providedBy(self.p1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='vtv.web.program')
        self.assertNotEqual(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='vtv.web.program')
        schema = fti.lookupSchema()
        self.assertEqual(IProgram, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='vtv.web.program')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IProgram.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.p1))
        self.assertTrue(IAttributeUUID.providedBy(self.p1))

    def test_default_workflow(self):
        workflow_tool = getattr(self.portal, 'portal_workflow')
        chain = workflow_tool.getChainForPortalType(self.p1.portal_type)
        self.assertEqual(len(chain), 1)
        self.assertEqual(chain[0], 'one_state_workflow')

    def test_program_selectable_as_folder_default_view(self):
        self.folder.setDefaultPage('p1')
        self.assertEqual(self.folder.default_page, 'p1')
