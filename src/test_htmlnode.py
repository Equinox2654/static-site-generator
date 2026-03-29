import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(node.to_html(), '<p href="https://github.com">Hello World</p>')

    def test_parent_to_html_1(self):
        child_node = LeafNode(tag='b', value='HI')
        parent_node = ParentNode(tag='p', children=[child_node])
        self.assertEqual(parent_node.to_html(), '<p><b>HI</b></p>')
        
    def test_parent_to_html_2(self):
        child_node = LeafNode(tag='b', value='HI')
        child_node2 = LeafNode(tag='b', value='HI')
        parent_node = ParentNode(tag='p', children=[child_node, child_node2])
        self.assertEqual(parent_node.to_html(), '<p><b>HI</b><b>HI</b></p>')

    def test_parent_to_html_3(self):
        grandchild_node = LeafNode(tag='b', value='HI')
        child_node = ParentNode(tag='p', children=[grandchild_node])
        parent_node = ParentNode(tag='div', children=[child_node])
        self.assertEqual(parent_node.to_html(), '<div><p><b>HI</b></p></div>')

if __name__ == "__main__":
    unittest.main()
