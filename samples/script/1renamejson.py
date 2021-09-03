#将转换后的json文件重命名，1.json,2.json，大豆1-41，水稻42-104，玉米105-157,小麦158-253

import os
length =  len(os.listdir(r'D:\Camera Roll\Crop classification\ML\order1'))
#for dirs in os.listdir(r'D:\Camera Roll\Crop classification\ML\order1'):   # 改成你自己的json文件夹所在的目录
dirs = os.listdir(r'D:\Camera Roll\Crop classification\ML\order1')   # 改成你自己的json文件夹所在的目录
#print(dirs)  
for i in range(1,length+1):
    #print(i)
    old_name = os.path.join(r'D:\Camera Roll\Crop classification\ML\order1' ,dirs[i-1])
    new_name = os.path.join(r'D:\Camera Roll\Crop classification\ML\order1' ,str(i+253)+'_json')
    print(new_name)
    os.rename(old_name, new_name)
       # print(dirs)
   
    # for dr in dirs:
        # file_dir = os.path.join(root, dr)
       # # print(file_dir)
       # # print(dr)
        # b = os.listdir(file_dir)
        # #print(b)
        # new_name = dr.split('_')[0] + '.png'
        # img_name= b[0].split('.')[0]+ '.png'
        # file = os.path.join(file_dir, img_name)
        # # # print(file)
        # # new_name = dr.split('_')[0] + '.png'
        # new_file_name = os.path.join(file_dir, new_name)
        # print(new_file_name)
        # os.rename(file, new_file_name)
