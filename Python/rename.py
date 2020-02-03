# -*- coding: UTF-8 -*-

import os

# 让用户输入路径名和文件名
path = input("输入目录的绝对路径名：")
keyword = input("输入需要删除的文字（以重命名文件）：")

# 合成文件路径
path = os.path.join(path)

# 删除匹配关键字，返回新路径（由新文件名构成）
def delKeyword(keyword, name, path):
    newName = name.replace(keyword, '')
    newPath = os.path.join(path, newName)
    return newPath

# 遍历获取目录(包括子目录)下所有文件和文件夹
# 生成的列表顺序是从子目录到根目录（从底至上）
for root, dirs, files in os.walk(path, topdown=False):
    # 重命名文件
    for fileName in files:
        if keyword in fileName:
            oldPath = os.path.join(root, fileName)
            newPath = delKeyword(keyword, fileName, root)
            os.rename(oldPath, newPath)

    # 重命名目录
    for dirName in dirs:
        if keyword in dirName:
            oldPath = os.path.join(root, dirName)
            newPath = delKeyword(keyword, dirName, root)
            os.rename(oldPath, newPath)


