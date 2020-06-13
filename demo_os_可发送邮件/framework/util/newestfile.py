import os


def newst_file(test_dir):
    #列举test_dir目录下的所有文件（名），结果以列表形式返回
    lists = os.listdir(test_dir)
    #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以
    #最后lists元素，按文件修改时间大小从小到大排序
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\'))
    #获取最新文件的绝对路径，列表中最后的一个值，文件夹+文件名
    file_path = os.path.join(test_dir, lists[-1])

    return file_path, lists[-1]


if __name__ == '__main__':
    print(newst_file('..\\report'))