from enum import Enum

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

