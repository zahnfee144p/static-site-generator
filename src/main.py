from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node)

main()
