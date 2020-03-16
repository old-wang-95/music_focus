from music_focus.processors.processor_base import ProcessorBase


class TransformPostsResultProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        posts_result = workflow_input['posts']
        music_type = workflow_input['music_type']
        max_cnt = workflow_input['max_cnt']

        json_result = {}
        for cur_music_type, each_posts in posts_result['posts'].items():
            if music_type not in ('all', cur_music_type):
                continue
            json_result[cur_music_type] = []
            for idx, each_post in enumerate(each_posts):
                if idx >= max_cnt:
                    break
                json_result[cur_music_type].append({
                    'id': each_post.id,
                    'user_id': each_post.user_id,
                    'user_name': each_post.user_name,
                    'time': str(each_post.time),
                    'content': each_post.content,
                    'share_cnt': each_post.share_cnt,
                    'comment_cnt': each_post.comment_cnt,
                    'like_cnt': each_post.like_cnt,
                    'link': each_post.link,
                    'score': posts_result['scores'][cur_music_type][idx],
                    'image_path': each_post.image_path
                })

        workflow_output['result'] = json_result
