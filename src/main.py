from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node
from node_split_func import extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_link, text_to_textnodes, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    test_string = '''
# This is a heading

This is some paragraph that I want to keep. I want to keep writing
This is part of the same paragraph

- This is a list
- This is part of the same list

'''
    nodes = markdown_to_blocks(test_string)

    print(nodes)


if __name__ == "__main__":
    main()