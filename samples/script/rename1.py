#将文件夹中第一个图片名字命名为文件夹前缀
# import os
# for root, dirs, names in os.walk(r'script/coco/images/train2017'):   # 改成你自己的json文件夹所在的目录
#
#     for dr in dirs:
#         file_dir = os.path.join(root, dr)
#        # print(file_dir)
#        # print(dr)
#         b = os.listdir(file_dir)
#         #print(b)
#         new_name = dr.split('_')[0] + '.png'
#         img_name= b[0].split('.')[0]+ '.json.png'
#         file = os.path.join(file_dir, img_name)
#         # # print(file)
#         # new_name = dr.split('_')[0] + '.png'
#         new_file_name = os.path.join(file_dir, new_name)
#         print(new_file_name)
#         os.rename(file, new_file_name)


import os

for root, dirs, names in os.walk(r'D:\Data\wheat'):  # 改成你自己的json文件夹所在的目录
    i = 1
    for dr in names:
        # print(dr)
        old_name = os.path.join(root, dr)
        new_name = os.path.join(root,"r_" + str(i) + ".json")
        i+=1
        print(new_name)
        os.rename(old_name, new_name)

