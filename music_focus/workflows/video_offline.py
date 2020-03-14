from music_focus.processors.fetch_videos_processor import FetchVideosProcessor
from music_focus.processors.rank_processor import RankProcessor
from music_focus.processors.save_result_processor import SaveResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class VideoOffline(WorkflowBase):

    def __init__(self):
        super(VideoOffline, self).__init__()

    def load_processors(self):
        self._processors = [
            FetchVideosProcessor(),
            RankProcessor(),
            SaveResultProcessor()
        ]
