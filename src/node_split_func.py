import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    ret_list = list()

    for node in old_nodes:
        # check if the node is something other than just text
        if node.text_type is not TextType.TEXT:
            ret_list.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
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

def text_to_textnodes(text: str) -> list[TextNode]:
    mother_node = TextNode(text, TextType.TEXT)
    ret_nodes = split_nodes_delimiter([mother_node], "**", TextType.BOLD)
    ret_nodes = split_nodes_delimiter(ret_nodes, "_", TextType.ITALIC)
    ret_nodes = split_nodes_delimiter(ret_nodes, "`", TextType.CODE)
    ret_nodes = split_nodes_images(ret_nodes)
    ret_nodes = split_nodes_link(ret_nodes)

    return ret_nodes

def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdown = markdown.split("\n\n")
    no_empty_list = [item for item in split_markdown if item != ""]
    ret_list = list(map(lambda x: x.strip(), no_empty_list))
    
    return ret_list