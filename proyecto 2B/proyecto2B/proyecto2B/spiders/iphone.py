import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class AraniaCrawlOnu (CrawlSpider):
	name = 'crawl_iphone'
	
	allowed_domains = ['socialcompare.com']
	
	start_urls = ['http://socialcompare.com/en/comparison/apple-iphone-product-line-comparison']
	
	
	url_segmento_permitido = ('apple-iphone-product-line-comparison')
	
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
		
		modelo = response.css('div.overflowWrapper > #table > #tableHolder > #t > table > thead > tr > th::text').extract()
		procesador = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(23) > td::text').extract()
		camara_frontal = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(21) > td::text').extract()
		rom = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(8) > td::text').extract()
		microsd = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(7) > td::text').extract()
		ram = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(24) > td::text').extract()
		tamanoPantalla = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(10) > td::text').extract()
		resolucionPantalla = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(11) > td::text').extract()
		sim = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(25) > td::text').extract()
		bateria = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(49) > td::text').extract()
		peso = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(5) > td::text').extract()
		fechaL =response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(46) > td::text').extract()
	
		
		serie_modelo = pd.Series(modelo)
		serie_procesador = pd.Series(procesador)
		serie_rom = pd.Series(rom)
		serie_ram = pd.Series(ram)
		serie_microsd = pd.Series(microsd)
		serie_sim = pd.Series(sim)
		
		serie_tamanio = pd.Series(tamanoPantalla)
		serie_pantalla = pd.Series(resolucionPantalla)
		
		serie_bateria = pd.Series(bateria)
		serie_peso = pd.Series(peso)
		serie_lanzamiento = pd.Series(fechaL)
		serie_camara = pd.Series(camara_frontal)
		
		df = pd.DataFrame({"MODELO": serie_modelo,"PROCESADOR":serie_procesador , "ROM": serie_rom, "RAM": serie_ram, "MICROSD":serie_microsd, "SIM":serie_sim, "TAMAÑO PANTALLA":serie_tamanio,
		" RESOLUCION PANTALLA":serie_pantalla, "BATERIA": serie_bateria, "PESO": serie_peso, "FECHA LANZAMIENTO":serie_lanzamiento,"CAMARA FRONTAL":serie_camara})
		
		
		#path_guardado = './datosIphone.xlsx'
		#df_Libro = df.copy()
		#df_Libro.to_excel(path_guardado, index = False)
		
		
		path_guardado = './datosApple.csv'
		df_datos = df.copy()
		df_datos.to_csv(path_guardado, index = False)
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		