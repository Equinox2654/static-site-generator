from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph',
    HEADING = 'heading',
    CODE = 'code',
    QUOTE = 'quote',
    UNORDERED_LIST = 'unordered_list',
    ORDERED_LIST = 'ordered_list',

def markdown_to_blocks(markdown: str):
    text = markdown.split('\n\n')
    new_text = []
    for t in text:
        n = t.strip()
        if n == '':
            continue
        new_text.append(n)
    return new_text

def block_to_block_type(block: str):
    headers = re.findall(r'^#', block)
    code = re.findall(r'```', block)
    quote = re.findall(r'(?<!(.*?))>', block)
    unordered_list = re.findall(r'- ', block)
    ordered_list = re.findall(r'/d+. ', block)
    if len(headers) >= 1 and len(headers) <= 6:
        return BlockType.HEADING
    elif len(code) == 2:
        return BlockType.CODE
    elif len(quote) == 1:
        return BlockType.QUOTE
    elif len(unordered_list) >= 1:
        return BlockType.UNORDERED_LIST
    elif len(ordered_list) >= 1:
        previous_item = ordered_list[0]
        for item in ordered_list[1:]:
            if int(item.strip('. ')) == int(previous_item.strip('. ')):
                pass
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
