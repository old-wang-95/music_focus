import json
import time

import tornado.httpserver
import tornado.ioloop
import tornado.web

from music_focus import logger
from music_focus.servers.server_base import ServerBase
from music_focus.workflows.focus_online import FocusOnline
from music_focus.workflows.weibo_online import WeiboOnline


class Handler(tornado.web.RequestHandler):

    def initialize(self, workflow, workflow_input):
        self.workflow = workflow
        self.workflow_input = workflow_input

    def get(self, *args, **kwargs):
        result = {
            'status': 'OK'
        }
        init_time = time.time()
        try:
            logger.info('start to run workflow: {}'.format(self.workflow.__class__.__name__))
            result['result'] = self.workflow.run(self.workflow_input)
            logger.info('workflow: {} run finish'.format(self.workflow.__class__.__name__))
        except Exception as e:
            logger.exception('error to run workflow: {}, {}'.format(self.workflow.__class__.__name__, e))
            result['status'] = 'ERROR'
        result_str = json.dumps(result, ensure_ascii=False, indent=2)
        logger.info('result: {}, cost time: {}s'.format(result_str, time.time() - init_time))
        self.write(result_str)


class OnlineServer(ServerBase):

    def __init__(self, address='0.0.0.0', port=8000, process_num=2):
        self._address = address
        self._port = port
        self._process_num = process_num

    def start(self):
        app = tornado.web.Application([
            ('/api/v1/posts', Handler, {'workflow': WeiboOnline(), 'workflow_input': {'result_type': 'posts'}}),
            ('/api/v1/focuses', Handler, {'workflow': FocusOnline(), 'workflow_input': {'result_type': 'focuses'}})
        ])
        server = tornado.httpserver.HTTPServer(app)
        server.bind(self._port, address=self._address)
        server.start(self._process_num)
        logger.info('online server start with address: {}, port: {}, process_num: {}'.format(self._address, self._port,
                                                                                             self._process_num))
        tornado.ioloop.IOLoop.current().start()
