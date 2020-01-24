from dataclasses import dataclass
from datetime import datetime
from typing import List

from music_focus.beans.comment import Comment


@dataclass
class Post:
    id: int
    user_id: int
    user_name: str
    time: datetime
    content: str
    share_cnt: int
    comment_cnt: int
    like_cnt: int
    comments: List[Comment]
