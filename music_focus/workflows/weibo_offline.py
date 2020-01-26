from music_focus.processors.compute_posts_hot_processor import ComputePostsHotProcessor
from music_focus.processors.fetch_posts_processor import FetchPostsProcessor
from music_focus.processors.rank_processor import RankProcessor
from music_focus.processors.save_result_processor import SaveResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class WeiboOffline(WorkflowBase):

    def __init__(self):
        super(WeiboOffline, self).__init__()

    def load_processors(self):
        self._processors = [
            FetchPostsProcessor(),
            ComputePostsHotProcessor(),
            RankProcessor(),
            SaveResultProcessor()
        ]
