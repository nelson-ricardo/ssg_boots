from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node
from node_split_func import extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    image_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(image_string)

    print(nodes)


if __name__ == "__main__":
    main()