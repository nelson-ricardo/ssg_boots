import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Assert equality of nodes
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_uneq(self):
        # assert unequality of nodes with links
        link_node = TextNode("Some anchor text", TextType.LINK, "http://boot.dev")
        img_node = TextNode("Some anchor text", TextType.IMAGE, "http://boot.dev")
        self.assertNotEqual(link_node, img_node)
    def test_eq_links(self):
        link1 = TextNode("cool math games", TextType.LINK, "www.example.com")
        link2 = TextNode("cool math games", TextType.LINK, "www.example.com")
        self.assertEqual(link1, link2)

if __name__ == "__main__":
    unittest.main()