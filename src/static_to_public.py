from os.path import exists, isdir, join, isfile
from os import listdir, mkdir
from shutil import copy, rmtree

def copy_to_new_dir(src, dst, list_dir = [], initial = True):
    if not initial and list_dir == []:
        return
    if list_dir == [] and initial:
        if not exists(src) or not exists(dst):
            print(src)
            print(dst)
            raise Exception("Invalid src directory" if not exists(src) else "Invalid dst directory")
        list_dir = listdir(src)
        rmtree(dst)
        mkdir(dst)
    path = join(src, list_dir[0])
    if isfile(path):
        copy(path, dst)
    elif isdir(path):
        dir_path = join(dst, list_dir[0])
        mkdir(join(dir_path))
        dirs = listdir(path)
        if dirs != []:
            copy(join(path, dirs[0]), dir_path)
            copy_to_new_dir(path, dir_path, dirs[1:], False)
    copy_to_new_dir(src, dst, list_dir[1:], False)
