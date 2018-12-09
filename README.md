# movie_Sentiment_Analysis_UsingNLP-NLTK

영화 Avengers: Infinity War 에 대해 트위터에서 언급한 텍스트 부분을 토대로 
영화 예고편 및 개봉 전/후에 대한 사람들의 만족감/기대감을 비교할 수 있다.

# 1. Utlities

* Python을 이용하여 트위터에서 원하는 키워드, 기간, 원하는 갯수를 입력하면 자동으로 JSON 파일 형식으로 출력해주는 오픈소스를 활용하였다.
 https://github.com/taspinar/twitterscraper
 
 위의 소스코드를 그대로 git하여 활용하였으며 기타 코드 수정은 하지 않았다.
 
* Python을 지원하는 NLP인 NLTK를 활용하여 각 텍스트 부분을 추출하여 자연언어 처리한 후 감정분석하여 정규화하는 툴을 썼다.
