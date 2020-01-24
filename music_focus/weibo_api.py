import json

import requests

from music_focus.beans.post import Post
from music_focus.beans.user import User, Gender
from music_focus.cache import Cache
from music_focus.utils import dt_utils


def get_user_info(user_id):
    """
    根据用户id, 获取用户相关信息

    :param user_id:
    :type user_id: int
    :return:
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}'.format(user_id)
    res = Cache().cache(url, requests.get, url)
    assert res.status_code == 200, \
        'get {} user_info fail, status code: {}, text: {}'.format(user_id, res.status_code, res.text)

    data = json.loads(res.text)
    user = User(
        id=user_id,
        name=data['data']['userInfo']['screen_name'],
        gender=Gender.male if data['data']['userInfo']['gender'] == 'm' else Gender.female,
        verified=data['data']['userInfo']['verified'],
        description=data['data']['userInfo']['description'],
        followers_cnt=data['data']['userInfo']['followers_count'],
        follow_cnt=data['data']['userInfo']['follow_count'],
        profile=int(
            [tab['containerid'] for tab in data['data']['tabsInfo']['tabs'] if tab['tab_type'] == 'profile'][0]
        ),
        posts=int(
            [tab['containerid'] for tab in data['data']['tabsInfo']['tabs'] if tab['tab_type'] == 'weibo'][0]
        ),
        video=int(
            [tab['containerid'] for tab in data['data']['tabsInfo']['tabs'] if tab['tab_type'] == 'video'][0]
        ),
        super_topic=int(
            [tab['containerid'] for tab in data['data']['tabsInfo']['tabs'] if tab['tab_type'] == 'cardlist'][0]
        ),
        album=int(
            [tab['containerid'] for tab in data['data']['tabsInfo']['tabs'] if tab['tab_type'] == 'album'][0]
        )
    )
    return user


def get_posts_by_user(user):
    """
    根据user, 获取用户的微博列表

    :param user:
    :type user: User
    :return:
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}'.format(user.id, user.posts)
    res = Cache().cache(url, requests.get, url)
    assert res.status_code == 200, \
        'get {} posts fail, status code: {}, text: {}'.format(user, res.status_code, res.text)

    posts = []
    data = json.loads(res.text)
    for card in data['data']['cards']:
        if card['card_type'] != 9:
            continue
        post = Post(
            id=int(card['mblog']['id']),
            user_id=user.id,
            user_name=user.name,
            time=dt_utils.parse_date_time(card['mblog']['created_at']),
            content=card['mblog']['text'],
            share_cnt=card['mblog']['reposts_count'],
            comment_cnt=card['mblog']['comments_count'],
            like_cnt=card['mblog']['attitudes_count'],
            comments=[]
        )
        posts.append(post)

    return posts
