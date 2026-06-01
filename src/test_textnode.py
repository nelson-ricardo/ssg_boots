import unittest
from textnode import TextNode, TextType
from textnode_functions import text_node_to_html_node, split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from htmlnode import LeafNode

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
        node = TextNode("I have a small **house**", TextType.TEXT)
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
    
    
        

if __name__ == "__main__":
    unittest.main()