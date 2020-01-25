from music_focus.processors.processor_base import ProcessorBase


class RankProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        scores = tmp_result['scores']
        if 'posts' in tmp_result:
            posts = tmp_result['posts']
            sorted_posts = [post for _, post in sorted(zip(scores, posts), reverse=True)]
            tmp_result['posts'] = sorted_posts
        elif 'focuses' in tmp_result:
            focuses = tmp_result['focuses']
            sorted_focuses = [post for _, post in sorted(zip(scores, focuses), reverse=True)]
            tmp_result['focuses'] = sorted_focuses
