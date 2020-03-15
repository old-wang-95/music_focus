from music_focus import logger
from music_focus.api import weibo_api
from music_focus.processors.processor_base import ProcessorBase


class RefreshVideoUrlProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        videos_result = workflow_input['videos']
        for music_type, each_videos in videos_result['videos'].items():
            for video in each_videos:
                try:
                    video.url = weibo_api.get_video_url_by_post(video.post_id)
                except Exception as e:
                    logger.exception(
                        'get video_url of video: {} of post: {} error! {}'.format(video.id, video.post_id, e))
