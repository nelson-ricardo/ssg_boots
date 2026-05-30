from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text",
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
        return (
            self.text == diff_text_node.text and
            self.text_type.value == diff_text_node.text_type.value and
            self.url == diff_text_node.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text_type_vals = [text_type.name for text_type in TextType]

    if text_node.text_type.name not in text_type_vals:
        raise ValueError("TextNode: invalid text type")

    if text_node.text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type is TextType.LINK:
        if text_node.url is None:
            raise ValueError("TextNode: LINK expects a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    else:
        if text_node.url is None or text_node.text is None:
            raise ValueError("TextNode: IMAGE expects url and text")

        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})