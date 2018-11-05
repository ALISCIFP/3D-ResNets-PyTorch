import os
import shutil
import re
path='/Users/perla/Desktop/before 3'#原文件路径
path1='/Users/perla/Desktop/after'#分类文件
#列出文档
file_list = os.listdir(path)
file_list=file_list[1:]#把mac电脑文件中.DS_Store除掉
id=[]#存储文件名中的id
for i in range(len(file_list)):
    id.append(file_list[i].split('_')[1])
id=set(id)#取出唯一的id值，用于建立文件夹
sort_folder_number = list(id)#把集合id转化为列表类型
for number in sort_folder_number:
    new_folder_path = os.path.join(path1,'%s'%number)#新文件夹路径
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
#提取出文档名称内的id，并根据id决定将发往指定文件夹
for i in range(len(file_list)):
    old_file_path = os.path.join(path,file_list[i])
    fid=file_list[i].split('_')[1]
    new_file_path = os.path.join(path1,'%s'%(fid),file_list[i])
    shutil.move(old_file_path,new_file_path)
