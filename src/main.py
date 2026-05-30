from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode("div", [child_node])
        
        print(parent_node.to_html())

if __name__ == "__main__":
    main()