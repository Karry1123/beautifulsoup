from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment
import unittest


class TestBeautifulSoupIteration(unittest.TestCase):

    def test_simple_html_iteration(self):
        html = "<p>Hello <b>world</b></p><p>Another</p>"
        soup = BeautifulSoup(html, 'html.parser')
        nodes = list(soup)

        self.assertEqual(len(nodes), 6)

        expected = [
            ('Tag', '<p>'),
            ('NavigableString', 'Hello '),
            ('Tag', '<b>'),
            ('NavigableString', 'world'),
            ('Tag', '<p>'),
            ('NavigableString', 'Another'),
        ]
        for i, (expected_type, expected_start) in enumerate(expected):
            node = nodes[i]
            self.assertIsInstance(node, eval(expected_type))
            if isinstance(node, Tag):
                self.assertEqual(node.name, expected_start[1:-1])
            else:
                self.assertEqual(str(node), expected_start)

    def test_iteration_does_not_include_soup_itself(self):
        soup = BeautifulSoup("<a>Link</a>", 'html.parser')
        for node in soup:
            self.assertNotEqual(node.name, "[document]")
            self.assertIsNot(node, soup)

    def test_iteration_includes_comments_and_strings(self):
        markup = """<div>
            Hello
            <!-- comment -->
            <span>Text</span>
        </div>"""
        soup = BeautifulSoup(markup, 'html.parser')
        nodes = list(soup)
        types = [type(n).__name__ for n in nodes]
        self.assertIn('NavigableString', types)  # "Hello\n            "
        self.assertIn('Comment', types)
        self.assertIn('Tag', types)

    def test_empty_document(self):
        soup = BeautifulSoup("", 'html.parser')
        self.assertEqual(list(soup), [])

        soup = BeautifulSoup("   \n\t  ", 'html.parser')
        # Whitespace-only documents still have a string if not stripped
        nodes = list(soup)
        self.assertEqual(len(nodes), 1)
        self.assertIsInstance(nodes[0], NavigableString)

    def test_nested_structure_depth_first(self):
        html = "<div><p>One<span>Two</span></p><p>Three</p></div>"
        soup = BeautifulSoup(html, 'html.parser')
        names = [node.name if isinstance(node, Tag) else 'text' for node in soup]
        expected_order = ['div', 'p', 'text', 'span', 'text', 'p', 'text']
        self.assertEqual(names, expected_order)


if __name__ == '__main__':
    unittest.main()