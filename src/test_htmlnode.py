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

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag: p, value: What a strange world, children: None, props: {'class': 'primary'})",
        )


if __name__ == "__main__":
    _ = unittest.main()
