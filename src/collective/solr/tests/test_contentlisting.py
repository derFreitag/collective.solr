from unittest import TestCase

from plone.app.contentlisting.interfaces import IContentListingObject
from plone.uuid.interfaces import IUUID
from zope.interface.verify import verifyClass

from collective.solr.contentlisting import FlareContentListingObject
from collective.solr.flare import PloneFlare
from collective.solr.testing import LEGACY_COLLECTIVE_SOLR_INTEGRATION_TESTING


class ContentListingTests(TestCase):

    layer = LEGACY_COLLECTIVE_SOLR_INTEGRATION_TESTING

    def setUp(self):
        self.flare = FlareContentListingObject(PloneFlare({
            'getId': 'foobar',
            'path_string': '/plone/news',
            'UID': 'test-uid',
            'getObjSize': 42,
            'review_state': 'published',
            'listCreators': ['foo', 'bar'],
            'Creator': 'Flare Creator',
            'Title': 'Flare Title',
            'Description': 'Flare Description',
            'Subject': 'Flare Subject',
            'Date': 'Flare Date',
            'expires': '1.1.2099',
            'created': '31.12.1969',
            'modified': '27.07.2016',
            'Language': 'de',
            'portal_type': 'NewsItem',
            'Type': 'Flare NewsItem',
            }))

    def testInterfaceComplete(self):
        self.assertTrue(
            verifyClass(IContentListingObject, FlareContentListingObject))

    def test_getId(self):
        self.assertEqual(self.flare.getId(), 'foobar')

    def test_getObject(self):
        self.assertEqual(self.flare.getObject(), self.layer['portal']['news'])

    def test_getDataOrigin(self):
        self.assertEqual(self.flare.getObject(), self.layer['portal']['news'])

    def test_getPath(self):
        self.assertEqual(self.flare.getPath(), '/plone/news')

    def test_getURL(self):
        self.assertEqual(self.flare.getURL(False), '/plone/news')
        self.assertEqual(self.flare.getURL(True), '/plone/news')

    def test_uuid_key(self):
        self.assertEqual(self.flare.uuid(), 'test-uid')

    def test_uuid_object(self):
        del self.flare.flare['UID']
        self.assertEqual(self.flare.uuid(),
                         IUUID(self.layer['portal']['news']))

    def test_getSize(self):
        self.assertEqual(self.flare.getSize(), 42)

    def test_review_state(self):
        self.assertEqual(self.flare.review_state(), 'published')

    def test_listCreators(self):
        self.assertEqual(self.flare.listCreators(), ['foo', 'bar'])

    def test_Creator(self):
        self.assertEqual(self.flare.Creator(), 'Flare Creator')

    def test_Subject(self):
        self.assertEqual(self.flare.Subject(), 'Flare Subject')

    def test_Publisher(self):
        self.assertRaises(NotImplementedError, self.flare.Publisher)

    def test_listContributors(self):
        self.assertRaises(NotImplementedError, self.flare.listContributors)

    def test_Contributors(self):
        self.assertRaises(NotImplementedError, self.flare.Contributors)

    def test_Date(self):
        self.assertEqual(self.flare.Date(), 'Flare Date')

    def test_CreationDate(self):
        self.assertEqual(self.flare.CreationDate(), '31.12.1969')

    def test_EffectiveDate(self):
        self.assertEqual(self.flare.EffectiveDate(),
                         self.layer['portal']['news'].EffectiveDate())

    def test_ExpirationDate(self):
        self.assertEqual(self.flare.ExpirationDate(), '1.1.2099')

    def test_ModificationDate(self):
        self.assertEqual(self.flare.ModificationDate(), '27.07.2016')

    def test_Format(self):
        self.assertRaises(NotImplementedError, self.flare.Format)

    def test_Identifier(self):
        self.assertEqual(self.flare.Identifier(), '/plone/news')

    def Language(self):
        self.assertEqual(self.Language, 'de')

    def test_Rights(self):
        self.assertRaises(NotImplementedError, self.flare.Rights)

    def test_Title(self):
        self.assertEqual(self.flare.Title(), 'Flare Title')

    def test_Description(self):
        self.assertEqual(self.flare.Description(), 'Flare Description')

    def test_Type(self):
        self.assertEqual(self.flare.Type(), 'Flare NewsItem')

    def test_ContentTypeClass(self):
        self.assertEqual(self.flare.ContentTypeClass(),
                         'contenttype-newsitem')

    def test_PortalType(self):
        self.assertEqual(self.flare.PortalType(), 'NewsItem')

    def test_Author(self):
        self.assertEqual(self.flare.Author(),
                         {'username': 'Flare Creator',
                          'description': '',
                          'language': '',
                          'home_page': '/HOMEPAGEURL',
                          'location': '',
                          'fullname': 'Flare Creator'})

    def test_CroppedDescription(self):
        self.assertEqual(self.flare.CroppedDescription(), 'Flare Description')
