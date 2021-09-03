#为了适应模型内部默认的路径格式，需要对label.png进行简单的重命名
#比如你的json文件夹叫1_json，那这个png的图就应该改成1.png
import os
for root, dirs, names in os.walk(r'D:\Data\test'):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        # print(dr)
        file = os.path.join(file_dir, 'img.png')
        new_name = dr.split('_json')[0] + '.png'    #m_1.json m_1.jpg
        new_file_name = os.path.join(file_dir, new_name)
        # print(file,new_file_name)
        os.rename(file, new_file_name)


#
# import os
# for root, dirs, names in os.walk(r"D:\Code\python\Mask_RCNN-master\samples\my_data\labelme_json"):   # 改成你自己的json文件夹所在的目录
#     # print(root)
#     for dir in dirs:
#         old_name = os.path.join(root, dir)
#         # print(old_name)
#         # print(file_dir)
#         # file = os.path.join(file_dir, 'label.png')
#         # print(file)
#         file = os.path.join(old_name, 'r_7.png')
#         new_name = dir.split('_')[0] + '.png'
#         # print(old_name)
#         print(new_name)
#         # new_file_name = os.path.join(file_dir, new_name)
#         # os.rename(old_name, new_name)