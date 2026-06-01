import re

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

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    ret_list = list()

    for node in old_nodes:
        # check if the node is something other than just text
        if node.text_type is not TextType.TEXT:
            ret_list.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) == 1:
            raise ValueError("split_nodes_delimiter DELIMITER: invalid delimiter type")

        for index, string in enumerate(split_text):
            # handles when split creates an empty string
            if string == "":
                continue
            if (index + 1) % 2 == 0:
                ret_list.append(TextNode(string, text_type))
            else:
                ret_list.append(TextNode(string, TextType.TEXT))
    
    return ret_list

def extract_markdown_images(text) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[(.+?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text) -> list[tuple[str, str]]:
    matches = re.findall(r"\[(.+?)\]\((.+?)\)", text)
    return matches

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    pattern = r"(!\[.+?\]\(.+?\))"

    ret_list = list()

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            ret_list.append(node)
            continue
        matches = re.split(pattern, node.text)
        for i, string in enumerate(matches):
            if string == "":
                continue
            if (i + 1) % 2 == 0:
                alt, url = extract_markdown_images(string)[0]
                ret_list.append(TextNode(alt, TextType.IMAGE, url))
            else:
                ret_list.append(TextNode(string, TextType.TEXT))
    return ret_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    pattern = r"(\[.+?\]\(.+?\))"

    ret_list = list()

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            ret_list.append(node)
            continue
        matches = re.split(pattern, node.text)
        for i, string in enumerate(matches):
            if string == "":
                continue
            if (i + 1) % 2 == 0:
                text, url = extract_markdown_links(string)[0]
                ret_list.append(TextNode(text, TextType.LINK, url))
            else:
                ret_list.append(TextNode(string, TextType.TEXT))
    
    return ret_list