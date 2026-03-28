import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_1(self):
        node = TextNode("1", TextType.ITALIC, 'hello')
        node2 = TextNode("1", TextType.ITALIC, 'hello')
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Text node 1", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_1(self):
        node = TextNode("1", TextType.LINK, 'http://github.com')
        node2 = TextNode("1", TextType.LINK, 'https://github.com')
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
