import scrapy
import os
os.environ["http_proxy"] = "http://192.168.5.1:7890"
os.environ["https_proxy"] = "http://192.168.5.1:7890"

class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://book.douban.com/',
    ]
    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically


# lastly, run this in terminal
# scrapy runspider 5-2-scrapy.py -o res.json