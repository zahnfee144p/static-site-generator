import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_p_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node, expected)

    def test_a_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node, expected)

    def test_b_to_html(self):
        node = LeafNode("b", "bold", None).to_html()
        expected = "<b>bold</b>"
        self.assertEqual(node, expected)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    _ = unittest.main()
