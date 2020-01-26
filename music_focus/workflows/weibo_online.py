from music_focus.processors.load_result_processor import LoadResultProcessor
from music_focus.processors.transform_posts_result_processor import TransformPostsResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class WeiboOnline(WorkflowBase):

    def __init__(self):
        super(WeiboOnline, self).__init__()

    def load_processors(self):
        self._processors = [
            LoadResultProcessor(),
            TransformPostsResultProcessor()
        ]
