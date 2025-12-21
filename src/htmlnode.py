
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

class LeafNode(HTMLNode):
    # LeafNode represents a single HTML tag with no children like:
    # <p>This is a paragraph </p>

    # initialize properties of HTMLNode passed in from LeafNode
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        # value does not exist
        if self.value is None:
            raise ValueError("All leaf nodes **must** have a value")

        # there is no tag information
        if self.tag is None:
            return self.value

        # changes props to html
        properties = self.props_to_html()

        # if there are no properties makes a clean html tag
        # if there are properties it adds one space, then properties
        # then everything else
        if properties == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {properties}>{self.value}</{self.tag}>"