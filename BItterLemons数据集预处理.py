#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

import nltk
from nltk.stem import WordNetLemmatizer 

if __name__ == "__main__":
    
    lemmatizer = WordNetLemmatizer()
    
    '读取停止词文件'
    readStopWord = open('newStopWords','r')
    stopwords = []
    for line in readStopWord.xreadlines():
        stopword = line.replace('\n','').replace('\r','')
        if cmp(stopword,'') == 0:
            pass
        else:
            stopwords.append(stopword)
    
    '打开写入的文件'
    writeFile = open('input_docs.txt','a')
    
    count = 0
    
    '对每一个文件'
    filePath = '/media/blade091/新加卷/TAM-RELATED-PROJECTS/bt.1.0/docs/'
    files = os.listdir(filePath)
    for file in files:
        count = count + 1
        print count 
        '词性标注'
        words_tagged = []
        tagList = ['NN', 'NNS', 'NNP', 'NNPS',\
                   'JJ', 'JJS', 'RB', 'RBR', 'RBS',\
                   'VB', 'VBD', 'VBG', 'VBP', 'VBZ']
        fileName = filePath + file
        doc = open(fileName).read()
        docWords = nltk.word_tokenize(doc)
        docTokens = nltk.pos_tag(docWords)
        for token in docTokens:
            if token[1] in tagList:
                words_tagged.append(token[0])
        
        '去除停止词及标点符号'
        words_stopRemoval = []
        for word in words_tagged:
            newWord = word.replace(',','')\
                    .replace('\"','').replace('\'','')\
                    .replace('(','').replace(')','')\
                    .replace('.','')
            if not newWord in stopwords and\
                cmp(newWord,'') != 0:
                words_stopRemoval.append(newWord)
        
        '词形还原'
        words_lemmatized = []
        for word in words_stopRemoval:
            newWord = lemmatizer.lemmatize(word)
            words_lemmatized.append(newWord)

        '写入文件'
        writeFile.write('0') 
        for word in words_lemmatized:
            writeFile.write(' ')
            writeFile.write(word)
        writeFile.write('\n')
        
    writeFile.close()