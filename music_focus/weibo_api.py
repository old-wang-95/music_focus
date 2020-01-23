import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': 'YF-Page-G0=84b093c4d9813e1ef94d4c84b4d23923|1579779107|1579779107; WBtopGlobal_register_version=307744aa77dd5677; Ugrow-G0=1ac418838b431e81ff2d99457147068c; SUB=_2AkMpde3qf8NxqwJRmPEWy2nrbo92yQrEieKfKRwxJRMxHRl-yT92qnAntRB6AvXDBTAge7xfMbf7YYIPdurLoqp_mS23; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFA1AJKOgABjb3Jn6sifWFl; YF-V5-G0=8c4aa275e8793f05bfb8641c780e617b; Apache=5509799178652.603.1579770491820; _s_tentry=-; SINAGLOBAL=5509799178652.603.1579770491820; ULV=1579770491859:1:1:1:5509799178652.603.1579770491820:',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Host': 'weibo.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive'
}


def get_posts_by_user(user_id):
    # request
    url = 'https://weibo.com/p/{}/home?profile_ftype=1&is_all=1#_0'.format(user_id)
    res = requests.get(url, headers=headers)
    assert res.status_code == 200, \
        'get posts by user id fail, status code: {}, text: {}'.format(res.status_code, res.text)

    # parse
    bs = BeautifulSoup(res.text, 'html5lib')
    posts_panel = bs.find('div', attrs={'class': 'WB_frame_c'})
    if not posts_panel:
        raise Exception('can not find posts panel!')
    for post in posts_panel.find_all('div', attrs={'action-type': 'feed_list_item'}):
        print(post)
