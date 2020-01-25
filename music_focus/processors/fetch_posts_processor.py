from datetime import datetime
from datetime import timedelta

from music_focus import logger
from music_focus.api import weibo_api
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class FetchPostsProcessor(ProcessorBase):

    def __init__(self, before_day=2):
        self._before_data = before_day

    def run(self, workflow_input, tmp_result, workflow_output):
        new_posts = []
        for music_type, users in users_config.items():
            for user_id, _ in users:
                try:
                    user = weibo_api.get_user_info(user_id)
                    posts = [post for post in weibo_api.get_posts_by_user(user) if
                             post.time > datetime.now() - timedelta(days=2)]
                    new_posts.extend(posts)
                except Exception as e:
                    logger.exception('fetch user: {} data error! {}'.format(user_id, e))
        tmp_result['posts'] = new_posts
