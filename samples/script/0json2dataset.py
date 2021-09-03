#将json文件转换成 文件夹（包含5个文件），下一步对文件夹进行重命名
import os
import glob
# files=os.listdir(r'D:\Camera Roll\Crop classification\ML\order')
# name = os.path.join(D:\Camera Roll\Crop classification\ML\order,files[1])
# print(name)
files=glob.glob('D:\Data\wheat'+'\*.json')
# files.remove('0json2dataset.py')   # 删除这个py文件本身
# print(files)
for i in range(len(files)):
    os.system('labelme_json_to_dataset '+files[i])
