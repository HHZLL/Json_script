import os
import json
import re

import numpy as np
import glob
import shutil
from sklearn.model_selection import train_test_split
np.random.seed(41)

#0为背景
classname_to_id = {"maize": 1,}

class Lableme2CoCo:

    def __init__(self):
        self.images = []
        self.annotations = []
        self.categories = []
        self.img_id = 0
        self.ann_id = 0

    def save_coco_json(self, instance, save_path):
        json.dump(instance, open(save_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)  # indent=2 更加美观显示

    # 由json文件构建COCO
    def to_coco(self, json_path_list):
        self._init_categories()
        i = 0
        # print("测试1",self.categories)
        for json_path in json_path_list:    #D:\Code\python\Mask_RCNN-master\samples\my_data\json\89.json
            obj = self.read_jsonfile(json_path) #返回一个json对象
            # print(json_path)
            # print(obj)
            self.images.append(self._image(obj, json_path)) #image h,w,id,file_name
            # print(self.images)
            shapes = obj['shapes']
            # print(shapes)
            for shape in shapes:
                annotation = self._annotation(shape)
                self.annotations.append(annotation)
                self.ann_id += 1
            self.img_id += 1
        instance = {}
        instance['info'] = 'spytensor created'
        instance['license'] = ['license']
        instance['images'] = self.images
        instance['annotations'] = self.annotations
        instance['categories'] = self.categories
        return instance

    # 构建类别
    def _init_categories(self):
        for k, v in classname_to_id.items():
            category = {}
            category['id'] = v
            category['name'] = k
            self.categories.append(category)

    # 构建COCO的image字段
    def _image(self, obj, path):
        image = {}
        from labelme import utils
        img_x = utils.img_b64_to_arr(obj['imageData'])
        h, w = img_x.shape[:-1]
        image['height'] = h
        image['width'] = w
        image['id'] = self.img_id
        image['file_name'] = os.path.basename(path).replace(".json", ".jpg")
        return image

    # 构建COCO的annotation字段
    def _annotation(self, shape):

        label = re.sub("[^A-Za-z]","",shape["label"])

        # label = shape['label']
        points = shape['points']
        annotation = {}
        annotation['id'] = self.ann_id
        annotation['image_id'] = self.img_id
        annotation['category_id'] = int(classname_to_id[label])
        annotation['segmentation'] = [np.asarray(points).flatten().tolist()]
        annotation['bbox'] = self._get_box(points)
        annotation['iscrowd'] = 0
        annotation['area'] = annotation['bbox'][2] * annotation['bbox'][3] #bbox的面积，不是精确面积
        return annotation

    # 读取json文件，返回一个json对象
    def read_jsonfile(self, path):
        with open(path, "r", encoding='utf-8') as f:
            return json.load(f)

    # COCO的格式： [x1,y1,w,h] 对应COCO的bbox格式
    def _get_box(self, points):
        min_x = min_y = np.inf
        max_x = max_y = 0
        for x, y in points:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return [min_x, min_y, max_x - min_x, max_y - min_y]


if __name__ == '__main__':
    labelme_path = r"D:\Code\python\Mask_RCNN-master\samples\my_data\Data"
    saved_coco_path = "./"
    # 创建文件
    if not os.path.exists("%scoco/annotations/"%saved_coco_path):
        os.makedirs("%scoco/annotations/"%saved_coco_path)
    if not os.path.exists("%scoco/images/train2017/"%saved_coco_path):
        os.makedirs("%scoco/images/train2017"%saved_coco_path)
    if not os.path.exists("%scoco/images/val2017/"%saved_coco_path):
        os.makedirs("%scoco/images/val2017"%saved_coco_path)
    # 获取images目录下所有的json文件列表
    json_list_path = glob.glob(labelme_path + "/*.json")
    print(len(json_list_path))
    # 数据划分,这里没有区分val2017和tran2017目录，所有图片都放在images目录下
    train_path, val_path = train_test_split(json_list_path, test_size=0.2)
    print("train_n:", len(train_path), 'val_n:', len(val_path))
    # print(train_path)
    # 把训练集转化为COCO的json格式
    l2c_train = Lableme2CoCo()
    train_instance = l2c_train.to_coco(train_path)
    # print("******",train_instance)

    l2c_train.save_coco_json(train_instance, '%scoco/annotations/instances_train2017.json'%saved_coco_path)
    for file in train_path:     # D:\Code\python\Mask_RCNN-master\samples\my_data\Data\89.json
        # print(file)
        shutil.copy(file.replace("json","png"),"%scoco/images/train2017/"%saved_coco_path)  #copy image(D:\Code\python\Mask_RCNN-master\samples\my_data\Data\89.png) to B
   #将png改为jpg
    pic_list = glob.glob("./coco/images/train2017/"+"*")
    for pic1 in pic_list:
        # if pic1.split(".")[-1] == 'jpg':
        #     break
        # print("1")
        os.rename(pic1,pic1.replace("png","jpg"))

    for file in val_path:
        shutil.copy(file.replace("json","png"),"%scoco/images/val2017/"%saved_coco_path)
        # 将png改为jpg
    pic_list = glob.glob("./coco/images/val2017/" + "*.png")
    for pic1 in pic_list:
        os.rename(pic1, pic1.replace("png", "jpg"))
    # 把验证集转化为COCO的json格式
    l2c_val = Lableme2CoCo()
    val_instance = l2c_val.to_coco(val_path)
    l2c_val.save_coco_json(val_instance, '%scoco/annotations/instances_val2017.json'%saved_coco_path)
    print("success!!")





# #encoding:utf-8
# import os
# import re
# import argparse
# import json
# from labelme import utils
# import numpy as np
# import glob
# import PIL.Image
# #from PIL import Image
# class labelme2coco(object):
#     def __init__(self, labelme_json, save_json_path="./val.json"):
#         self.labelme_json = labelme_json
#         self.save_json_path = save_json_path
#         self.images = []
#         self.categories = []
#         self.annotations = []
#         self.label = []
#         self.annID = 1
#         self.height = 0
#         self.width = 0
#         self.save_json()
#     def data_transfer(self):
#         for num, json_file in enumerate(self.labelme_json):
#             with open(json_file, "r") as fp:
#                 data = json.load(fp)
#
#                 #输出json中key值
#                 # for key in data:
#                 #     print(key)
#                 # print(data["shapes"])
#                 self.images.append(self.image(data, num))
#                 print(self.images)
#                 for shapes in data["shapes"]:
#                     label = re.sub("[^A-Za-z]","",shapes["label"])
#                     if label not in self.label:
#                         self.label.append(label)
#                     # print(self.label)
#                     points = shapes["points"]
#                     self.annotations.append(self.annotation(points, label, num))
#                     self.annID += 1
#         # Sort all text labels so they are in the same order across data splits.
#         self.label.sort()
#         for label in self.label:
#             self.categories.append(self.category(label))
#         for annotation in self.annotations:
#             annotation["category_id"] = self.getcatid(annotation["category_id"])
#     def image(self, data, num):
#         image = {}
#         img = utils.img_b64_to_arr(data["imageData"])
#         height, width = img.shape[:2]
#         img = None
#         image["height"] = height
#         image["width"] = width
#         image["id"] = num
#         image["file_name"] = data["imagePath"].split("/")[-1]
#         self.height = height
#         self.width = width
#         return image
#     def category(self, label):
#         category = {}
#         category["supercategory"] = label[0]
#         category["id"] = len(self.categories)
#         category["name"] = label[0]
#         return category
#     def annotation(self, points, label, num):
#         annotation = {}
#         contour = np.array(points)
#         x = contour[:, 0]
#         y = contour[:, 1]
#         area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
#         annotation["segmentation"] = [list(np.asarray(points).flatten())]
#         annotation["iscrowd"] = 0
#         annotation["area"] = area
#         annotation["image_id"] = num
#         annotation["bbox"] = list(map(float, self.getbbox(points)))
#         annotation["category_id"] = label[0]  # self.getcatid(label)
#         annotation["id"] = self.annID
#         return annotation
#     def getcatid(self, label):
#         for category in self.categories:
#             if label == category["name"]:
#                 return category["id"]
#         print("label: {} not in categories: {}.".format(label, self.categories))
#         exit()
#         return -1
#     def getbbox(self, points):
#         polygons = points
#         mask = self.polygons_to_mask([self.height, self.width], polygons)
#         return self.mask2box(mask)
#     def mask2box(self, mask):
#         index = np.argwhere(mask == 1)
#         rows = index[:, 0]
#         clos = index[:, 1]
#         left_top_r = np.min(rows)  # y
#         left_top_c = np.min(clos)  # x
#         right_bottom_r = np.max(rows)
#         right_bottom_c = np.max(clos)
#         return [
#             left_top_c,
#             left_top_r,
#             right_bottom_c - left_top_c,
#             right_bottom_r - left_top_r,
#         ]
#     def polygons_to_mask(self, img_shape, polygons):
#         mask = np.zeros(img_shape, dtype=np.uint8)
#         mask = PIL.Image.fromarray(mask)
#         xy = list(map(tuple, polygons))
#         PIL.ImageDraw.Draw(mask).polygon(xy=xy, outline=1, fill=1)
#         mask = np.array(mask, dtype=bool)
#         return mask
#     def data2coco(self):
#         data_coco = {}
#         data_coco["images"] = self.images
#         data_coco["categories"] = self.categories
#         data_coco["annotations"] = self.annotations
#         return data_coco
#     def save_json(self):
#         print("save coco1 json")
#         self.data_transfer()
#         self.data_coco = self.data2coco()
#         print(self.save_json_path)
#         os.makedirs(
#             os.path.dirname(os.path.abspath(self.save_json_path)), exist_ok=True
#         )
#         json.dump(self.data_coco, open(self.save_json_path, "w"), indent=4)
# if __name__ == "__main__":
#     import argparse
#     #parser = argparse.ArgumentParser(
#      #   description="labelme annotation to coco1 data json file."
#     #)
#     #parser.add_argument(
#      #   "labelme_images",
#     #    help="Directory to labelme images and annotation json files.",
#     #    type=str,
#     #)
#     #parser.add_argument(
#      #   "--output", help="Output json file path.", default="trainval.json"
#     #)
#     #args = parser.parse_args()
#     #labelme_json = glob.glob(os.path.join(args.labelme_images, "*.json"))
#     filename = os.path.join(r"D:\Code\python\Mask_RCNN-master\samples\my_data\json", "*.json")
#     # print(filename, "first")
#     labelme_json = glob.glob(filename)
#     print("labelme_json",labelme_json,'\n',len(labelme_json))
#     output = "./val.json"
#     labelme2coco(labelme_json, output)
