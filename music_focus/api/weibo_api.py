import json
import re
import time
import urllib.parse
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from music_focus.beans.focus import Focus
from music_focus.beans.post import Post
from music_focus.beans.user import User, Gender
from music_focus.beans.video import Video
from music_focus.utils import dt_utils
from music_focus.utils.cache import Cache
from music_focus.utils.number_utils import parse_number

USER_POSTS_URL_FORMATTER = 'https://m.weibo.cn/u/{}'
POSTS_CSS_SELECTOR = '.card.m-panel.card9.weibo-member'


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
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get {} user_info fail, status code: {}, text: {}'.format(user_id, res.status_code, res.text)

    data = json.loads(res.text)

    def _get_tab_type(tab_type):
        for tab in data['data']['tabsInfo']['tabs']:
            if tab['tab_type'] == tab_type:
                return int(tab['containerid']) if tab['containerid'].isdigit() else 0
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
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
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
            link='https://m.weibo.cn/detail/{}'.format(card['mblog']['id']),
            comments=[]
        )
        posts.append(post)

    return posts


def get_focuses_by_user(user, use_cache=True):
    """
    根据user, 获取相关的热点(微博话题)

    :param user:
    :param use_cache:
    :return:
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}'.format(user.id, user.posts)
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get {} focuses fail, status code: {}, text: {}'.format(user, res.status_code, res.text)

    focuses = []
    data = json.loads(res.text)
    for card in data['data']['cards']:
        if card['card_type'] != 11:
            continue
        for card_item in card['card_group']:
            if card_item['card_type'] != 17:
                continue
            for item in card_item['group']:
                focus_title = item['title_sub']
                focus_info = _parse_focus_by_title(focus_title)
                focus = Focus(
                    title=focus_title,
                    description=focus_info['description'],
                    recent_read=focus_info['recent_read'],
                    read_cnt=focus_info['read_cnt'],
                    discuss_cnt=focus_info['discuss_cnt'],
                    member_cnt=focus_info['member_cnt'],
                    link='https://m.weibo.cn/search?containerid=' +
                         urllib.parse.quote('231522type=1&t=10&q=' + focus_title),
                    related_users=[user.name]
                )
                focuses.append(focus)
                time.sleep(1)
    return focuses


def _parse_focus_by_title(focus_title, use_cache=True):
    """
    根据热点标题解析热点

    目前热点就是微博上的话题
    :param focus_title: 热点标题
    :param use_cache:
    :return:
    """
    focus_info = {}

    # parse description, read_cnt, discus_cnt, member_cnt
    url = 'https://m.s.weibo.com/topic/detail?q=' + urllib.parse.quote(focus_title)
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get focus: {} html fail, status code: {}, text: {}'.format(focus_title, res.status_code, res.text)
    soup = BeautifulSoup(res.text, 'html5lib')
    description_tags = soup.find('div', {'class': 'g-list-a title detail'}).find_all('dl')
    focus_info['description'] = description_tags[-1].text.strip().replace(' ', '') if description_tags else ''
    read_cnt, discuss_cnt, member_cnt = [t.text for t in
                                         soup.find('div', {'class': 'g-list-a data'}).find('ul').find_all('span')]
    focus_info['read_cnt'], focus_info['discuss_cnt'], focus_info['member_cnt'] = \
        parse_number(read_cnt), parse_number(discuss_cnt), parse_number(member_cnt)
    time.sleep(1)

    # parse today read
    url = 'https://m.s.weibo.com/ajax_topic/trend?q={}&time=24h&type=read'.format(urllib.parse.quote(focus_title))
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get focus: {} 24h read fail, status code: {}, text: {}'.format(focus_title, res.status_code, res.text)
    today_read = 0
    today_start = False
    for time_point in json.loads(res.text)['data']['read']:
        if time_point['time'] == '00:00':
            today_start = True
        if today_start:
            today_read += time_point['value']
    time.sleep(1)

    # parse two days ago read
    url = 'https://m.s.weibo.com/ajax_topic/trend?q={}&time=7d&type=read'.format(urllib.parse.quote(focus_title))
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get focus: {} 7d read fail, status code: {}, text: {}'.format(focus_title, res.status_code, res.text)
    before_yesterday_read, yesterday_read = [time_point['value']
                                             for time_point in json.loads(res.text)['data']['read'][-2:]]

    focus_info['recent_read'] = 3 * today_read + 2 * yesterday_read + 1 * before_yesterday_read

    return focus_info


def get_videos_by_user(user, use_cache=True):
    """
    根据user, 获取相关的视频

    :param user
    :type user: User
    :param use_cache
    :type use_cache: bool
    """
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}'.format(user.id, user.posts)
    res = Cache().cache(url, requests.get, url) if use_cache else requests.get(url)
    assert res.status_code == 200, \
        'get {} posts fail, status code: {}, text: {}'.format(user, res.status_code, res.text)

    videos = []
    data = json.loads(res.text)
    for card in data['data']['cards']:
        if card['card_type'] != 9:
            continue

        page_info = None
        if card['mblog'].get('page_info', {}).get('type') == 'video':  # 此微博为原创视频
            page_info = card['mblog']['page_info']
        if card['mblog'].get('retweeted_status', {}).get('page_info', {}).get('type') == 'video':  # 此微博为转载视频
            if re.sub('乐队|_|樂團|樂隊|微博', '', user.name) \
                    not in card['mblog']['retweeted_status']['page_info']['media_info']['next_title']:  # 必须有涉及此用户
                continue
            page_info = card['mblog']['retweeted_status']['page_info']
        if not page_info:
            continue

        video = Video(
            id=page_info['media_info']['media_id'],
            post_id=int(card['mblog']['id']),
            user_id=user.id,
            user_name=user.name,
            time=datetime.fromtimestamp(page_info['media_info']['video_publish_time']),
            text=page_info['media_info']['next_title'],
            cover_path=page_info['page_pic']['url'],
            url=page_info['media_info']['stream_url_hd'],
            view_cnt=page_info['media_info']['online_users_number'],
            display_view_cnt=page_info['media_info']['online_users']
        )
        videos.append(video)

    return videos
