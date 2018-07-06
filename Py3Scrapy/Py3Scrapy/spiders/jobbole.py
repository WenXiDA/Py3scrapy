# -*- coding: utf-8 -*-
import hashlib
import  re
import sys, os

import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from Py3Scrapy.items import JobBoleArticleItem

from Py3Scrapy.commons import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://python.jobbole.com/all-posts/']

    def parse(self, response):

        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        print(post_nodes)
        print(type(post_nodes))
        for post_node in post_nodes:
            image_url = post_node.css('img::attr(src)').extract_first('')
            post_url = post_node.css('::attr(href)').extract_first('')
            print(image_url)
            print(post_url)
            #创建Request对象，传给scrapy进行页面的下载，
            # parse.urljoin(response.url, post_url)方法是为了防止从href中获取的url是省略的主域名的，所以使用该方法可以将主域名和子域名链接
            #callback在Request下载完成后调用，进行文章详情的处理
            yield Request(url= parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self.parse_detail, dont_filter=True, errback= self.errback_httpbin)
            '''parse.urljoin(response.url, post_url)补全域名'''
        next_url = response.css('.next.page-numbers::attr(href)').extract_first('')
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse, dont_filter=True, errback=self.errback_httpbin)

    def parse_detail(self, response):
        article_items = JobBoleArticleItem()
        font_image_url = response.meta.get('front_image_url', '')
        title = response.xpath("//div[@id='wrapper']/div[3]/div[1]/div[1]/h1/text()").extract()[0]
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace('·', '').strip()
        zan = response.css(".post-adds span h10::text").extract_first('')
        zan = int(zan) if zan !='' else 0
        shoucang = response.xpath("//div[@class='post-adds']/span[2]/text()").extract()[0].strip()
        match_re = re.match('(\d+)', shoucang)
        if match_re:
            shoucang = int(match_re.group()[0])
        else:
            shoucang = 0
        pinglun = response.xpath("//div[@class='post-adds']/a[1]/span[1]/text()").extract()[0].strip()
        match_re = re.match('(\d+)', pinglun)
        if match_re:
            pinglun = int(match_re.group()[0])
        else:
            pinglun = 0
        tag_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)
        try:
            create_date = datetime.datetime.strptime(create_date, '%Y/%m/%d').date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        url = response.url
        # print(zan)
        # print(title)
        # print(pinglun)
        # print(shoucang)
        # print(create_date)
        article_items['url'] = url
        article_items['title'] = title
        article_items['create_date'] = create_date
        article_items['zan'] = zan
        article_items['shoucang'] = shoucang
        article_items['pinglun'] = pinglun
        article_items['tags'] = tags
        article_items['font_image_url'] = [font_image_url]
        article_items['url_object_id'] = get_md5(url)
        yield article_items

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)


