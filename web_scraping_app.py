import requests
from bs4 import BeautifulSoup

# Stackoverflow newest questions -
stack_overflow_res = requests.get('https://stackoverflow.com/questions')
stack_overflow_soap = BeautifulSoup(stack_overflow_res.text, 'html.parser')

questions = stack_overflow_soap.select('.question-summary')

for question in questions:
    print(question.select_one('.question-hyperlink').getText())
    print(question.select_one('.vote-count-post').getText())


# Top headlines from India today -
news_res = requests.get('https://www.indiatoday.in/news.html')
news_soap = BeautifulSoup(news_res.text, 'html.parser')

headlines = news_soap.select('.story')

for headline in headlines:
    print(headline.getText())
    print('https://www.indiatoday.in/' + headline.select_one('a').get('href'))
