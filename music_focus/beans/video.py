from dataclasses import dataclass
from datetime import datetime


@dataclass
class Video:
    id: str
    post_id: int
    user_id: int
    user_name: str
    time: datetime
    text: str
    cover_path: str
    url: str
    view_cnt: int
    display_view_cnt: str
