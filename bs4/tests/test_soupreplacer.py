import unittest
from bs4 import BeautifulSoup
from bs4.SoupReplacer import SoupReplacer

class TestSoupReplacer(unittest.TestCase):
    def test_simple_replace(self):
        html = "<b>Hello</b>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertEqual(str(soup), "<blockquote>Hello</blockquote>")

    def test_multiple_replace(self):
        xml = "<html><body><b>Hi</b><b>There</b></body></html>"
        replacer = SoupReplacer("b", "i")
        soup = BeautifulSoup(xml, "lxml", replacer=replacer)
        self.assertEqual(str(soup), "<html><body><i>Hi</i><i>There</i></body></html>")