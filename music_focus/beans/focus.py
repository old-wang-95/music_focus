from dataclasses import dataclass


@dataclass
class Focus:
    title: str
    description: str
    today_read: int  # 今日阅读数
    read_cnt: int  # 总阅读
    discuss_cnt: int  # 总讨论数
    member_cnt: int  # 总参与人数
    link: str
