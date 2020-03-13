import os
import shutil


def empty_dir(dir_name):
    for fname in os.listdir(dir_name):
        fpath = '{}/{}'.format(dir_name, fname)
        if os.path.isdir(fpath):
            shutil.rmtree(fpath)
        else:
            os.remove(fpath)
