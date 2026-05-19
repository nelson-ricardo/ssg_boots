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
    
    def props_to_html(self):
        if self.props is not None:
            ret_string = ""
            for prop in self.props:
                ret_string += f"{prop}=\"{self.props[prop]}\" "
            return ret_string
        else:
            return ""
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"