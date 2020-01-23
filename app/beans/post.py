from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.beans.comment import Comment


@dataclass
class Post:
    user_id: str
    user_name: str
    time: datetime
    content: str
    share_num: int
    comment_num: int
    like_num: int
    comments: List[Comment]
