import scrapy

from ..items import SampleItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = ['http://quotes.toscrape.com']
	page_number = 2

	def parse(self, response):
		items = SampleItem()

		all_div_quotes = response.css('div.quote')
		for quote in all_div_quotes:
			title = quote.css('span.text::text').extract()
			author = quote.css('.author::text').extract()
			tags = quote.css('.tag::text').extract()
			items['title'] = title
			items['author'] = author
			items['tag'] = tags
			yield items

		if self.page_number < 11:
			next_page = self.start_urls[0] + '/page/'+ str(self.page_number)
			yield response.follow(next_page, callback = self.parse)
			self.page_number += 1

