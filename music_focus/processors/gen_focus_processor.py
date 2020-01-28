import time

from music_focus import logger
from music_focus.api import weibo_api
from music_focus.conf.focus_blacklist import config as blacklist_config
from music_focus.conf.users import config as users_config
from music_focus.processors.processor_base import ProcessorBase


class GenFocusProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        focuses = {}

        # get focuses from weibo api
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
            # distinct, black_list, merge related_users
            black_list = blacklist_config['all'] + blacklist_config[music_type]
            tmp_dict = {}
            for focus in focuses[music_type]:
                if focus.title in black_list:
                    continue
                if focus.title not in tmp_dict:
                    tmp_dict[focus.title] = focus
                else:
                    tmp_dict[focus.title].related_users.extend(focus.related_users)
                # distinct related_users
                tmp_dict[focus.title].related_users = list(set(tmp_dict[focus.title].related_users))

            focuses[music_type] = list(tmp_dict.values())

        # score
        scores = {
            music_type: [f.recent_read for f in each_focuses] for music_type, each_focuses in focuses.items()
        }

        tmp_result['focuses'] = focuses
        tmp_result['scores'] = scores
