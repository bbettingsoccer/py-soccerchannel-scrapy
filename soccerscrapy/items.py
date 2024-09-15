# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoccerscrapyItem(scrapy.Item):
    teamA = scrapy.Field()
    scoreA = scrapy.Field()
    teamB = scrapy.Field()
    scoreB = scrapy.Field()
    status = scrapy.Field()

