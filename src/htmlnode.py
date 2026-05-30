class HTMLNode():
    '''
    constructor
    tag: tag type
    value: value inside of the tag
    children: list of HTMLNode children
    props: key-value dictionary containing all the properties
    '''
    def __init__(self, 
                 tag : str | None = None,
                 value: str | None = None,
                 children: list[HTMLNode] | None = None,
                 props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is not None:
            ret_string = ""
            for prop in self.props:
                ret_string += f" {prop}=\"{self.props[prop]}\""
            return ret_string
        else:
            return ""
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str | None, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self) -> str:
        if self.value is None: 
            raise ValueError("invalid HTML: need value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self) -> str:

        # handles the case were Parent Node does not have a tag
        # or children, a parent node ALWAYS has children, if not it would be
        # a leaf node
        if self.tag is None:
            raise ValueError("Node needs a tag value")
        if self.children is None:
            raise ValueError("Node needs children")


        ret_string = f"<{self.tag}{self.props_to_html()}>"
        for childNode in self.children:
            ret_string += childNode.to_html()
        ret_string += f"</{self.tag}>"

        return ret_string
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"