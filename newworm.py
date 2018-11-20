# # coding:utf-8
#
# import requests
# from bs4 import BeautifulSoup
#
# test_url = 'http://movie.douban.com/top250/'
#
# def download_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
#     }
#     data = requests.get(url,headers=headers).content
#     return data
#
# movie_name_list = []
# def parse_html(html):
#     soup = BeautifulSoup(html)
#     movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
#     if movie_list_soup != None:
#         for movie_li in movie_list_soup.find_all('li'):
#             detail = movie_li.find('div', attrs={'class': 'hd'})
#             movie_name = detail.find('span', attrs={'class': 'title'}).getText()
#             movie_name_list.append(movie_name)
#
#         next_page = soup.find('span', attrs={'class': 'next'}).find('a')
#         if next_page:
#             parse_html(download_page(test_url + next_page['href']))
#         return movie_name_list
#
# def main():
#     handle = parse_html(download_page(test_url))
#     if handle != None:
#         handle = list(handle)
#         for ele in handle:
#             print(ele)
#
# if __name__ == '__main__':
#     main()
import urllib
import re

# 根据url获取网页html内容
def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()

# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    # 解析jpg图片url的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')  # 注：这里最后加一个'width'是为了提高匹配精确度
    # 解析出jpg的url列表
    jpgs = re.findall(jpgReg, html)
    return jpgs

# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    urllib.urlretrieve(imgUrl, fileName)

# 批量下载图片，保存到F盘zdl文件夹
def batchDownloadJPGs(imgUrls, path='F:/zdl/'):
    # 用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print('正在下载第'+str(count)+'张')
        count = count + 1

# 封装：从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)

if __name__ == '__main__':
    main()