from enum import Enum
from markdown_to_tuple import extract_markdown_images, extract_markdown_links

class TextType(Enum):
    TEXT = 'Plain text',
    BOLD = '**Bold text**',
    ITALIC = '__Italic text__',
    CODE = '`Code text`',
    LINK = '[anchor text](url)'
    IMAGE = '![alt text](url)',

class TextNode():
    
    def __init__(self, text: str, text_type: TextType, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value) -> bool:
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        return True

    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    return_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            return_list.append(node)
            continue
        new_text: list[str] = node.text.split(delimiter)
        if len(new_text) % 2 == 0:
            raise Exception(f"No closing Delimiter Found in node {node}")
        for i in range(len(new_text)):
            if new_text[i] == '':
                continue
            if i % 2 == 0:
                return_list.append(TextNode(text=new_text[i], text_type=TextType.TEXT))
            else:
                return_list.append(TextNode(text=new_text[i], text_type=text_type))
    return return_list

def split_nodes_image(old_nodes: list[TextNode]):
    return_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            return_list.append(old_node)
            continue
        og_text = old_node.text
        images = extract_markdown_images(og_text)
        if len(images) == 0:
            return_list.append(old_node)
            continue
        for image in images:
            sections = og_text.split(f'![{image[0]}]({image[1]})', 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown. Incorrect image format.")
            if sections[0] != "":
                return_list.append(TextNode(text=sections[0], text_type=TextType.TEXT))
            return_list.append(
                TextNode(
                    text=image[0],
                    text_type=TextType.IMAGE,
                    url=image[1]
                )
            )
            og_text = sections[1]
        if og_text != "":
            return_list.append(TextNode(text=og_text, text_type=TextType.TEXT))
    return return_list

def split_nodes_link(old_nodes: list[TextNode]):
    return_list = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            return_list.append(old_node)
            continue
        og_text = old_node.text
        links = extract_markdown_links(og_text)
        if len(links) == 0:
            return_list.append(old_node)
            continue
        for link in links:
            sections = og_text.split(f'[{link[0]}]({link[1]})', 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown. Incorrect Link Format")
            if sections[0] != "":
                return_list.append(TextNode(text=sections[0], text_type=TextType.TEXT))
            return_list.append(TextNode(
                text=link[0],
                text_type=TextType.LINK,
                url=link[1]
            ))
            og_text = sections[1]
        if og_text != "":
            return_list.append(TextNode(text=og_text, text_type=TextType.TEXT))
    return return_list

def text_to_textnodes(text):
    og_node = TextNode(text=text, text_type=TextType.TEXT)
    node_list = []

    node_list = split_nodes_delimiter([og_node], '**', TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, '_', TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, '`', TextType.CODE)
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    return node_list
