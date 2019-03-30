# -*- coding: UTF-8 -*- 
class Crawler:
    def __init__(self,HTMLStr):
        # 套件引入
        from bs4 import BeautifulSoup
        # title、img、運費 dict 對應集合
        productInfoDict = {}

        # print(urlHTMLAry)

        soup = BeautifulSoup(HTMLStr, 'html.parser')

        # all titles
        h2_tags_title = soup.find_all('li',class_="item-name")
        h3_tags_title = soup.find_all('h3',class_="item-name isDefault-name")

        all_tags_title = h2_tags_title + h3_tags_title

        # all images
        h3_tags_imgs = soup.find_all('img',class_="rt-product-image")

        print(len(all_tags_title))
        print(len(h3_tags_imgs))

        # while i<len(all_tags_title):
        # AryQQQQ = []
        for i in range(10):
            print h2_tags_title[i].text
            print h3_tags_imgs[i]['src']



