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

    def test_name_xformer(self):
        html = "<b>Hello</b><i>World</i>"
        replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIn("<blockquote>", str(soup))

    def test_attrs_xformer(self):
        html = '<p class="red" id="x">Hi</p>'
        replacer = SoupReplacer(attrs_xformer=lambda tag: {"style": "color:blue;"} if tag.name == "p" else tag.attrs)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIn("style", str(soup))

    def test_xformer_side_effect(self):
        def remove_class(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]
        html = '<p class="red" id="x">Hi</p>'
        replacer = SoupReplacer(xformer=remove_class)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertNotIn("class", str(soup))

    def test_combined_transformers(self):
        def rename(tag):
            return "div" if tag.name == "p" else tag.name
        def add_data(tag):
            attrs = dict(tag.attrs)
            attrs["data-test"] = "ok"
            return attrs
        html = "<p>Hello</p>"
        replacer = SoupReplacer(name_xformer=rename, attrs_xformer=add_data)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertIn("data-test", str(soup))

    def test_xml_name_xformer(self):
        xml = "<html><body><b>Hi</b><b>There</b></body></html>"
        replacer = SoupReplacer(name_xformer=lambda tag: "i" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(xml, "lxml", replacer=replacer)
        self.assertEqual(str(soup), "<html><body><i>Hi</i><i>There</i></body></html>")

    def test_no_replacement(self):
        html = "<p>Hello</p>"
        replacer = SoupReplacer()
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertEqual(str(soup), "<p>Hello</p>")