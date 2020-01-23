from dataclasses import dataclass


@dataclass
class Comment:
    user_name: str
    content: str
