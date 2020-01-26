from music_focus.processors.processor_base import ProcessorBase


class RankProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        scores = tmp_result['scores']
        if 'posts' in tmp_result:
            posts = tmp_result['posts']
            for music_type, each_posts in posts.items():
                each_sorted_posts = [post for _, post in
                                     sorted(zip(scores[music_type], each_posts), key=lambda t: t[0], reverse=True)]
                posts[music_type] = each_sorted_posts
        elif 'focuses' in tmp_result:
            focuses = tmp_result['focuses']
            for music_type, each_focuses in focuses.items():
                each_sorted_focuses = [focus for _, focus in
                                       sorted(zip(scores[music_type], each_focuses), key=lambda t: t[0], reverse=True)]
                focuses[music_type] = each_sorted_focuses
