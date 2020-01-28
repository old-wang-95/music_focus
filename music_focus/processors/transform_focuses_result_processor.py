from music_focus.processors.processor_base import ProcessorBase


class TransformFocusesResultProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        focuses_result = workflow_input['focuses']
        json_result = {}
        for music_type, each_focuses in focuses_result['focuses'].items():
            json_result[music_type] = []
            for idx, each_focus in enumerate(each_focuses):
                json_result[music_type].append({
                    'title': each_focus.title,
                    'description': each_focus.description,
                    'recent_read': each_focus.recent_read,
                    'read_cnt': each_focus.read_cnt,
                    'discuss_cnt': each_focus.discuss_cnt,
                    'member_cnt': each_focus.member_cnt,
                    'link': each_focus.link,
                    'score': focuses_result['scores'][music_type][idx]
                })
        workflow_output['result'] = json_result
