import os
import time
from datetime import datetime
from datetime import timedelta

from music_focus import logger
from music_focus.api import firefox_api
from music_focus.api import weibo_api
from music_focus.api.weibo_api import USER_POSTS_URL_FORMATTER, POSTS_CSS_SELECTOR
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class FetchPostsProcessor(ProcessorBase):

    def __init__(self, before_day=3):
        self._before_data = before_day
        self._images_dir = 'data/weibo_images'
        if not os.path.exists(self._images_dir):
            os.makedirs(self._images_dir)

    def run(self, workflow_input, tmp_result, workflow_output):
        posts = {}
        for music_type, users in users_config.items():
            posts[music_type] = []
            for user_id, _ in users:
                retry_time = 0
                while retry_time <= 3:
                    if retry_time > 0:
                        logger.info('start to retry, current retry time is: {}'.format(retry_time))
                    try:
                        use_cache = False if retry_time else True
                        # 获取当前用户信息及其微博信息
                        user = weibo_api.get_user_info(user_id, use_cache)
                        user_posts = weibo_api.get_posts_by_user(user, use_cache)
                        # 过滤旧微博, 并截图
                        new_user_posts = []  # 用户的新微博
                        for i, post_element in enumerate(
                                firefox_api.find_elements_in_page(USER_POSTS_URL_FORMATTER.format(user.id),
                                                                  POSTS_CSS_SELECTOR)):
                            if i >= len(user_posts) or user_posts[i].time <= datetime.now() - timedelta(
                                    days=self._before_data):  # 过滤旧微博
                                continue
                            image_path = '{}/{}.png'.format(self._images_dir, user_posts[i].id)
                            user_posts[i].image_path = '{}.png'.format(user_posts[i].id)
                            firefox_api.screenshot(post_element, image_path)
                            new_user_posts.append(user_posts[i])
                        posts[music_type].extend(new_user_posts)
                        logger.info('fetch user: {} data success'.format(user_id))
                        break
                    except Exception as e:
                        logger.exception('fetch user: {} data error! {}'.format(user_id, e))
                        retry_time += 1
                        time.sleep(1)
                time.sleep(1)
        tmp_result['posts'] = posts
