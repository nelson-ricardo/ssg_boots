import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
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