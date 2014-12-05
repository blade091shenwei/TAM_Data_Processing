#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     继续数据预处理1的处理，将数据中的大写单词，
#     尤其是首字母大写的单词转换成全部小写的形式
#     具体的：
#         提供文件夹的路径，对文件夹内的所有文本进行大写字母的转换处理
#     直接将文章的评论处理成以空格为分割的bag of words的形式
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

import os
import re

if __name__ == "__main__":
    
    readFolderPath = '/media/blade091/新加卷/Data/TAM-Data/bag_of_words_Politics/'
    writeFolderPath = '/media/blade091/新加卷/Data/TAM-Data/bag_of_words_Politics2/'
    files = os.listdir(readFolderPath)
    count = 0
    for fileName in files:
        count = count + 1
        print count 
        readPath = readFolderPath + fileName 
        writePath = writeFolderPath + fileName 
        
        writeFile = open(writePath, 'a')
        
        TEXT = open(readPath).read()
        words = re.split(' |\n',TEXT)
        for word in words:
            if cmp(word,'') == 0:
                pass
            else:
                writeFile.write( word.lower() )
                writeFile.write(' ')
        
        writeFile.close()
        
    
    