# -*- coding: utf-8 -*-
import scrapy
import string
import urlparse

from wtm.items import *

class WtmSpiderSpider(scrapy.Spider):
    name = "wtm"
    allowed_domains = ["allocine.fr"]
    start_urls = (
        'http://www.allocine.fr/films/',
    )

    def parse(self, response):
        nb_pages = int(response.css('span.button.item::text').extract()[-1].encode('utf-8'))
        yield scrapy.Request(response.url, callback=self.parseMoviesList) 
        for i in range(2, nb_pages + 1):
            yield scrapy.Request(urlparse.urljoin(response.url, '?page=' + str(i)), callback=self.parseMoviesList)

    def parseMoviesList(self, response):
	for movie_card in response.css('div.card.card-entity.card-entity-list.cf.hred'):
            # si notes presse + spectateurs
	    if len(movie_card.css('div.rating-holder div.stareval.stareval-medium').extract()) == 2:
                relative_link = movie_card.css("a.meta-title-link::attr(href)").extract_first().encode('utf-8')
		yield scrapy.Request(urlparse.urljoin(response.url, relative_link), callback=self.parseMovie)

    def parseMovie(self, response):
        movie = Movie()
        movie['url'] = response.url
        movie['title'] = response.css('div.titlebar-title.titlebar-title-lg::text').extract_first().encode('utf-8')
        movie['img_url'] = response.css('img.thumbnail-img::attr(src)').extract_first().encode('utf-8')
        movie['release_date'] = response.css('div.meta-body-item span.date::text').extract_first().encode('utf-8')
        runtime = ''
        for el in response.css('div.meta-body-item::text').extract():
            a = el.encode('utf-8').strip()
            if a != '' and ('h' in a or 'min' in a):
                runtime = a[1:-1]
                break
        movie['runtime'] = runtime
        movie['synopsis'] = response.css('div.synopsis-txt::text').extract_first().encode('utf-8')
        genres = []
        for g in response.css('span[itemprop="genre"]::text').extract(): 
            genres += [g.encode('utf-8')]
        movie['genres'] = genres
        countries = []
        for c in response.css('span.nationality::text').extract(): 
            countries += [c.encode('utf-8')]
        movie['countries'] = countries
        ratings = response.css('div.rating-holder span.stareval-note::text').extract()
        movie['press_rating'] = ratings[0].encode('utf-8').strip()
        movie['public_rating'] = ratings[1].encode('utf-8').strip()

        movie_id = response.url.split('http://www.allocine.fr/film/fichefilm_gen_cfilm=')[1][:-5]
        yield scrapy.Request('http://www.allocine.fr/film/fichefilm-' + str(movie_id) + '/casting/', callback=self.parseCasting, meta={'movie': movie})
    
    def parseCasting(self, response):
        movie = response.meta.get('movie')
        directors = {}
        for d in response.css('section.section.casting-director div.card.card-person'):
            img_url = d.css('img.thumbnail-img::attr(src)').extract_first().encode('utf-8')
            name = d.css('span[itemprop="name"]::text').extract_first().encode('utf-8')
            directors[name] = img_url
        movie['director'] = directors
        casting = {}
        for c in response.css('section.section.casting-actor div.card.card-person'):
            img_url = c.css('figure.thumbnail img::attr(data-src)').extract_first().encode('utf-8')
            name = c.css('span[itemprop="name"]::text').extract_first().encode('utf-8')
            casting[name] = img_url
        if len(casting) > 0:
            movie['cast'] = casting
            return movie
