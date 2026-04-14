from textnode import TextNode, TextType

class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ''
        if self.props:
            for prop in self.props:
                if string == '':
                    string = f'{prop}="{self.props[prop]}"'
                else:
                    string = f'{string} {prop}="{self.props[prop]}"'
            return string
        return string

class LeafNode(HTMLNode):

    def __init__(self, tag, value='', props=None) -> None:
        super().__init__(tag = tag, value = value, props = props)

    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

    def to_html(self):
        if not self.value and self.tag:
            return f'<{self.tag} {self.props_to_html()}>'
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        if self.tag:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return self.value

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def __repr__(self) -> str:
        return f'ParentNode({self.tag}, {self.children}, {self.props})'

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag Provided.")
        if not self.children or len(self.children) == 0:
            raise ValueError("No Children Provided.")
        html = ''
        for child in self.children:
            html = f'{html}{child.to_html()}'
        return f'<{self.tag}>{html}</{self.tag}>'

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.IMAGE:
            return LeafNode(tag='img', value='', props={'src': text_node.url, 'alt': text_node.text})
        case TextType.LINK:
            return LeafNode(tag='a', value=text_node.text, props={'href': text_node.url})
        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)
