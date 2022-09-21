import os.path


def ui2py():
    """
    将文件夹中所有ui文件转换成py文件
    :return:
    """
    path = os.getcwd()
    uiFiles = [_file for _file in os.listdir() if ".ui" in _file]
    pyFiles = [_file.split(".")[0] + ".py" for _file in uiFiles]
    for uiFile, pyFile in zip(uiFiles, pyFiles):
        cmd = r"D:\Install\Anaconda3\envs\pyqt\Scripts\pyuic5.exe {uiFile} -o {pyFile}".format(
            uiFile=os.path.join(path, uiFile), pyFile=os.path.join(path, pyFile))
        if os.system(cmd) == 0:
            print("{uiFile}=>{pyFile}成功！".format(uiFile=uiFile, pyFile=pyFile))
        else:
            print("{uiFile}=>{pyFile}失败！".format(uiFile=uiFile, pyFile=pyFile))


if __name__ == '__main__':
    ui2py()
