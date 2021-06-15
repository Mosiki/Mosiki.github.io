# author: V0W
# env: python3

import os
import re

# list files
def listFiles(dirPath):
	fileList=[]
	for root,dirs,files in os.walk(dirPath):
		for fileObj in files:
			fileList.append(os.path.join(root,fileObj))
	return fileList

def main():
	fileDir = "./"
	oldstr = r'https://cdn.jsdelivr.net/gh/Mosiki/blog-imgs/' ##这里是旧的七牛云外链
	newstr = r'https://cdn.jsdelivr.net/gh/Mosiki/blog-imgs/'   ### 这个是新的图床的外链,使用jsDelivr加速访问，https://cdn.jsdelivr.net/gh/GitHub用户名/图床仓库名/图片路径
	FileList = listFiles(fileDir)
	# print(FileList)
	for fname in FileList:
		f = open(fname, 'r+', encoding='UTF-8')
		all_the_lines=f.readlines()
		# print(all_the_lines)
		f.seek(0)
		f.truncate()
		for line in all_the_lines:
			f.write(line.replace(oldstr,newstr))
		f.close()

if __name__=='__main__':
    main() 
