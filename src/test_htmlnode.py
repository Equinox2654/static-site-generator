import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def test_props_to_html_1(self):
        node = HTMLNode(props={
            'href': 'https://github.com',
        })
        self.assertEqual(node.props_to_html(), 'href="https://github.com"')

    def test_props_to_html_2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_3(self):
        node = HTMLNode(props={
            'h': 'h',
            't': 't',
        })
        self.assertEqual(node.props_to_html(), 'h="h" t="t"')

if __name__ == "__main__":
    unittest.main()
