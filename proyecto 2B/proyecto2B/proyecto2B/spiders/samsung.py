import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class AraniaCrawlOnu (CrawlSpider):
	name = 'crawl_samsung'
		
	allowed_domains = ['socialcompare.com']
	
	start_urls = ['http://socialcompare.com/en/comparison/samsung-galaxy-s-product-line']
	
	
	url_segmento_permitido = ('samsung-galaxy-s-product-line')
	
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
	
		modelo_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(35) > td::text').extract()
		so = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(2) > td::text').extract()
		rom_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(3) > td::text').extract()
		microsSD_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(4) > td::text').extract()
		ram_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(6) > td::text').extract()
		tamano_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(8) > td::text').extract()
		pantalla_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(9) > td::text').extract()
		tipoPantalla_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(10) > td::text').extract()
		sim_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(16) > td::text').extract()
		bateria_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(23) > td::text').extract()
		peso_Samsung =response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(30) > td::text').extract()
		fechaLanzamiento_Samsung = response.css('div.overflowWrapper > #table > #tableHolder > #t > table.s-t > tbody > tr:nth-child(34) > td::text').extract()
	
		
		serie_modelo = pd.Series(modelo_Samsung)
		serie_so = pd.Series(so)
		serie_rom = pd.Series(rom_Samsung)
		serie_ram = pd.Series(ram_Samsung)
		serie_microsd = pd.Series(microsSD_Samsung)
		serie_sim = pd.Series(sim_Samsung)
		
		serie_tamanio = pd.Series(tamano_Samsung)
		serie_pantalla = pd.Series(pantalla_Samsung)
		serie_tipoPantalla = pd.Series(tipoPantalla_Samsung)
		
		serie_bateria = pd.Series(bateria_Samsung)
		serie_peso = pd.Series(peso_Samsung)
		serie_lanzamiento = pd.Series(fechaLanzamiento_Samsung)
		
		df = pd.DataFrame({"MODELO": serie_modelo,"SO":serie_so , "ROM": serie_rom, "RAM": serie_ram, "MICROSD":serie_microsd, "SIM":serie_sim, "TAMAÑO PANTALLA":serie_tamanio,
		" RESOLUCION PANTALLA":serie_pantalla, "TIPO PANTALLA": serie_tipoPantalla, "BATERIA": serie_bateria, "PESO": serie_peso, "FECHA LANZAMIENTO":serie_lanzamiento})
		
		path_guardado = './datosSamsung.csv'
		df_datos = df.copy()
		df_datos.to_csv(path_guardado, index = False)
	
			