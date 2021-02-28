import scrapy

from ..items import PeopleItem


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = ['https://www.work.ua/resumes-kharkiv/']

    def parse(self, response):
        for person in response.css('div.card.resume-link'):
            name = person.css('div b::text').get()
            age = person.css('div span:nth-child(3)::text').get()
            if '·' in age:
                age = person.css('div span:nth-child(4)::text').get()
            position = person.css('h2 a::text').get()

            people_item = PeopleItem()
            people_item['name'] = name
            people_item['age'] = age
            people_item['position'] = position

            yield people_item