from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node, extract_markdown_images, extract_markdown_links
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    image_string = "![hotdog](./hotdog.jpg) ![car](https://car.com/cool-car.webp)"
    links_string = "[lolol](https://lol.com) goes to somewhere in the forest [the forest](https://the-firest.com) and he lies there"
    images_list = extract_markdown_images(image_string)
    links_list = extract_markdown_links(links_string)

    print("images", images_list, "links", links_list)

if __name__ == "__main__":
    main()