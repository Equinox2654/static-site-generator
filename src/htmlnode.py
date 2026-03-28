
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
