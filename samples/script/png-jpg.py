# 转换png->jpg
import os
for root, dirs, names in os.walk(r"D:\Code\python\Mask_RCNN-master\samples\my_data\script\coco\images\train2017"):
    # print(names)
    for dir in names:
        old_name = os.path.join(root, dir)
        new_name = os.path.join(root, dir.split(".")[0]+'.jpg')
        # print(new_name)
        os.rename(old_name,new_name)
    print('转换成功')