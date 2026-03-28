import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_leafnode_1(self):
        node = LeafNode(tag=None, value="Hello World")
        self.assertEqual(node.to_html(), 'Hello World')

    def test_leafnode_2(self):
        node = LeafNode(tag="p", value="Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_leafnode_3(self):
        node = LeafNode(tag="p", value="Hello World", props={"href": "https://github.com"})
        self.assertEqual(node.to_html(), "<p href=https://github.com>Hello World</p>")

if __name__ == "__main__":
    unittest.main()
