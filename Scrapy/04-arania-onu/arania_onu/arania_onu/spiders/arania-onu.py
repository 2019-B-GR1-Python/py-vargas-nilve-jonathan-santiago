import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AraniaCrawlOnu (CrawlSpider):
	name = 'crawl_onu' #heredado.
	
	allowed_domains = ['un.org']
	
	start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/']
	
	regla_uno = (## busq TODO! 
				Rule(LinkExtractor(),callback = 'parse_page'),) #toma mas tiempo porq busca links y en los links busca mas links
	
	url_segmento_permitido = ('funds-programmes-specialized-agencies-and-others')
	
	regla_dos = (##busca dentro de dominios
			Rule( ## permitidos y segmentos permitidos
					LinkExtractor(
						allow_domains = allowed_domains,
						allow = url_segmento_permitido				
					), callback = 'parse_page'		
				),	
	)
				
	## lo que esta dentro de esta link no busca			
	url_segmento_restringido = ('ar/sections','zh/sections','ru/sections')
	
	# otra regla y se restrige segmentos del url.
	regla_tres = (
		Rule(
			LinkExtractor(
						allow_domains = allowed_domains,
						allow = url_segmento_permitido,		
						deny = url_segmento_restringido
					), callback = 'parse_page'
		),	
	)
	
	
	
	#las reglas son una lista de reglas.
	
	
	rules = regla_uno #heredado (override)
	
	def parse_page(self,response):
		lista_programas_onu = response.css('div.field-items > div.field-item > h4::text').extract()
		
		for agencia in lista_programas_onu:
			with open('onu_agencias.txt','a+',encoding = 'utf-8') as archivo:
				archivo.write(str(agencia) + '\n')
		
		