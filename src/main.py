import os, shutil

from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node
from node_split_func import extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_link, text_to_textnodes, markdown_to_blocks, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode
from md_to_html import generate_pages_recursive

def cp_static_to_public():

    # removes the current contents of public if it already exists
    if os.path.exists("./public"):
        print("Removing the public folder")
        shutil.rmtree("./public")
        os.mkdir("./public")
    else:
        print("Nothing to remove")
        os.mkdir("./public")

    copy_files_to_public("static", "public")

def copy_files_to_public(src_path: str, dest_path: str):
    items = os.listdir(f"./{src_path}")
    for item in items:
        item_file_path = f"./{src_path}/{item}"
        if os.path.isfile(item_file_path):
            shutil.copy2(item_file_path, f"./{dest_path}")
            print(f"I found a file at {item_file_path}.\nI will copy this to ./{dest_path}/{item}")
        else:
            os.mkdir(f"./{dest_path}/{item}")
            copy_files_to_public(f"{src_path}/{item}", f"{dest_path}/{item}")
            

def main():
    cp_static_to_public()
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()