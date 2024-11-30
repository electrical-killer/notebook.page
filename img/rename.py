import os    
import sys
filedir = os.path.dirname(os.getcwd())      #获取脚本所在目录
os.chdir(filedir)         #将脚本所在的目录设置为工作目录
wdir = os.getcwd()        #返回当前目录
print('当前工作目录：{}\n'.format(wdir))           #打印当前工作目录
												   #root	表示正在遍历的文件夹的名字（根/子）
for parent, dirs, files in os.walk(wdir):          #dirs	记录正在遍历的文件夹下的子文件夹集合
	i = 1										   #files	记录正在遍历的文件夹中的文件集合
	parent_base = os.path.basename(parent)         # parent（根目录）下的文件夹  #os.path.basename(),返回path最后的文件名
	if ('webp' in parent_base) :     #如果根目录下存在Picture和Video两个文件夹，进行下一步
		for file in files:                         #检测是否有文档        
			file_ext = file.split('.')[-1]         #返回文件的路径和文件名
			tmp = parent.split('\\')				#.split（'\\'）分割符
			new_name = 'data' + '\\' + 'obj' + '\\' + 'background' + str(i).zfill(3) + '.' + file_ext       #str.zfill(width)    width指定字符串的长度。原字符串右对齐，前面填充0
			old_path = os.path.join(parent, file)  #分离的部分合成一个整体
			new_path = os.path.join(parent, new_name)     
			os.rename(old_path, new_path)            
			i += 1
