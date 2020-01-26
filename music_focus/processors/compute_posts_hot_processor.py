from music_focus.processors.processor_base import ProcessorBase


class ComputePostsHotProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        posts = tmp_result['posts']
        scores = {}
        for music_type, each_posts in posts.items():
            scores[music_type] = []
            for post in each_posts:
                score = 1 * post.like_cnt + 5 * post.comment_cnt + 10 * post.share_cnt
                scores[music_type].append(score)
        tmp_result['scores'] = scores
