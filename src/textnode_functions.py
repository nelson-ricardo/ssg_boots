from htmlnode import LeafNode
from textnode import TextNode, TextType

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