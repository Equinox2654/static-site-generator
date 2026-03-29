import unittest

from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType

class test_text_to_html(unittest.TestCase):

    def test1(self):
        text_node = TextNode(text="HI", text_type=TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), '<b>HI</b>')

    def test2(self):
        text_node = TextNode(text="HI", text_type=TextType.TEXT)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.tag, None)
        self.assertEqual(leaf_node.to_html(), 'HI')

if __name__ == '__main__':
    unittest.main()
