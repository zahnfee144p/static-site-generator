from enum import Enum
from typing import override

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode:
    def __init__(self, text:str, text_type:TextType, url:str|None=None) -> None:
        self.text:str = text
        self.text_type = text_type
        self.url = url


    @override
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    @override
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

