import os
from distutils.dir_util import copy_tree
from shutil import copyfile
import subprocess

class Helper:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def ready_file(self):
        copyfile('./packages/preload.vue',  os.path.join(self.dir_path, 'src', 'views', 'preload.vue'))
        copy_tree('./packages/hackAsd',  os.path.join(self.dir_path, 'src', 'utils/'))

    @staticmethod
    def rm_token_of_headers():
        res = os.system('./filter.sh')
        print(res)

    def update_http(self):
        # 更新http 加签代码
        pass

    def create_git_branch(self):
        sub = subprocess.Popen("git branch -a", shell=True, stdout=subprocess.PIPE, cwd=self.dir_path)
        sub.wait()
        res = sub.stdout.read()
        res_str = str(res, encoding="utf-8")
        arr = res_str.split('\n')
        for i in arr:
            if not i.find('->') > -1 and not i.find('*') > -1 and not i.find('master') > -1 and i != '':
                branch_name = i.split('/')[-1]
                print(branch_name)
                title = branch_name.split('-')[1]
                print(title)
                asd_branch_name = 'feature-asd-%s-dev1.0.0' % title
                # print('new branch name %s' % asd_branch_name)
                g_res = subprocess.Popen('git checkout %s && git pull && git checkout -b %s' % (branch_name, asd_branch_name), shell=True, stdout=subprocess.PIPE, cwd=self.dir_path)
                g_res.wait()
                print(g_res.stdout.read())
        pass


if __name__ == '__main__':
    helper = Helper('/Users/yangli/Development/zibo-work/微警务/Micro-policing-h5')
    helper.create_git_branch()

