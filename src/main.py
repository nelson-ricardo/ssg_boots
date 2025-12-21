from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    properties = {
        "href" : "https://boot.dev",
        "target": "_blank",
    }

    link_node = HTMLNode("a", "click me", props=properties)

    print(link_node)

if __name__ == "__main__":
    main()