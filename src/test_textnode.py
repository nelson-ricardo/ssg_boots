import unittest
from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node
from node_split_func import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_images, split_nodes_link, text_to_textnodes, markdown_to_blocks
from htmlnode import LeafNode
from md_to_html import markdown_to_html_node

class TestTextNode(unittest.TestCase):
    # check if equality works correctly
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    # check if inequality works correctly
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a test node", TextType.CODE)
        self.assertNotEqual(node, node2)
    # checks if representations with links work correctly
    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://youtube.com")
        expect_out = "TextNode(This is a link, link, https://youtube.com)"
        self.assertEqual(repr(node), expect_out)
    def test_no_link(self):
        node = TextNode("This is some random text", TextType.ITALIC)
        expect_out = "TextNode(This is some random text, italic, None)"
        self.assertEqual(repr(node), expect_out)
    def test_textnode_to_html_text(self):
        node = TextNode("text", TextType.TEXT)
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode(None, "text")
        self.assertEqual(repr(exp_leaf_node), repr(rep_node))
    def test_textnode_to_html_bold(self):
        node = TextNode("text", TextType.BOLD)
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode("b", "text")
        self.assertEqual(repr(exp_leaf_node), repr(rep_node)) 
    def test_textnode_to_html_italic(self):
        node = TextNode("text", TextType.ITALIC)
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode("i", "text")
        self.assertEqual(repr(exp_leaf_node), repr(rep_node))
    def test_textnode_to_html_code(self):
        node = TextNode("text", TextType.CODE)
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode("code", "text")
        self.assertEqual(repr(exp_leaf_node), repr(rep_node))
    def test_textnode_to_html_link(self):
        node = TextNode("text", TextType.LINK, "example.com")
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode("a", "text", {"href": "example.com"})
        self.assertEqual(repr(exp_leaf_node), repr(rep_node))
    def test_textnode_to_html_image(self):
        node = TextNode("text", TextType.IMAGE, "example.com")
        rep_node = text_node_to_html_node(node)
        exp_leaf_node = LeafNode("img", None, {"src": "example.com", "alt": "text"})
        self.assertEqual(repr(exp_leaf_node), repr(rep_node))
    def test_textnode_to_html_link_no_url(self):
        node = TextNode("text", TextType.LINK, None)
        with self.assertRaises(ValueError):
            rep_node = text_node_to_html_node(node)
    def test_textnode_to_html_image_no_url(self):
        node = TextNode("text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            rep_node = text_node_to_html_node(node)
    def test_split_delimiter_bold_start(self):
        node = TextNode("**I** have a small house", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_nodes = [TextNode("I", TextType.BOLD), TextNode(" have a small house", TextType.TEXT)]
        self.assertEqual(exp_nodes, new_nodes)
    def test_split_delimiter_bold_middle(self):
        node = TextNode("I have a **small** house", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_nodes = [
            TextNode("I have a ", TextType.TEXT),
            TextNode("small", TextType.BOLD),
            TextNode(" house", TextType.TEXT)
        ]
        self.assertEqual(exp_nodes, new_nodes)
    def test_split_delimiter_bold_end(self):
        node = TextNode("I have a small **house**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        exp_nodes = [
            TextNode("I have a small ", TextType.TEXT),
            TextNode("house", TextType.BOLD),
        ]
        self.assertEqual(exp_nodes, new_nodes)
    def test_split_delimiter_non_text_node(self):
        non_text_node = TextNode("I love pizza", TextType.ITALIC)
        node = TextNode("I have a small **house**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([non_text_node, node], "**", TextType.BOLD)
        exp_nodes = [
            non_text_node, 
            TextNode("I have a small ", TextType.TEXT),
            TextNode("house", TextType.BOLD),
        ]
        self.assertEqual(exp_nodes, new_nodes)
    def test_split_delimiter_invalid_delim(self):
        node = TextNode("I have a small !!!house", TextType.TEXT)
        with self.assertRaises(ValueError):
            new_nodes = split_nodes_delimiter([node], "!!!", TextType.BOLD)
    def test_extract_markdown_images(self):
        img_string = "![water](./water)"
        exp_match = [("water", "./water")]
        self.assertEqual(exp_match, extract_markdown_images(img_string))
    def test_extract_markdown_links(self):
        link_string = "[water](water.com)"
        exp_match = [("water", "water.com")]
        self.assertEqual(exp_match, extract_markdown_links(link_string))
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "I have a link to [youtube](youtube.com) and [netflix](netflix.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("I have a link to ", TextType.TEXT),
                TextNode("youtube", TextType.LINK, "youtube.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("netflix", TextType.LINK, "netflix.com")
            ],
            new_nodes
        )
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        exp_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(exp_nodes, text_to_textnodes(text))  
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    ) 
        

if __name__ == "__main__":
    unittest.main()