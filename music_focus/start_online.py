import sys

from music_focus.servers.online_server import OnlineServer


def start():
    address = '0.0.0.0'
    port = 8000
    process_num = 2
    if len(sys.argv) >= 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        process_num = int(sys.argv[3])
    server = OnlineServer(address, port, process_num)
    server.start()


if __name__ == '__main__':
    start()
