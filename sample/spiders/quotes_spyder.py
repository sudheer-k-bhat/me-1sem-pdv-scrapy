import scrapy

#from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = ['http://quotes.toscrape.com']

	def parse(self, response):
		#items = QuotetutorialItem()

		all_div_quotes = response.css('div.quote')
		for quote in all_div_quotes:
			title = quote.css('span.text::text').extract()
			author = quote.css('.author::text').extract()
			tags = quote.css('.tag::text').extract()
		#items['title'] = title
		#items['author'] = author
		#items['tag'] = tags
		yield{'Title': title, 'Author':author, 'Tags': tags}
