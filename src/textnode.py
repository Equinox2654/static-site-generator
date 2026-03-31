from enum import Enum
from typing import Text

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
