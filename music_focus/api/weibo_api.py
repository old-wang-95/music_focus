import json

import requests

from music_focus.beans.post import Post
from music_focus.beans.user import User, Gender
from music_focus.utils import dt_utils
from music_focus.utils.cache import Cache


def get_user_info(user_id, use_cache=True):
    """
    根据用户id, 获取用户相关信息

    :param user_id:
    :type user_id: int
    :param use_cache:
    :type use_cache: bool
    :return:
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}'.format(user_id)
    if use_cache:
        res = Cache().cache(url, requests.get, url)
    else:
        res = requests.get(url)
    assert res.status_code == 200, \
        'get {} user_info fail, status code: {}, text: {}'.format(user_id, res.status_code, res.text)

    data = json.loads(res.text)

    def _get_tab_type(tab_type):
        for tab in data['data']['tabsInfo']['tabs']:
            if tab['tab_type'] == tab_type:
                return int(tab['containerid'])
        return 0

    user = User(
        id=user_id,
        name=data['data']['userInfo']['screen_name'],
        gender=Gender.male if data['data']['userInfo']['gender'] == 'm' else Gender.female,
        verified=data['data']['userInfo']['verified'],
        description=data['data']['userInfo']['description'],
        followers_cnt=data['data']['userInfo']['followers_count'],
        follow_cnt=data['data']['userInfo']['follow_count'],
        profile=_get_tab_type('profile'),
        posts=_get_tab_type('weibo'),
        video=_get_tab_type('video'),
        super_topic=_get_tab_type('cardlist'),
        album=_get_tab_type('album')
    )
    return user


def get_posts_by_user(user, use_cache=True):
    """
    根据user, 获取用户的微博列表

    :param user:
    :type user: User
    :param use_cache:
    :type use_cache: bool
    :return:
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}'.format(user.id, user.posts)
    if use_cache:
        res = Cache().cache(url, requests.get, url)
    else:
        res = requests.get(url)
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
