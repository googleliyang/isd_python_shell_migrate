import os
from distutils.dir_util import copy_tree
from shutil import copyfile


class Helper:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def ready_file(self):
        copyfile('./packages/preload.vue',  os.path.join(self.dir_path, 'src', 'views', 'preload.vue'))
        copy_tree('./packages/hackAsd',  os.path.join(self.dir_path, 'src', 'utils/'))

    def rm_token_of_headers(self):
        res = os.system('./filter.sh')
        print(res)

    def update_http(self):
        # 更新http 加签代码
        pass
