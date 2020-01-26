from music_focus.processors.load_result_processor import LoadResultProcessor
from music_focus.processors.transform_focuses_result_processor import TransformFocusesResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class FocusOnline(WorkflowBase):

    def __init__(self):
        super(FocusOnline, self).__init__()

    def load_processors(self):
        self._processors = [
            LoadResultProcessor(),
            TransformFocusesResultProcessor()
        ]
