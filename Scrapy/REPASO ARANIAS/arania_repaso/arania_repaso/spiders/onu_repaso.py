import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#https://github.com/alexolmedo/2018-B-GR1-Python/blob/master/proyecto2/scrapy/iphone.csv
class AraniaCrawlOnu (CrawlSpider):
	name = 'crawl_onu' # heredadp (override)
	
	allowed_domains = ['un.org']
	
	start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/']
	
	regla_uno = (## busq TODO!
		Rule( LinkExtractor(),callback = 'parse_page')
		,
	)
	
	url_segmento_permitido = (
		'funds-programmes-specialized-agencies-and-others'
	) 
	
	
	regla_dos = (#busca dentro de los dominios
		Rule( ##permitidos y segmentos permitidos
			LinkExtractor(
				allow_domains = allowed_domains,
				allow = url_segmento_permitido
			), callback = 'parse_page'
		),
	)
	
	
	url_segmentos_restringido = (
		'ar/sections',
		'zh/sections',
		'ru/sections'
	)
	
	
	regla_tres = (
		Rule(
			LinkExtractor(
				allow_domains = allowed_domains,
				allow = url_segmento_permitido,
				deny = url_segmentos_restringido
			),callback = 'parse_page'
		),
	)
	
	
	rules = regla_tres #heredado (override)
	
	def parse_page(self,response):
		lista_programas_onu = response.css('div.field-items > div.field-item > h4::text').extract()
		
		for agencia in lista_programas_onu:
			with open('onu_agenciasR3.txt','a+',encoding = 'utf-8') as archivo:
				archivo.write(str(agencia) + '\n')
	