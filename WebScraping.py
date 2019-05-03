import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions?sort=newest&page=110000")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

print(soup)

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
