#coding: utf-8
#scrapy crawl dnvgl -o dnvgl.json
#scrapy crawl dnvgl -o dnvgl.csv
import scrapy
import logging

from ShipSpider.items import ShipspiderItem


class ShipSpider(scrapy.Spider):
    name ='dnvgl'
    start_urls = [
        'https://www.dnvgl.com/cn/maritime/news/index.html'
    ]
    def parse(self, response):
        # 爬取所需内容
        for quote in response.xpath('/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul'):
            item = ShipspiderItem()
            #直接用chrome浏览器的开发者模式获取xpath
            item['title'] = quote.xpath('/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul/li/a/div[2]/text()').extract()
            #href的正确写法@href,
            item['url'] = quote.xpath('/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[1]/ul/li/a/@href').extract()
            yield item
        #next_page = response.xpath('/*[@id="listDiv"]/p/a[3]').extract_first()
        next_page = response.xpath('/html/body/div[1]/main/section[2]/div[2]/div/div/section/div[2]/a').extract()
        # 如果找得到下一页的连接，创建一个request并且设定这个request的callback为parse（）
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)