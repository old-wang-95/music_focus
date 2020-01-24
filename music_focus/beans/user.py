from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    male = 'male'
    female = 'female'


@dataclass
class User:
    id: int
    name: str
    gender: Gender
    verified: bool  # 是否被验证
    description: str  # 简介
    followers_cnt: int  # 关注者数量
    follow_cnt: int  # 关注数量
    profile: int  # 主页id
    weibo: int  # 微博页id
    video: int  # 视频页id
    super_topic: int  # 超话页id
    album: int  # 相册页id
