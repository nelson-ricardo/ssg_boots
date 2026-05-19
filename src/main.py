from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node1 = HTMLNode("p", "paragraph 1")
    node2 = HTMLNode("p", "paragraph 2")
    props = {
        "class": "solid",
        "id": "main-info"
    }

    testNode = HTMLNode("p", "just a plain paragraph", [node1, node2], props)

    print(testNode)

if __name__ == "__main__":
    main()