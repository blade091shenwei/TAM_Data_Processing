#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

# ＊＊＊＊＊＊＊＊程序功能＊＊＊＊＊＊＊＊
#     将整理好的YahooNews结构化数据集，
#     处理成bag of words的形式
#     一篇文章生成对应的文件，文件中的一行是一条评论
# 处理的过程主要包括：
#     1.  词性标注，留下标注为名词、动词、副词、形容词的词汇
#     2.  去除单词中可能存在的标点符号
#     3.  词形还原，将单词的复数等可能的形式还原成原本的形式
#     4.  去除停止词，去除停止词列表中的词汇
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
    writeFolderPath = '/media/blade091/新加卷/Data/TAM-Data/bag_of_words_Politics/'
    readFolderPath = '/media/blade091/新加卷/Data/TAM-Data/newPolitics/'
    
    '对没一个文件'
    count = 0
    files = os.listdir(readFolderPath) 
    for fileName in files:
        count = count + 1
        print count 
        
        writeFilePath = writeFolderPath + fileName 
        readFilePath = readFolderPath + fileName
        HTML = html.fromstring(open(readFilePath).read())
        eles = HTML.xpath('//comment|//reply')
        
        writeFile = open(writeFilePath,'a')
        
        for ele in eles:
            '词性标注'
            wordsTagged = []
            eleTokens = nltk.word_tokenize(ele.text)
            tagTokens = nltk.pos_tag(eleTokens)
            for tagToken in tagTokens:
                if tagToken[1] in tagList:
                    wordsTagged.append(tagToken[0]) 
            
            '去除单词中可能的符号'
            '去除括号、逗号、引号，去除位于单词结尾处的句号'
            #末尾要去除的可能的标点符号有逗号和句号
            wordsPunctuationRemoval = []
            for word in wordsTagged:
                if cmp(word[-1], '.') == 0:
                    word = word.replace('.','')
                else:
                    pass
                word = word.replace(',','')\
                    .replace('\"','').replace('\'','')\
                    .replace('(','').replace(')','')
                wordsPunctuationRemoval.append(word)
                
#             '词形还原'
#             #先不进行词形还原了，有些很奇怪的结果，不做词形还原先试试效果
#             wordsLemmatized = []
#             for word in wordsPunctuationRemoval:
#                 newWord = lemmatizer.lemmatize(word)
#                 wordsLemmatized.append(newWord)
                
            '去除文件中的停止词'
            wordsStopRemoval = []
            for word in wordsPunctuationRemoval:
                if word in stopWordList:
                    pass
                else:
                    wordsStopRemoval.append(word)
            
            '写入文件'
            for word in wordsStopRemoval:
                writeFile.write(' ') 
                writeFile.write(word)
            writeFile.write('\n')
            
        writeFile.close()
        
        
        
        
    
    