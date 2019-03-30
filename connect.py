# -*- coding: UTF-8 -*- 

class Connector:
    def __init__(self,url):
        # 引入 需要 模組
        import requests

        # self.urlHTMLAry = []
        self.htmlStr=''

        # 定死讓他只會取三頁的資料
        for i in range(3):
            # header 避免 request 被擋下
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

            # 目標網址
            url = 'https://class.ruten.com.tw/user/index00.php?s=hambergurs&p='

            # 使用 GET 方式下載普通網頁
            re = requests.get(url+str(i),headers=headers)

            # 檢查狀態碼是否 OK
            try:
                if re.status_code == requests.codes.ok:
                    re.encoding = 'utf8'
                    # 網頁 HTML 原始碼塞入Ary
                    self.htmlStr = self.htmlStr + re.text
                    # self.urlHTMLAry.append([re.text])
            except:
                print('連線錯誤')
