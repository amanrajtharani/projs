import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

def read_article(clicked_url):
    os.system('cls')
    response2 = requests.get(clicked_url)
    soup = BeautifulSoup(response2.content,'lxml')
    main_content = soup.find('div',class_="detail-content")
    story_paragraphs = soup.find('div',class_="story-detail")
    if main_content:
        content_heading = main_content.find('div',class_="detail-heading")
        date = main_content.find('div',class_="category-date")
        if content_heading:
            title = content_heading.find('h1')
            print(title.text)
            print(date.text,"\n")
            for story_paragraph in story_paragraphs: 
                print(story_paragraph.text)

def article_list(ciick_link):
    os.system('cls')
    response = requests.get(ciick_link)
    cont = BeautifulSoup(response.content, 'lxml')
    articles = cont.find('div', class_='detail-center')
    article_link = []
    if articles:
        article_list_items = articles.find_all('li')
        if article_list_items:
            for item in article_list_items:
                tpage = item.find('div',class_="latest-right")
                title_tag = item.find('a', class_="open-section")
                date = item.find('span',class_="latestDate")  
                if title_tag:
                    article_link.append(title_tag.get('href'))
                    name = tpage.find('p')
                    if name:
                        print(name.text) 
                        print(date.text)
    read_input = int(input("Enter the number of article : "))
    os.system('cls')
    read_article(article_link[read_input-1]) 
def main():
    print("********************************************************************")
    print("Here is the list of cateogaries choose anyone which you want to read")
    cateogaries = {
        "latest" : 'https://www.thenews.com.pk/latest-stories',
        "national" : 'https://www.thenews.com.pk/latest/category/national',
        "sports" : 'https://www.thenews.com.pk/latest/category/sports',
        "world" : 'https://www.thenews.com.pk/latest/category/world',
    }
    links = []
    for key in cateogaries:
        print(f"{key}")
        links.append(cateogaries[key])
    cateogary_num = int(input("Enter the number of cateogary : "))
    article_list(links[cateogary_num-1])




if __name__ == "__main__":
    main()
