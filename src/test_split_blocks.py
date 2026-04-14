import unittest
from split_blocks import markdown_to_blocks, BlockType, block_to_block_type, markdown_to_html_node, extract_title

class test_split_blocks(unittest.TestCase):

    def test_markdown_to_blocks_1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_1(self):
        block = "## Hello"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_2(self):
        block = ' # Hello'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_3(self):
        block = '#Hello'
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_4(self):
        block = """
```
Blah Blah Blah
```
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_5(self):
        block = """
```
Blah Blah Blah
 ```
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_6(self):
        block = """
``` Hello
Blah Blah Blah
```
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_7(self):
        block = """
>Hello
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_8(self):
        block = """
>Hello
>Hello
>Hello
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_9(self):
        block = """
> Hello
> Hello
> Hello
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_10(self):
        block = """
 > Hello
 > Hello
 > Hello
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_11(self):
        block = """
> Hello
  Hello
> Hello
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_12(self):
        block = """
- adfsjl;
- adfslkj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_13(self):
        block = """
- adfsjl;
 - adfslkj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_14(self):
        block = """
-adfsjl;
-adfslkj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_15(self):
        block = """
1. adkjl
2. a;dsf
3. adj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_16(self):
        block = """
1. adkjl
4. adkh
2. a;dsf
3. adj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_17(self):
        block = """
1. adkjl

2. a;dsf
3. adj
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_18(self):
        block = """
Hello T-
his a normal paragraph
        """
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_markdown_to_html_1(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_2(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_markdown_to_html_3(self):
        md = """
# Title

This is some **interesting** _text_ with a [link](https://boot.dev).

```
Here is some code
```

And here is an image ![image](https://boot.dev)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Title</h1><p>This is some <b>interesting</b> <i>text</i> with a <a href="https://boot.dev">link</a>.</p><code>Here is some code</code><p>And here is an image <img src="https://boot.dev" alt="image"></p></div>'
        )

    def test_extract_title_1(self):
        md = """
# Hello
## he
        """
        header = extract_title(md)
        self.assertEqual(header, "Hello")

    def test_extract_title_2(self):
        md = """
#Hello
        """

        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()

