from enum import Enum
import re
from htmlnode import ParentNode, LeafNode, text_node_to_html_node 
from textnode import text_to_textnodes, TextNode, TextType
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
    headers = re.findall(r'^#{1,6} ', block, re.MULTILINE)
    code = re.findall(r'```\n(.*?)\n```\s*$', block, re.DOTALL)
    quote = re.findall(r'^>', block, re.MULTILINE)
    unordered_list = re.findall(r'^- ', block, re.MULTILINE)
    ordered_list = re.findall(r'^(\d+)\. ', block, re.MULTILINE)
    is_ordered = [int(n) for n in ordered_list] == list(range(1, len(ordered_list) + 1))
    if len(headers) == 1:
        return BlockType.HEADING
    elif len(code) == 1:
        return BlockType.CODE
    elif len(quote) == len(block.split('\n')) - 2:
        return BlockType.QUOTE
    elif len(unordered_list) == len(block.split('\n')) - 2:
        return BlockType.UNORDERED_LIST
    elif len(ordered_list) == len(block.split('\n')) - 2 and is_ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str):
    html_nodes = text_to_children(markdown)
    html_node = ParentNode(tag='div', children=html_nodes)
    return html_node

def parse_text(text: str):
    text_nodes = text_to_textnodes(text)
    nodes = []
    for text_node in text_nodes:
        nodes.append(text_node_to_html_node(text_node))
    return nodes

def text_to_children(text: str):
    blocks = markdown_to_blocks(text)
    nodes: list = []
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                lines: list = block.split('\n')
                text = ' '.join(lines)
                leaf_nodes = parse_text(text)
                nodes.append(ParentNode(tag='p', children=leaf_nodes))
            case BlockType.HEADING:
                lines = block.split('\n')
                for line in lines:
                    headers = re.findall(r'^#{1,6} ', line, re.MULTILINE)
                    levels = [len(h) for h in headers]
                    leaf_nodes = parse_text(line.strip(headers[0]))
                    match len(levels):
                        case 1:
                            nodes.append(ParentNode(tag='h1', children=leaf_nodes))
                        case 2:
                            nodes.append(ParentNode(tag='h2', children=leaf_nodes))
                        case 3:
                            nodes.append(ParentNode(tag='h3', children=leaf_nodes))
                        case 4:
                            nodes.append(ParentNode(tag='h4', children=leaf_nodes))
                        case 5:
                            nodes.append(ParentNode(tag='h5', children=leaf_nodes))
                        case 6:
                            nodes.append(ParentNode(tag='h6', children=leaf_nodes))
            case BlockType.CODE:
                nodes.append(LeafNode(tag='code', value=block.strip('```\n').strip('\n```')))
            case BlockType.QUOTE:
                lines = block.split('\n')
                for line in lines:
                    line = line.strip('>').strip('\n')
                    leaf_nodes = parse_text(line)
                    nodes.append(ParentNode(tag='p', children=leaf_nodes))
            case BlockType.UNORDERED_LIST:
                lines = block.split('\n')
                leaf_nodes = []
                for line in lines:
                    line = line.strip('- ').strip('\n')
                    leaf_leaf_nodes = parse_text(line)
                    leaf_nodes.append(ParentNode(tag='li', children=leaf_leaf_nodes))
                nodes.append(ParentNode(tag='ul', children=leaf_nodes))
            case BlockType.ORDERED_LIST:
                lines = block.split('\n')
                leaf_nodes = []
                for line in lines:
                    start = re.findall(r'^(\d+)\. ', line)
                    line = line.strip(start)
                    leaf_leaf_nodes = parse_text(line)
                    leaf_nodes.append(ParentNode(tag='li', children=leaf_leaf_nodes))
                nodes.append(ParentNode(tag='ol', children=leaf_nodes))
    return nodes

def extract_title(markdown):
    if not re.search(r'^# ', markdown, re.MULTILINE):
        raise Exception("No Title Found")
    header = re.findall(r'^# .*', markdown, re.MULTILINE)
    return header[0].strip('# ').strip()
