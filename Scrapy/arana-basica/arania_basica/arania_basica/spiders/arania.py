import scrapy

class IntroSpider(scrapy.Spider):
	name = 'introduccion_spider'
	
	urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']
	
	#definir una funcion
	
	def start_requests(self):
		for url in self.urls:
			yield scrapy.Request(url=url)
			
	def parse(self,response):
		etiqueta_contenedora = response.css('article.product_pod')
		#titulos = etiqueta_contenedora.css('h3 > a::text').extract()
		imagen = etiqueta_contenedora.css('a >  img::attr(src)').extract()
	
		#print(f'titulos: {titulos}')
		print(f'imagen: {imagen}')



https://github.com/jonathanvargas2016/proyecto_Moviles.git