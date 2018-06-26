import unittest
from unittest import mock
from api.douban import BookInfoByIsbn
import requests
import enum
from api.test import mocking_douban_api as moc


class TestDoubanBook(unittest.TestCase):

    @mock.patch('api.douban.requests.get', side_effect=moc.get)
    def testDoubanBook_normal(self, mock_get):
        a = BookInfoByIsbn("9787301160978", apiBaseUrl=moc.url.normal)
        self.assertTrue(isinstance(a, dict))
        self.assertNotEquals(len(a), 0)

    @mock.patch('api.douban.requests.get', side_effect=moc.get)
    def testDoubanBook_wrongJson(self, mock_get):
        a = BookInfoByIsbn("9787301160978", apiBaseUrl=moc.url.Wrong_Json)
        self.assertEquals(len(a), 0)

    @mock.patch('api.douban.requests.get', side_effect=moc.get)
    def testDoubanBook_exceedLimations(self, mock_get):
        a = BookInfoByIsbn(
            "9787301160978", apiBaseUrl=moc.url.Exceed_limtation)
        self.assertEquals(len(a), 0)
