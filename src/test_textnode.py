import unittest
from textnode import TextNode, TextType

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
        

if __name__ == "__main__":
    unittest.main()