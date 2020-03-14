import time

from music_focus import logger
from music_focus.servers.server_base import ServerBase
from music_focus.workflows.focus_offline import FocusOffline
from music_focus.workflows.video_offline import VideoOffline
from music_focus.workflows.weibo_offline import WeiboOffline


class OfflineServer(ServerBase):

    def __init__(self, interval=30 * 60):
        self._interval = interval
        self._workflows = [
            WeiboOffline(),
            VideoOffline(),
            FocusOffline(),
        ]
        self._workflow_inputs = [
            {'result_type': 'posts'},
            {'result_type': 'videos'},
            {'result_type': 'focuses'}
        ]

    def start(self):
        while True:
            for i in range(len(self._workflows)):
                workflow, workflow_input = self._workflows[i], self._workflow_inputs[i]
                try:
                    logger.info('start to run workflow: {}'.format(workflow.__class__.__name__))
                    result = workflow.run(workflow_input)
                    logger.info('workflow: {} run finish, result: {}'.format(workflow.__class__.__name__, result))
                except Exception as e:
                    logger.exception('error for workflow: {}, {}'.format(workflow.__class__.__name__, e))
            time.sleep(self._interval)
