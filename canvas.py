from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
#from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
import scrapy

from lib2to3.pgen2 import driver
from telnetlib import EC
from token import OP
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

class LoginSpider(Spider):
  name = 'GitHubLogin'
  start_urls = ['https://canvas.utp.edu.pe/']

  def parse(self, response):
    full_url = response.xpath('//div[@class="ctacanvas_main"]').extract_first()
    query = urlparse(full_url).query

    return scrapy.FormRequest.from_response(
      response,
      formdata={'pseudonym_session_password': 'u17200379@utp.edu.pe', 'password': open('./password.txt').readline().strip()},
      callback=self.after_login
    )

  def afterlogin(self, response):
    #check login succeed before going on
    if "authentication failed" in response.body:
         self.log("Login failed", level=log.ERROR)
    else:
        return Request(url="http://example.com",
                           callback=self.parse_Page)

  def parse_repositorios(self, response):
    sel = Selector(response);
    repositorios = sel.xpath('//span[@class="Grouping-styles__title"]/text()')
    for repositorio in repositorios:
      print (repositorio.get())

process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': 'datos_de_salida.json'
})
process.crawl(LoginSpider)
process.start()