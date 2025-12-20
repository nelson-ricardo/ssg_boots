
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # HTML tag name
        self.value = value # string representing the value of the HTML tag
        self.children = children # list of HTMLNode objects rep. children
        self.props = props # dic representing attributes (e.g. href or target)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("Method Not Implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        ret_string = ""
        for attr in self.props:
            ret_string += f"{attr}=\"{self.props[attr]}\" "
        
        return ret_string.rstrip()