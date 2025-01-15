import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "link", list(), {"href": "https://www.google.com"})
        node2 = HTMLNode("<a>", "link", list(), {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("<a>", "link", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("<p>", "link", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = HTMLNode("<a>", "other link", None, None)
        self.assertEqual(node.props, None)

    def test_text_neq(self):
        node = HTMLNode("<a>", "other link", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("<a>", "link", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    _ = unittest.main()
