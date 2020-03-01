import os
import time
from datetime import datetime
from datetime import timedelta

from music_focus import logger
from music_focus.api import chrome_api
from music_focus.api import weibo_api
from music_focus.api.weibo_api import USER_POSTS_URL_FORMATTER, POSTS_CSS_SELECTOR
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class FetchPostsProcessor(ProcessorBase):

    def __init__(self, before_day=3):
        self._before_data = before_day

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
                                chrome_api.find_elements_in_page(USER_POSTS_URL_FORMATTER.format(user.id),
                                                                 POSTS_CSS_SELECTOR)):
                            user_post = user_posts[i]
                            if user_post.time <= datetime.now() - timedelta(days=self._before_data):  # 过滤旧微博
                                continue
                            images_dir = 'data/weibo_images'
                            if not os.path.exists(images_dir):
                                os.mkdir(images_dir)
                            image_path = '{}/{}.png'.format(images_dir, user_post.id)
                            user_post.image_path = '{}.png'.format(user_post.id)
                            chrome_api.screenshot(post_element, image_path)
                            new_user_posts.append(user_post)
                        posts[music_type].extend(new_user_posts)
                        logger.info('fetch user: {} data success'.format(user_id))
                        break
                    except Exception as e:
                        logger.exception('fetch user: {} data error! {}'.format(user_id, e))
                        retry_time += 1
                        time.sleep(1)
                time.sleep(1)
        tmp_result['posts'] = posts
