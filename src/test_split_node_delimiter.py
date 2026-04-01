from typing import Text
import unittest

from textnode import TextNode, TextType, split_nodes_delimiter

class test_spit_node_delimiter(unittest.TestCase):

    def test1(self):
        text_node = TextNode(text="Hello **World**!", text_type=TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], '**', TextType.BOLD)
        self.assertEqual(new_nodes,
                 [
                 TextNode(text="Hello ", text_type=TextType.TEXT),
                 TextNode(text="World", text_type=TextType.BOLD),
                 TextNode(text='!', text_type=TextType.TEXT)
                 ]
            )

    def test2(self):
        text_node = TextNode(text="Hello **World!", text_type=TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([text_node], '**', TextType.BOLD)

    def test3(self):
        text_node = TextNode(text="I **LOVE** the **Human Race**.", text_type=TextType.TEXT)
        new_nodes = split_nodes_delimiter([text_node], '**', TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode(text="I ", text_type=TextType.TEXT),
                TextNode(text="LOVE", text_type=TextType.BOLD),
                TextNode(text=' the ', text_type=TextType.TEXT),
                TextNode(text='Human Race', text_type=TextType.BOLD),
                TextNode(text='.', text_type=TextType.TEXT),
            ]
        )

    def test4(self):
        text_nodes = [
            TextNode(text='Hello **World**', text_type=TextType.TEXT),
            TextNode(text='**Hello** World', text_type=TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(text_nodes, '**', TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode(text='Hello ', text_type=TextType.TEXT),
                TextNode(text='World', text_type=TextType.BOLD),
                TextNode(text='Hello', text_type=TextType.BOLD),
                TextNode(text=' World', text_type=TextType.TEXT),
            ]
        )

if __name__ == '__main__':
    unittest.main()
