import json

import requests

from music_focus.beans.user import User, Gender
from music_focus.cache import Cache


def get_user_info(user_id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={}'.format(user_id)
    res = Cache().cache(url, requests.get, url)
    assert res.status_code == 200, \
        'get user_info fail, status code: {}, text: {}'.format(res.status_code, res.text)

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
        weibo=int(
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
