from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_link
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    image_string = "I have a very cute cat, here is a picture of it: [cute cat](http://example.com) and I love it, I also have a dog, here it is: [cute dog](http://example.com) I love my animals"
    node = TextNode(image_string, TextType.TEXT)
    list = split_nodes_link([node, node, node, TextNode("yurr", TextType.BOLD), node])

    print(list)


if __name__ == "__main__":
    main()