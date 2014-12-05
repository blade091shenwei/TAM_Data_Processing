#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     将整理好的YahooNews结构化数据集（当中的评论），处理成
#     bag of words的形式
#     一篇文章的评论对应的是一篇文章
#     （可以将所有文章先处理好）
#     修改：并不生成input文件，而是将每个文件转换成bag of words 的形式
#     文件中的每一行是一条评论，有多少条评论和回复就有多少行，见“YahooNews数据集预处理.py”
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

import nltk
from nltk.stem import WordNetLemmatizer 
from readLib import readStopWordList
from lxml import html

if __name__ == "__main__":
    
    lemmatizer = WordNetLemmatizer()
    
    '读取停止词文件' 
    stopWordList = readStopWordList("newStopWords")
    
    '词性列表'
    tagList = ['NN', 'NNS', 'NNP', 'NNPS',\
                   'JJ', 'JJS', 'JJR', 'RB', 'RBR', 'RBS',\
                   'VB', 'VBD', 'VBG', 'VBP', 'VBZ']
    
    '打开写入的文件'
    writeFile = open('/media/blade091/新加卷/Data/TAM-Data/input_docs.txt','a')
    count = 0
    
    '对每一个文件'
    folderPath = '/media/blade091/新加卷/Data/newPolitics/'
    files = os.listdir(folderPath)
    for fileName in files:
        count = count + 1
        print count 
        
        filePath = folderPath + fileName
        HTML = html.fromstring(open(filePath).read())
        eles = HTML.xpath('//comment|//reply')
        
        '先进行词性标注'
        words_tagged = []
        for ele in eles:
            eleTokens = nltk.word_tokenize(ele.text)
            tagTokens = nltk.pos_tag(eleTokens) 
            for tagToken in tagTokens:
                if tagToken[1] in tagList:
                    words_tagged.append(tagToken[0])
        
        '去除单词中的标点符号'
        words_punctuationRemoval = []
        for word in words_tagged:
            newWord = word.replace(',','')\
                    .replace('\"','').replace('\'','')\
                    .replace('(','').replace(')','')\
                    .replace('.','')
            if cmp(newWord,'') != 0:
                words_punctuationRemoval.append(newWord)
        
        '词形还原'
        words_lemmatized = []
        for word in words_punctuationRemoval:
            newWord = lemmatizer.lemmatize(word)
            words_lemmatized.append(newWord)
        
        '去除文件中的停止词'
        words_stopRemoval = []
        for word in words_lemmatized:
            if word in stopWordList:
                pass
#                 print "!!!!!!!!!!!!!!!!"
            else:
                words_stopRemoval.append(word)
        
#         for word in words_stopRemoval:
#             print word 
        
        '写入文件'
        writeFile.write('0') 
        for word in words_stopRemoval:
            writeFile.write(' ')
            writeFile.write(word)
        writeFile.write('\n')
        
    writeFile.close()        
    
    


