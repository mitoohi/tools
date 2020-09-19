import os
import sys


# 暴力破解压缩文件
def hack_password(filename):
    ed = '} '
    start = '7z x ' + filename + ' -p{'
    for i in range(1000, 1250):
        cmd = start + str(i) + ed
        print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    file = sys.argv[1]
    hack_password(file)
