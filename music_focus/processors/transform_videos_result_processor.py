from music_focus.processors.processor_base import ProcessorBase


class TransformVideosResultProcessor(ProcessorBase):

    def run(self, workflow_input, tmp_result, workflow_output):
        videos_result = workflow_input['videos']
        music_type = workflow_input['music_type']
        max_cnt = workflow_input['max_cnt']

        json_result = {}
        for cur_music_type, each_videos in videos_result['videos'].items():
            if music_type not in ('all', cur_music_type):
                continue
            json_result[cur_music_type] = []
            for idx, video in enumerate(each_videos):
                if idx >= max_cnt:
                    break
                json_result[cur_music_type].append({
                    "id": video.id,
                    "post_id": video.post_id,
                    "user_id": video.user_id,
                    "user_name": video.user_name,
                    "time": str(video.time),
                    "text": video.text,
                    "cover_path": video.cover_path,
                    "url": video.url,
                    "view_cnt": video.view_cnt,
                    "display_view_cnt": video.display_view_cnt
                })

        workflow_output['result'] = json_result
