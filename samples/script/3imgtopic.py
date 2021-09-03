#将生成文件夹json中的原图存入cs2_mask文件夹中

import os
from shutil import copyfile
for root, dirs, names in os.walk(r'D:\Data\test'):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        # print(dr)
        ''' file = os.path.join(file_dir,'r_7.png')
        print(file)'''
       
        new_name1 = dr.split('_json')[0] + '.png'
        new_name = 'img.png'
        new_file_name = os.path.join(file_dir, new_name)    #源文件路径
        print(new_file_name)
        
        tar_root = r'D:\Data\pic'      # 目标路径
        tar_file = os.path.join(tar_root, new_name1)    #目标文件名
        # print(tar_file)
        copyfile(new_file_name, tar_file)