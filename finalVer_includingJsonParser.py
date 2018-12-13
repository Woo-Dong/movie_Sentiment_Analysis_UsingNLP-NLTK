import csv
import json
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer as Vader


# ==================== NLTK Processing PART
csvFile_output = open('csvFile_output.csv', 'w', encoding='utf-8')
wr = csv.writer(csvFile_output)
wr.writerow(["id", "timestamp", "Sentimental Score", "text"])

fileName = 'insert_JSON_File_name.json'

with open(fileName, 'r') as jsonFile:
    json_contents = json.load(jsonFile)

for aJson in json_contents:
    
    idNum = aJson["id"] 
    timestamp = aJson["timestamp"]  
    textArea = aJson["text"]

    letters_only = re.sub('[^a-zA-Z]', ' ', textArea )   #text부분에서 영어만 추출, 특수문자 등은 빈칸으로 채움
    
    lower_case = letters_only.lower()   
    words = lower_case.split()  #단어만 split함(빈칸 제거)
    words = [w for w in words if not w in stopwords.words('english')]   #stopwords 제거(I, me, my, our, ...)

    #복수형, 진행형등의 문자를 같은 의미의 단어로 다룰수 있게 함
    stemmer = SnowballStemmer('english')    
    words = [stemmer.stem(w) for w in words]

    wordnet_lemmatizer = WordNetLemmatizer()
    
    divWords = ""
    for w in words:
        if w == 'war':
            continue
        else:
            divWords += wordnet_lemmatizer.lemmatize(w) + " "
    sid=Vader()

    ss=sid.polarity_scores(divWords)
    sentimentalStatus = ss['compound']

    wr.writerow([idNum, timestamp, sentimentalStatus, divWords ] )

print("Complete: ", fileName) 

