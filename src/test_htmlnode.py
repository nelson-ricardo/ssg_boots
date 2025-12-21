import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    test_props = {"href":"https://boot.dev", "target":"_blank"}
    test_node_no_props = LeafNode("p", "hello world")
    test_node_props = LeafNode("a", "click me", test_props)

    def test_init(self):
        self.assertEqual(repr(self.test_node_no_props), "HTMLNode(p, hello world, None, None)")

    def test_init_props(self):
        eq_rep_text = f"HTMLNode(a, click me, None, {self.test_props})"
        self.assertEqual(repr(self.test_node_props), eq_rep_text)

    def test_to_html_no_prop(self):
        self.assertEqual(self.test_node_no_props.to_html(), "<p>hello world</p>")

    def test_to_html_props(self):
        eq_rep_text = "<a href=\"https://boot.dev\" target=\"_blank\">click me</a>"
        self.assertEqual(self.test_node_props.to_html(), eq_rep_text)

    def test_rep(self):
        node = HTMLNode("h1", "Title")
        self.assertEqual(repr(node), "HTMLNode(h1, Title, None, None)")

    def test_to_html(self):
        # should raise an exception because the method is not implemented
        node = HTMLNode("h1", "Title")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        # check if the props_to_html generates the expected output
        test_props = {
            "class": "main-title",
            "id": "website-hero", 
        }

        node = HTMLNode("h1", "Title", props=test_props)
        expected_output = "class=\"main-title\" id=\"website-hero\""
        self.assertEqual(node.props_to_html(), expected_output)