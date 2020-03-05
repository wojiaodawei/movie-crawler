# Web crawler for AlloCiné (allocine.fr)

~~ *This project was implemented in October 2017* ~~

AlloCiné is an entertainment website providing content on cinema.

[*Scrapy*](https://scrapy.org/), a web-crawling framework in Python, is used.

Information collected about all the films listed on Allociné.fr is as follows:
* url
* title
* img_url
* synopsis
* release_date
* director
* cast
* genres
* countries
* runtime
* press_rating
* public_rating

To launch the spiderbot *wtm* browsing the website, type:
```
./crawling.sh 
```

Collected data is encoded in JSON format in a single file *wtm_movies.json*.

Then use the script *splitJSON.py* to split each of the extracted movies (in JSON format) individually in the directory *movies/*.
