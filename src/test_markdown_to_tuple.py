import unittest

from markdown_to_tuple import extract_markdown_images, extract_markdown_links

class test_markdown_to_tuple(unittest.TestCase):

    def test_extract_markdown_images_1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This text has [image](hello) and a real ![image](https://boot.dev)"
        )
        self.assertListEqual([("image", "https://boot.dev")], matches)

    def test_extract_markdown_images_3(self):
        matches = extract_markdown_images(
            "This text has ![image] but no link"
        )
        self.assertListEqual([], matches)
        
    def test_extract_markdown_links_1(self):
        matches = extract_markdown_links(
            "This text has a [link](https://hello.com)"
        )
        self.assertListEqual([("link", "https://hello.com")], matches)

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
            "This text has [link](hello) and an image ![image](https://boot.dev)"
        )
        self.assertListEqual([("link", "hello")], matches)

    def test_extract_markdown_links_3(self):
        matches = extract_markdown_links(
            "This text has [text] but no link"
        )
        self.assertListEqual([], matches)

if __name__ == '__main__':
    unittest.main()
