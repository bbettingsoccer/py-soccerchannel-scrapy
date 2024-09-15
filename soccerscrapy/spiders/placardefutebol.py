import scrapy

from soccerscrapy.items import SoccerscrapyItem


class PlacardefutebolSpider(scrapy.Spider):
    name = "placardefutebol"
    allowed_domains = ["placardefutebol.com.br"]
    start_urls = ["https://www.placardefutebol.com.br"]

    def parse(self, response):
        dataObj = SoccerscrapyItem()

        for article in response.xpath('//div[@class="row align-items-center content"]'):
            dataObj['status'] = article.xpath(
                './/div [@class="w-25 p-1 status text-center"]//span//text()').extract_first()
            print(" STATUS ", dataObj['status'])

            dataObj['teamA'] = article.xpath('.//h5[@class="text-right team_link"]//text()').extract_first()
            dataObj['teamB'] = article.xpath('.//h5[@class="text-left team_link"]//text()').extract_first()
            dataObj['scoreA'] = article.xpath(
                './/div[@class="w-25 p-1 match-score d-flex justify-content-end"]//h4//span//text()').extract_first()
            dataObj['scoreB'] = article.xpath(
                './/div[@class="w-25 p-1 match-score d-flex justify-content-start"]//h4//span//text()').extract_first()
            yield dataObj
