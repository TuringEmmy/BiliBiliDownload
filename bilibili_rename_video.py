#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/19-06:11
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : csy_lgy
# @File     : bilibili_rename_video.py
# @Project  : 1
import json
import os
import re
import shutil
from datetime import datetime

readme = []


def get_rename_video_name(path):
    # print(path)
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        # print(data)
        json_obbject = json.loads(data)
        return json_obbject.get("PartName") + ".mp4", data


def rename_video_cp_new_folder():
    fold_list = os.listdir("./data")
    # print(fold_list)
    fold_path = os.path.abspath("./data")
    if not os.path.exists("video"):
        os.mkdir("video")
    video_fold_list = [fold_path + "/" + video_fold for video_fold in fold_list]

    for video_fold in video_fold_list:
        print(video_fold)
        for item in os.listdir(video_fold):
            try:
                info = re.search("\d+.info", item)
                # print(item)
                # infp_name = info.string.split(".")[0]
                # print(info.string)

                info_path = os.path.abspath(video_fold + '/' + info.string)
                # print(info_path)
                video_rename, data = get_rename_video_name(info_path)
                # print(video_rename)
                readme.append(video_rename.split('.')[0] + '.' + video_rename.split('.')[1] + "\n")
                # video = re.search("video.mp4", item)
                # audio = re.search("audio1.mp4", item)

                # os.rename(info_path, "txt.ttx")

                # print(info.string)
                # copy(audio, os.curdir() + "/video/" + audio)
                # print(video.string)
                shutil.copyfile(video_fold + "/video.mp4",
                                "video/" + video_rename)
                # print(video_fold + "/video.mp4")
                # print(os.getcwd() + "/video/" + video_name + ".mp4")
            except:
                pass
    # break
    return data


if __name__ == '__main__':
    data = rename_video_cp_new_folder()
    # print(''.join(readme))
    description = ''.join(readme)
    # with open()
    # print(data, type(json.loads(data)))
    title = json.loads(data)['Title']
    edit_time = datetime.now()
    print(edit_time)

    read = "#### " + title + '\n' + description + '\n' + '编辑时间:' + str(edit_time).split('.')[
        0] + '\n' + "联系方式:yonglonggeng@163.com" + '\n'
    # print(read)
    with open("video/readme.md", 'w', encoding='utf-8') as f:
        f.write(read)
