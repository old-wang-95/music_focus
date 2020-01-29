import sys

from music_focus.servers.offline_server import OfflineServer


def start():
    interval = 30 * 60
    if len(sys.argv) >= 2:
        interval = sys.argv[1]
    server = OfflineServer(interval)
    server.start()


if __name__ == '__main__':
    start()
