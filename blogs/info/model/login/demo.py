# import requests
# import json
# from lxml import etree
#
# headers={
#     "User-Agent":'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
# }
url='https://www.feixiaohao.com/search?word=EXT'
# response = requests.request("POST",url,headers=headers)
# # print(response.text)
# data = etree.HTML(response.content.decode('utf-8'))
# # print(type(data),data)
# res= data.xpath('//div/a/span/text()')
# print(res)

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url=url)

ret_list  = driver.find_elements_by_xpath('//*[@class="ivu-table-row"]//*[@class="ivu-table-column-left"]//*[@class="ivu-table-cell"]/*')
for ret in ret_list:
    print(ret.get_attribute("href"))