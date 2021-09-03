
## 删除json中指定label的字典元素，json文件可以看作字典，其中每个元素的值又有不同的类型
import glob
import json
img_list = glob.glob(r'D:\Data\test1\\' + "*" + '.json')
# img_list = [r'D:\Data\test1\w_11.json']
print(img_list)
# 打开json文件
for i in range(len(img_list)):
    # print(img_list[i])
    f = open(img_list[i], encoding='utf-8')
    # 读取json
    setting = json.load(f)
    a = setting['shapes']   #读取key为shapes的键值对
    for i2 in a[::-1]:  # 逆向读取！！！，否则会使用remove和del都会错误
        # print(i2)
        if i2['label'] == "wheat":
            a.remove(i2)
            print("执行删除wheat")
        elif i2['label'] == "wheat1":
            a.remove(i2)
            print("执行删除wheat1")
    # 将修改后的json写入文件
    string = json.dumps(setting)
    with open(img_list[i], 'w', encoding='utf-8') as f:
        f.write(string)
        f.close()
