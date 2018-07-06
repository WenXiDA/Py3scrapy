# -*- coding: utf-8 -*-


import sys, os


# Scrapy settings for Py3Scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Py3Scrapy'

SPIDER_MODULES = ['Py3Scrapy.spiders']
NEWSPIDER_MODULE = 'Py3Scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Py3Scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY为True会读取网站的url，将不符合robots协议的url过滤掉
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Py3Scrapy.middlewares.Py3ScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Py3Scrapy.middlewares.Py3ScrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# scrapy自动下载图片pipelines，后面的数字表示执行的顺序，这里先执行ImagesPipeline
ITEM_PIPELINES = {
    'Py3Scrapy.pipelines.Py3ScrapyPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'Py3Scrapy.pipelines.ArticleImagesPipeline': 1,
    'Py3Scrapy.pipelines.JsonWithEncodingPipeline': 2,
    'Py3Scrapy.pipelines.JsonExporterPipeline': 3,
    'Py3Scrapy.pipelines.MysqlTwistedPipline': 4,

}
#设置图片的url,在解析IMAGES_URLS_FIELD时使用的是数组，，所以这里的IMAGES_URLS_FIELD必须是列表，
#而IMAGES_URLS_FIELD的值优势在items中获取的，所以items中ont_image_url对应的值必须是列表，即article_items['font_image_url'] = [font_image_url]
IMAGES_URLS_FIELD = 'font_image_url'
project_dir = os.path.dirname(os.path.abspath(__file__))
#图片储存路径
print(project_dir)
IMAGES_STORE = os.path.join(project_dir, 'images')
#过滤下载图片的大小
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DATABASES = {
    'default': {
        'NAME': 'maxshop',  # 数据库名
        'USER': 'root',  # 用户名
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'utf8',  ##设置字符集，不然会出现中文乱码
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    }
}
