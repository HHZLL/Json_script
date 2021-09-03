# 检测json文件是否标注错误，检测polygon格式！！！
# 检查标签命名是否规范，如soya写成saya

import os
import json
import glob
import re
# path = r'D:\Data\wheat\\'
path = r'D:\Data\wheat\\'

json_path =  glob.glob(path+"*.json")
# print(json_path)
for i in range(len(json_path)):
    # print(json_path[i])
    #读取json 文件！！
    f = open(json_path[i],encoding='utf-8')
    jsoncontent = json.load(f)
    #遍历shapes，查看shape——type是否为多边形
    for i1 in range(len(jsoncontent['shapes'])):
        # print(jsoncontent['shapes'][i1]['shape_type'])
        if(jsoncontent['shapes'][i1]['shape_type'] != 'polygon'):
            print("标注错误！！",json_path[i])
        elif (re.sub(u"([^\u0041-\u007a])", "", jsoncontent['shapes'][i1]['label']) not in ['soya', 'wheat']):
            print("标签错误！！", json_path[i], '\t', '标签：', jsoncontent['shapes'][i1]['label'])
print("标注完美，你是个合格的标注工具人:)")

#检查标签命名是否规范，如soya写成saya
# import os
# import json
# import glob
# import re
# path = r'D:\Data\wheat\\'
# json_path = os.listdir(path)
# json_path =  glob.glob(path+"*.json")
# print(json_path)
# for i in range(len(json_path)):
#     # print(json_path[i])
#     #读取json 文件！！
#     f = open(json_path[i],encoding='utf-8')
#     jsoncontent = json.load(f)
#     #遍历shapes，查看shape——type是否为多边形
#     for i1 in range(len(jsoncontent['shapes'])):
#         # print(jsoncontent['shapes'][i1]['shape_type'])
#         # print()
#         if(re.sub(u"([^\u0041-\u007a])", "", jsoncontent['shapes'][i1]['label']) not in ['soya','wheat']):
#             print("标签错误！！",json_path[i],'\t','标签：',jsoncontent['shapes'][i1]['label'])
# print("完美，你是个合格的标注工具人:)")
