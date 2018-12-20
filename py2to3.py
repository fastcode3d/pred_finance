import os


# 定义一个处理方法
def Python2toPython3(dirname, p2to3FileName):
    if os.path.exists(dirname):
        for dirpath, dirnames, filenames in os.walk(dirname):
            for filename in filenames:
                if filename.endswith('.py'):
                    fileFullName = os.path.join(dirpath, filename)
                    print(('Processing File:', fileFullName))
                    # -w -n效果是修改但不留备份文件 .bak是备份的原文件
                    # -f 给出明确的修复集
                    pycode2to3 = ("python " + p2to3FileName + " -w " +
                                  fileFullName)
                    print((os.popen(pycode2to3, 'r').read()))


# dirname 需要转换的文件目录
dirname = os.getcwd()

# p2to3FileName 本机Python安装目录下的2to3.py的路径，2to3.py是python自带的工具
p2to3FileName = (r'H:\python3.6.5\Tools\scripts\2to3.py')

Python2toPython3(dirname, p2to3FileName)
