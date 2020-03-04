# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Movie(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    synopsis = scrapy.Field()
    release_date = scrapy.Field()
    director = scrapy.Field()
    cast = scrapy.Field()
    genres = scrapy.Field() 
    countries = scrapy.Field() 
    runtime = scrapy.Field() 
    press_rating = scrapy.Field() 
    public_rating = scrapy.Field() 
 
# class Director(scrapy.Item):
#     name = scrapy.Field() 
#     img_url = scrapy.Field() 

# class Actor(scrapy.Item):
#     name = scrapy.Field() 
#     img_url = scrapy.Field() 


