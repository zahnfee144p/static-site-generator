import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.url, None)

    def test_text_neq(self):
        node = TextNode("This is a text node with style", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    _ = unittest.main()
