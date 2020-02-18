import scrapy
import pandas as pd


class IntroSpider(scrapy.Spider):
	name = 'introduccion_spider'
	imagen_url = []
	titles = []
	price = []

			
	
	#definir una funcion
	
	def start_requests(self):
		
		for i in range(1,51):
			urls =[f'http://books.toscrape.com/catalogue/category/books_1/page-{i}.html']
			for url in urls:
				yield scrapy.Request(url=url)
			
	def parse(self,response):
		etiqueta_contenedora = response.css('article.product_pod')
		titulos = etiqueta_contenedora.css('h3 > a::attr(title)').extract()
		imagen = etiqueta_contenedora.css('h3 > a::attr(href)').extract()
		precio = etiqueta_contenedora.css('div.product_price >  p.price_color::text').extract()
			

	
		for i in range(len(titulos)):
			self.imagen_url.append(response.urljoin(imagen[i]))
			self.titles.append(titulos[i])
			self.price.append(precio[i])
		
		
		serie_titulo = pd.Series(self.titles)
		serie_precio = pd.Series(self.price)
		serie_imagen = pd.Series(self.imagen_url)
		
			
		salida = serie_titulo+';'+serie_imagen+';'+serie_precio+'\n'
		
		with open('libros.txt','+a') as file:			
				file.writelines(salida)
            
		df = pd.DataFrame({"TITULOS": serie_titulo, "IMAGEN": serie_imagen, "PRECIO": serie_precio})
		print(f'df {df}')
		
		path_guardado = './libro.xlsx'
		df_Libro = df.copy()
		df_Libro.to_excel(path_guardado, index = True)
		
		
		
		
          
		




