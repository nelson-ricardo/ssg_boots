from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

# TextNode, instantiate the class
class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # define equality (textnodes are equal if all contents are equal)
    def __eq__(self, diff_text_node):
        if not isinstance(diff_text_node, TextNode):
            return False 
        else:
            return (
                self.text == diff_text_node.text and
                self.text_type.value == diff_text_node.text_type.value and
                self.url == diff_text_node.url
            )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

