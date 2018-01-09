
# Haha. Häx
# https://stackoverflow.com/questions/44058239/sqlite3-error-on-aws-lambda-with-python-3
import imp
import sys
sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")

import os
import datetime
import logging
import json

import boto3

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# from hy_scraper.spiders import OpintoniSpider

def crawl(event, context):
  # process = CrawlerProcess(get_project_settings())

  start = datetime.datetime.utcnow()
  logger.info('Crawling started: {}'.format(datetime.datetime.now().time()))

  configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
  runner = CrawlerRunner(get_project_settings())

  d = runner.crawl('opintoni_spider')
  d.addBoth(lambda _: reactor.stop())
  reactor.run() # the script will block here until the crawling is finished

  # process.crawl('opintoni_spider')
  # process.start() # the script will block here until the crawling is finished

  end = datetime.datetime.utcnow()
  logger.info('Crawling took {} h:m:s:ms'.format(str(end - start)))