#
import requests
import json
import urllib.parse

def getScoresAPIs(movieName):
    # get movie / tvshow by title
    encodeName = urllib.parse.quote(movieName)
    idSearch = "http://www.omdbapi.com/?t="+ encodeName + "&apikey=b2504522" #api key with 1000 calls per day
    
    payload = {}
    headers = {}

    genre = ""
    imdbScore = "N/A"
    metacriticScore = "N/A"
    rottenTomatoesScore = "N/A"
    writers = ""
    cast = ""
    awards = ""

    titleResponse = requests.request("GET", idSearch, headers=headers, data=payload)
    movie = json.loads(titleResponse.text)

    if(movie.get("Response") != "False"):    #Movie not found
        genre = movie.get('Genre')
        writers = movie.get('Writer')
        cast = movie.get('Actors')

        awards = movie.get('Awards')
        imdbScore = movie.get('imdbRating')
        ratings = movie.get('Ratings')
        for r in ratings:
            if (r.get('Source') == "Rotten Tomatoes"):
                rottenTomatoesScore = r.get('Value')
            elif (r.get('Source') == "Metacritic"):
                metacriticScore = r.get('Value')

    return {'genre': genre, 'writers': writers, 'cast':cast, 'awards':awards, 'imdb': imdbScore, 'metacritic': metacriticScore, 'rottentomatoes': rottenTomatoesScore}

def main():
    return
      

if __name__ == '__main__':
    main()

