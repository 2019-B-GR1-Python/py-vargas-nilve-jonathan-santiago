# Scrapy 
## Scrapy instalcion

Ejecutar dentro del `anaconda prompt`.
```
$ conda install -c conda-forge scrapy

```
## Comandos Generales

Da `las caracteristicas` para poder hacer web scraping o web 
```
$ scrapy bench

```

Vizualizar las `configuraciones extra`

```
$ scrapy  settings

```
Visualizamos la `version` de Scrapy

```
$ scrapy version

```

```
$ scrapy view `url`

$ scrapy view https://www.pluralsight.com/authors


```
NO se ve el contenido
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT  no se ve el contenido del sri porque atras hay los servidores que nos redirecciona.
```



### Scrapy shell `url`
Permite interacruar con la respuesta del scrapy
```

 $ scrapy shell http://quotes.toscrape.com/
```

acceder a alas propiedades por etiqueta 
```
$response.css('title').extract()   
```

acceder a alas propiedades por etiqueta 
```
$response.css('title::text').extract()   
```
acceder a alas propiedades por clase
```
$response.css('.author::text').extract()

```
extraer un elemento de la lista.. devuelve un selector.
```
$ response.css('.author::text').extract()[0]
$ response.css('.author::text')[0]
$ response.css('.author::text')[0].extract()

```

extraer el primer elemento
```
$ response.css('.author::text').extract_first()

```

clases dentro de clases
```
$len(response.css('div.tags>a.tag::text').extract())
$(response.css('div.tags a.tag::text').extract()) 
$(response.css('.tags .tag::text').extract()) 
```

extrer los links

```
$(response.css('div.quote > span > a::attr(href)').extract())
```

xpath, extraer los titulos

```
$response.xpath('/html/head/title').extract()
```


```
$ response.xpath('/html/body/div[1]/div[2]/div[2]/h2').extract()
```


extraer el texto con xpath 
```
$ response.xpath('/html/body/div[1]/div[2]/div[2]/h2/text()').extract()
```

extraer el primer link
```
$response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```