import os
import shutil


def empty_dir(dir_name):
    for fname in os.listdir(dir_name):
        fpath = '{}/{}'.format(dir_name, fname)
        try:
            if os.path.isdir(fpath):
                shutil.rmtree(fpath)
            else:
                os.remove(fpath)
        except FileNotFoundError:  # 防止多进程同时删除时可能的报错
            pass
