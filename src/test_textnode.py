import unittest

from textnode import TextNode, TextType, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_split_images_1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_2(self):
        node = TextNode(
            text="This has ![image](Nothing) and another ![image2](More Nothign)",
            text_type=TextType.TEXT
        )
        node2 = TextNode(
            text="This has [link](Nothing) and another ![image2](More Nothign)",
            text_type=TextType.TEXT
        )

        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "Nothing"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "image2", TextType.IMAGE, "More Nothign"
                ),
                TextNode("This has [link](Nothing) and another ", text_type=TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "More Nothign")
            ]
        )

    def test_split_links_1(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_2(self):
        node = TextNode(
            text="This has [image](Nothing) and another [image2](More Nothing)",
            text_type=TextType.TEXT
        )
        node2 = TextNode(
            text="This has ![link](Nothing) and another [image2](More Nothing)",
            text_type=TextType.TEXT
        )

        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This has ", TextType.TEXT),
                TextNode("image", TextType.LINK, "Nothing"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "image2", TextType.LINK, "More Nothing"
                ),
                TextNode("This has ![link](Nothing) and another ", text_type=TextType.TEXT),
                TextNode("image2", TextType.LINK, "More Nothing")
            ]
        )

    def test_text_to_node_1(self):
        text = "This **test** has _multiple_ **types** of `words` and a [link](https://link.com) plus an image ![image](https://image.com)"
        node_list = text_to_textnodes(text)
        self.assertListEqual(
            node_list,
            [
                TextNode("This ", TextType.TEXT),
                TextNode("test", TextType.BOLD),
                TextNode(" has ", TextType.TEXT),
                TextNode("multiple", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("types", TextType.BOLD),
                TextNode(" of ", TextType.TEXT),
                TextNode("words", TextType.CODE),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com"),
                TextNode(" plus an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.com")
            ]
        )

    def test_text_to_node_2(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()
