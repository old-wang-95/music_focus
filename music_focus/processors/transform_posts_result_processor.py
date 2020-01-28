from music_focus.processors.processor_base import ProcessorBase


class TransformPostsResultProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        posts_result = workflow_input['posts']
        json_result = {}
        for music_type, each_posts in posts_result['posts'].items():
            json_result[music_type] = []
            for idx, each_post in enumerate(each_posts):
                json_result[music_type].append({
                    'id': each_post.id,
                    'user_id': each_post.user_id,
                    'user_name': each_post.user_name,
                    'time': str(each_post.time),
                    'content': each_post.content,
                    'share_cnt': each_post.share_cnt,
                    'comment_cnt': each_post.comment_cnt,
                    'like_cnt': each_post.like_cnt,
                    'score': posts_result['scores'][music_type][idx]
                })
        workflow_output['result'] = json_result
