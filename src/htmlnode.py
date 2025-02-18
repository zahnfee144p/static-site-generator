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
        props_str = ""
        if self.props == None:
            return props_str
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str


    @override
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"
    

    @override
    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
