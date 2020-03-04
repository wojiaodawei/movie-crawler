#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
#import sys

if __name__ == '__main__':
    #with open(sys.argv[1], 'r') as fichier:
    with open('wtm_movies.json', 'r') as fichier:
        data = json.load(fichier)
    missings = {'url': 0,
                'title': 0,
                'img_url': 0,
                'synopsis': 0,
                'release_date': 0,
                'director': 0,
                'cast': 0,
                'genres': 0,
                'countries': 0,
                'runtime': 0,
                'press_rating': 0,
                'public_rating': 0}
    logs = {}
    movie_id = 1
    for movie in data:
        movie['movie_id'] = movie_id
        if 'Harry' in movie['title']:
            print(movie['title'])
        good = True
        for item in missings:
            if item not in movie:
                good = False
                print("COUCOU JE SUIS LA")
                print(item + " MISSING")
                missings[item] += 1
            elif movie[item] == '' or movie[item] == [] or movie[item] == 0 or movie[item] == {}:
                good = False
                print(item + " VIDE : " + str(movie[item]))
                missings[item] += 1
                cle = item + " VIDE : " + str(movie[item])
                if cle in logs:
                    logs[cle] += [movie['url']]
                else:
                    logs[cle] = [movie['url']]                
        if good:
            with open('movies/'+str(movie_id)+'.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(movie, ensure_ascii=False))
        movie_id += 1                    
    print(missings)
    print(len(data))
    print("\n\n\n")
    for log in logs:
        print(log + '\n')
        print(logs[log])
        print('\n')
