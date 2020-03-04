#!/bin/bash

if [ -f wtm_movies.json ];then
	rm -f wtm_movies.json;
fi

scrapy crawl wtm -o wtm_movies.json -t json



