from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
        random_node = TextNode("text", TextType.BOLD)
        new_node = text_node_to_html_node(random_node)

if __name__ == "__main__":
    main()