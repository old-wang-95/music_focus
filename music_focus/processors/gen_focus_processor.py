import time

from music_focus import logger
from music_focus.api import weibo_api
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class GenFocusProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        focuses = {}
        for music_type, users in users_config.items():
            focuses[music_type] = []
            for user_id, _ in users:
                retry_time = 0
                while retry_time <= 3:
                    if retry_time > 0:
                        logger.info('start to retry, current retry time is: {}'.format(retry_time))
                    try:
                        use_cache = False if retry_time else True
                        user = weibo_api.get_user_info(user_id, use_cache)
                        user_focuses = weibo_api.get_focuses_by_user(user, use_cache)
                        focuses[music_type].extend(user_focuses)
                        logger.info('fetch user: {} data success'.format(user_id))
                        break
                    except Exception as e:
                        logger.exception('fetch user: {} data error! {}'.format(user_id, e))
                        retry_time += 1
                time.sleep(1)
            # distinct focuses
            focuses[music_type] = list({focus.title: focus for focus in focuses[music_type]}.values())
        tmp_result['focuses'] = focuses
