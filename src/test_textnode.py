import unittest

from textnode import TextNode, TextType, split_nodes_image, split_nodes_link


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


if __name__ == "__main__":
    unittest.main()
