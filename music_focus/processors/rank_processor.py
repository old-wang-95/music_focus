from music_focus.processors.processor_base import ProcessorBase


class RankProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        scores = tmp_result['scores']
        if 'posts' in tmp_result:
            posts = tmp_result['posts']
            for music_type, each_posts in posts.items():
                posts[music_type], scores[music_type] = self._rank(each_posts, scores[music_type])
        elif 'focuses' in tmp_result:
            focuses = tmp_result['focuses']
            for music_type, each_focuses in focuses.items():
                focuses[music_type], scores[music_type] = self._rank(focuses, scores[music_type])

    @staticmethod
    def _rank(items, scores):
        """
        根据scores, 对items进行排序

        :param items: posts or focuses
        :type items: list
        :param scores:
        :type scores: list
        :return:
        """
        new_scores, new_items = [], []
        for score, item in sorted(zip(scores, items), key=lambda t: t[0], reverse=True):
            new_items.append(item)
            new_scores.append(score)
        return new_items, new_scores
