import scrapy

from ..items import SampleItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	page_number = 2
	start_urls = ['http://quotes.toscrape.com']

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
		
		next_page = response.css('list.next a::attr(href)').get()
		next_page = 'http://quotes.toscrape.com/page/' + str(next_page)
		if next_page is not None:
			yield response.follow(next_page, callback = self.parse)
			next_page += 1

