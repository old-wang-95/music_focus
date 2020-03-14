import time
from datetime import datetime, timedelta

from music_focus import logger
from music_focus.api import weibo_api
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class FetchVideosProcessor(ProcessorBase):

    def __init__(self, before_day=5):
        self._before_data = before_day

    def run(self, workflow_input, tmp_result, workflow_output):
        videos = {}
        scores = {}
        for music_type, users in users_config.items():
            videos[music_type] = []
            scores[music_type] = []
            tmp_set = set()  # video去重
            for user_id, _ in users:
                retry_time = 0
                while retry_time <= 3:
                    if retry_time > 0:
                        logger.info('start to retry, current retry time is: {}'.format(retry_time))
                    try:
                        use_cache = False if retry_time else True
                        user = weibo_api.get_user_info(user_id, use_cache)
                        user_videos = weibo_api.get_videos_by_user(user, use_cache)
                        for video in user_videos:
                            if video.id in tmp_set or video.time <= datetime.now() - timedelta(days=self._before_data):
                                continue
                            videos[music_type].append(video)
                            scores[music_type].append(video.view_cnt)
                            tmp_set.add(video.id)
                        logger.info('fetch user: {} data success'.format(user_id))
                        break
                    except Exception as e:
                        logger.exception('fetch user: {} data error! {}'.format(user_id, e))
                        retry_time += 1
                        time.sleep(1)
                time.sleep(1)
        tmp_result['videos'] = videos
        tmp_result['scores'] = scores
