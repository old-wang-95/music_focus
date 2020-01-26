from music_focus.processors.fetch_posts_processor import FetchPostsProcessor
from music_focus.processors.gen_focus_processor import GenFocusProcessor
from music_focus.processors.rank_processor import RankProcessor
from music_focus.processors.save_result_processor import SaveResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class FocusOffline(WorkflowBase):

    def __init__(self):
        super(FocusOffline, self).__init__()

    def load_processors(self):
        self._processors = [
            FetchPostsProcessor(),
            GenFocusProcessor(),
            RankProcessor(),
            SaveResultProcessor()
        ]
