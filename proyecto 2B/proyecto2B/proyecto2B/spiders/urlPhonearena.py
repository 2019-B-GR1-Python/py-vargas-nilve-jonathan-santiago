import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class AraniaLinksPhone (CrawlSpider):
	name = 'crawl_urls2'
	
	allowed_domains = ['www.phonearena.com']
	
	start_urls = ['https://www.phonearena.com/phones/manufacturers']
	
	
	url_segmento_permitido = ('Apple')
	
	regla_dos = (##busca dentro de dominios
			Rule( ## permitidos y segmentos permitidos
					LinkExtractor(
						allow_domains = allowed_domains,
						allow = url_segmento_permitido				
					), callback = 'parse_page'		
				),	
	)
				
	rules = regla_dos #heredado (override)
	
	def parse_page(self,response):
		
		links = response.xpath('//*[@id="manufacturers-content-inner"]/div/div[2]/div[1]/a[2]/@href').extract()
		print(f'links {links}')
		serie_links = pd.Series(links)
		
		
		salida = 'www.phonearena.com' + serie_links + '\n'
		
		with open('urls2.txt','+a') as file:			
				file.writelines(salida)