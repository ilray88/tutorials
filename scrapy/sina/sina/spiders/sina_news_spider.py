#!/usr/bin/env mytrader
# -*- coding: utf-8 -*-
# Created by ZIJIA on 2021/10/15
#
import re

import scrapy
from bs4 import BeautifulSoup


class SinaNewsSpider(scrapy.Spider):

	name = 'sina_news'
	start_urls = [
		'https://news.sina.com.cn'
	]
	custom_settings = {
		'LOG_LEVEL':'ERROR'
	}
	def parse(self,response):
		# print(response.url)
		# print(response.body)
		soup = BeautifulSoup(response.body,'html.parser')
		tags = soup.find_all('a',href=re.compile(r"sina.*\d{4}-\d{2}-\d{2}.*shtml$"))
		for tag in tags:
			url = tag.get('href')
			yield scrapy.Request(url,callback=self.parse_details)
	def parse_details(self,response):
		soup = BeautifulSoup(response.body,'html.parser')
		try:
			title = self.extract_title(soup)
			if title is None:
				raise Exception('Title not find for ' + response.url)
		except Exception as e:
			self.logger.error(str(e))


	def extract_title(self,soup):
		selectors = ['h1.main-title']
		for selector in selectors:
			if len(soup.select(selector))!=0:
				title = soup.select(selector)[0].text
				return title









