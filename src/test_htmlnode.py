import unittest

from htmlnode import HTMLNode

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
    def props_to_html(self):
        props = {
            "class": "solid"
        }
        test_node_props = HTMLNode("p", "value", None, props).props_to_html()
        self.assertEqual(test_node_props, "class=\"solid\"")
    # check props to html without props
    def no_props_to_html(self):
        test_node_props = HTMLNode("p", "value")
        self.assertEqual("", test_node_props.props_to_html())