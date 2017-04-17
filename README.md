# ShipSpider
第一步：准备开发环境
1.	桌面环境：申请阿里云云服务器ECS实例，Windows  Server2008 R2 Enterprise 64位（单核Xeon2.6Gzh、2G内存、50G系统盘；实际开发中，建议使用Mac或Linux环境，能避免很多不必要的坑。）
2.	安装Python环境：Anaconda4.2（Python3.5）（便于定制多个版本的Python开发环境，并且集成了很多科学计算库）
3.	安装爬虫库：用命令行安装Scrapy1.3.3
pip install scrapy
4.	安装IDE：Pycharm（Community 2017.1）和SublimeText3

第二步：创建第一个项目
本文案例将在D盘根目录下创建Scrapy项目，启动命令行，输入：
scrapy install ShipSpider
在本地生成项目文件，目录结构为：
D:\SHIPSPIDER
│  scrapy.cfg
│  
└─ShipSpider
    │  items.py
    │  middlewares.py
    │  pipelines.py
    │  settings.py
    │  __init__.py
    │  
    ├─spiders
    │  │  __init__.py
    │  │  
    │  └─__pycache__
    └─__pycache__

第三步：获取及分析DNVGL网站新闻页面
用Chrome打开www.dnvgl.com，找到新闻页面：
https://www.dnvgl.com/cn/maritime/news/index.html
这个URL就是本次要抓取的网页页面。通过键F12打开开发者模式，在网页的源代码中找到要抓取的内容的HTML代码，从而获得XPath。
获取内容的块的XPath：/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul
获取文章标题的XPath：/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul/li/a/div[2]/text()
获取文章正文链接的XPath：/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul/li/a/@href

第四步：在item.py中增加需要抓取的主要内容
在已经创建的类class ShipspiderItem(scrapy.Item)增加：
    title = scrapy.Field()#标题
    url = scrapy.Field()#正文URL

第五步：以上都是准备工作，开启真正的爬取代码。
在\ShipSpider\spiders\目录下新建dnvgl_spider.py，代码见源码。

第六步：代码都写完了，测试下吧
在D:\ShipSpider目录下，进行命令行操作：
scrapy crawl dnvgl -o dnvgl.json

第七步：检查看下爬取的文件吧
D:\ShipSpider目录下，打开dnvgl.json，抓取的数据见dnvgl.json。
至此，完成了所有的代码开发，实现了最简单的网页新闻列表爬取，总共历时15小时。代码虽然简单，但是感觉看世界的角度有了很大变化。

在过程中遇到了默认编码、反爬虫、命令行操作、XPath等大坑，坚持几个原则就行：
1.	保持热情，坚定目标，坚持、坚持、再坚持；
2.	能看官方文档就看不看网友博客；
3.	能google就不baidu。
