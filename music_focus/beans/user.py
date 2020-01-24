from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    male = 'male'
    female = 'female'


@dataclass
class User:
    """
    每种tab [profile, posts, video, super_topic, album], 都是一个container
    sina都会有一个container id
    """

    id: int
    name: str
    gender: Gender
    verified: bool
    description: str
    followers_cnt: int
    follow_cnt: int

    profile: int
    posts: int
    video: int
    super_topic: int
    album: int
