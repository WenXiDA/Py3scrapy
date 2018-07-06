# -*- coding: utf-8 -*-


import  sys
import os
from scrapy.cmdline import  execute

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
#启动scrapy命令： scrapy crwal "spidername",EX:scrapy crawl jobbloe
execute(["scrapy", "crawl", "jobbole"])