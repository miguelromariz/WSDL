#
import requests
import json

def getScoresAPIs(movieName):
    # get movie / tvshow by title
    idSearch = "http://www.omdbapi.com/?t="+ movieName + "&apikey=b2504522" #api key with 1000 calls per day

    payload = {}
    headers = {}

    genre = ""
    imdbScore = "N/A"
    metacriticScore = "N/A"
    rottenTomatoesScore = "N/A"

    titleResponse = requests.request("GET", idSearch, headers=headers, data=payload)
    movie = json.loads(titleResponse.text)

    if(movie.get("Response") != "False"):    #Movie not found
        genre = movie.get('Genre')
        imdbScore = movie.get('imdbRating')
        ratings = movie.get('Ratings')
        for r in ratings:
            if (r.get('Source') == "Rotten Tomatoes"):
                rottenTomatoesScore = r.get('Value')
            elif (r.get('Source') == "Metacritic"):
                metacriticScore = r.get('Value')

    return {'genre': genre, 'imdb': imdbScore, 'metacritic': metacriticScore, 'rottentomatoes': rottenTomatoesScore}

def main():
    return
      

if __name__ == '__main__':
    main()

