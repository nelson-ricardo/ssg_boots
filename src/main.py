from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    DELIM = "**"

    first_string: str = "**I** have a small house"
    second_string: str = "I have a **small** house"
    third_string: str = "I have a small **house**"

    split_string_first = third_string.split("**")
    ret_list = list()

    for i, string in enumerate(split_string_first):
        if string == "":
            continue
        if (i + 1) % 2 == 0:
            ret_list.append(TextNode(string, TextType.BOLD))
        else:
            ret_list.append(TextNode(string, TextType.TEXT))
    
    print(ret_list)

if __name__ == "__main__":
    main()