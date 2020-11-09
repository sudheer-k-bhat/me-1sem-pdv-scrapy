import scrapy

#from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = ['http://quotes.toscrape.com']

	def parse(self, response):
		#items = QuotetutorialItem()

		all_div_quotes = response.css('div.quote')
		title = all_div_quotes.css('span.text::text')
		author = all_div_quotes.css('.author::text')
		tags = all_div_quotes.css('.tag::text')
		#items['title'] = title
		#items['author'] = author
		#items['tag'] = tags
		yield{'Title': title, 'Author':author, 'Tags': tags}
