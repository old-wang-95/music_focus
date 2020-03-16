from music_focus.conf.focus_blacklist import config  as blacklist
from music_focus.processors.processor_base import ProcessorBase


class TransformFocusesResultProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        focuses_result = workflow_input['focuses']
        music_type = workflow_input['music_type']
        max_cnt = workflow_input['max_cnt']

        json_result = {}
        for cur_music_type, each_focuses in focuses_result['focuses'].items():
            if music_type not in ('all', cur_music_type):
                continue
            cur_black_list = blacklist['all'] + blacklist[cur_music_type]
            json_result[cur_music_type] = []
            for idx, each_focus in enumerate(each_focuses):
                if idx >= max_cnt:
                    break
                if each_focus.title in cur_black_list:
                    continue
                json_result[cur_music_type].append({
                    'title': each_focus.title,
                    'description': each_focus.description,
                    'recent_read': each_focus.recent_read,
                    'read_cnt': each_focus.read_cnt,
                    'discuss_cnt': each_focus.discuss_cnt,
                    'member_cnt': each_focus.member_cnt,
                    'link': each_focus.link,
                    'related_users': each_focus.related_users,
                    'score': focuses_result['scores'][cur_music_type][idx]
                })

        workflow_output['result'] = json_result
