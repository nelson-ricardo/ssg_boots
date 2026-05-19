import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    # check representation without children or props
    def test_rep_simple(self):
        node = HTMLNode("p", "simple")
        exp_out = "HTMLNode(p, simple, None, None)"
        self.assertEqual(repr(node), exp_out)
    # check representation without props
    def test_rep_w_child(self):
        child = HTMLNode("p", "p1")
        test_node = HTMLNode("div", None,[child])
        exp_out = "HTMLNode(div, None, [HTMLNode(p, p1, None, None)], None)"
        self.assertEqual(repr(test_node), exp_out)
    # check representation with everything included
    def test_rep_everything(self):
        child = HTMLNode("p", "p1")
        props = {
            "class":"c1",
            "id":"id1"
        }
        test_node = HTMLNode("div", "value", [child], props)
        exp_out = "HTMLNode(div, value, [HTMLNode(p, p1, None, None)], {'class': 'c1', 'id': 'id1'})"
        self.assertEqual(repr(test_node), exp_out)
    # check props to html with props
    def test_props_to_html(self):
        props = {
            "class": "solid"
        }
        test_node_props = HTMLNode("p", "value", None, props).props_to_html()
        self.assertEqual(test_node_props, " class=\"solid\"")
    # check props to html without props
    def test_no_props_to_html(self):
        test_node_props = HTMLNode("p", "value")
        self.assertEqual("", test_node_props.props_to_html())
    
    # check LeafNode representation
    def test_leafNode_rep(self):
        test_node = LeafNode("string", "p")
        exp_out = "LeafNode(p, string, None)"
        self.assertEqual(repr(test_node), exp_out)
    # check LeafNode representation with props
    def test_leafNode_props_rep(self):
        props = {
            "class": "solid"
        }
        test_node = LeafNode("value", "p", props)
        exp_out = "LeafNode(p, value, {'class': 'solid'})"
        self.assertEqual(repr(test_node), exp_out)
    # check LeafNode html with no props
    def test_leafNode_html_no_props(self):
        test_node = LeafNode("paragraph", "p1")
        exp_out = "<p1>paragraph</p1>"
        self.assertEqual(test_node.to_html(), exp_out)
    # check LeafNode html with one prop
    def test_leafNode_html_one_prop(self):
        prop = {
            "class": "solid"
        }
        test_node = LeafNode("paragraph", "p1", prop)
        exp_out = "<p1 class=\"solid\">paragraph</p1>"
        self.assertEqual(test_node.to_html(), exp_out)
    # check LeafNode html with mult props
    def test_leafNode_html_mult_props(self):
        props = {
            "class": "link",
            "id": "main-website",
            "href": "http://example.com",
            "target": "_blank"
        }
        test_node = LeafNode("link", "a", props)
        exp_out = "<a class=\"link\" id=\"main-website\" href=\"http://example.com\" target=\"_blank\">link</a>"
        self.assertEqual(test_node.to_html(), exp_out)