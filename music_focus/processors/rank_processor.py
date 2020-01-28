from music_focus.processors.processor_base import ProcessorBase


class RankProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        rtype = workflow_input['result_type']
        scores = tmp_result['scores']
        for music_type, each_posts in tmp_result[rtype].items():
            tmp_result[rtype][music_type], scores[music_type] = self._rank(each_posts, scores[music_type])

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
