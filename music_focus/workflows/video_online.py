from music_focus.processors.load_result_processor import LoadResultProcessor
from music_focus.processors.refresh_video_url_processor import RefreshVideoUrlProcessor
from music_focus.processors.transform_videos_result_processor import TransformVideosResultProcessor
from music_focus.workflows.workflow_base import WorkflowBase


class VideoOnline(WorkflowBase):

    def __init__(self):
        super(VideoOnline, self).__init__()

    def load_processors(self):
        self._processors = [
            LoadResultProcessor(),
            TransformVideosResultProcessor(),
            RefreshVideoUrlProcessor(),
        ]
