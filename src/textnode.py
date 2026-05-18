from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# TextNode, instantiate the class
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # define equality (textnodes are equal if all contents are equal)
    def __eq__(self, diff_text_node):
        return (
            self.text == diff_text_node.text and
            self.text_type.value == diff_text_node.text_type.value and
            self.url == diff_text_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"