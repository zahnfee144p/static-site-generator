from typing import override


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self):
        raise NotImplementedError

    @override
    def __repr__(self):
        return f"HTMLNode(\ntag: {self.tag}\nvalue:{self.value}\nchildren: {self.children}\nprops: {self.props})"
    
