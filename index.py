# -*- coding: UTF-8 -*- 

# 引入模組
from connect import Connector
from crawler import Crawler

# 輸入url進行連線
conn = Connector('https://class.ruten.com.tw/user/index00.php?s=hambergurs')

# 印出 title、img 清單
Crawler(conn.htmlStr)

