import os
import sys

from music_focus.servers.offline_server import OfflineServer
from music_focus.servers.online_server import OnlineServer


def start_offline():
    interval = 30 * 60
    if len(sys.argv) >= 2:
        interval = sys.argv[1]
    server = OfflineServer(interval)
    server.start()


def start_online():
    address = '0.0.0.0'
    port = 8000
    process_num = 2
    if len(sys.argv) >= 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        process_num = int(sys.argv[3])
    server = OnlineServer(address, port, process_num)
    server.start()


def start():
    assert 'ROLE' in os.environ and os.environ['ROLE'].lower() in ('online', 'offline'), \
        'You must set env ROLE in (online, offline)!'
    if os.environ['ROLE'].lower() == 'online':
        start_online()
    else:
        start_offline()


if __name__ == '__main__':
    start()
