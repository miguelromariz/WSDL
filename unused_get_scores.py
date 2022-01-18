import requests
import imdb

def getScoresAPIs(movieName):
    # name
    idSearch = "https://imdb-api.com/en/API/SearchMovie/k_27jpecqz/" + movieName

    payload = {}
    headers = {}

    imdbScore = "Unknown"
    metacriticScore = "Unknown"
    rottenTomatoesScore = "Unknown"

    titleResponse = requests.request("GET", idSearch, headers=headers, data=payload)
    result = titleResponse.json().get('results')
    print(result)
    if(len(result) > 0):
        id = result[0].get('id')

        url = "https://imdb-api.com/en/API/Ratings/k_27jpecqz/" + id    #api key (imdb-api.com) c/ limite de 100 runs por dia

        response = requests.request("GET", url, headers=headers, data=payload)
        errorMsg = response.json().get('errorMessage')


        if errorMsg == "":
            imdbScore = response.json().get('imDb')
            metacriticScore = response.json().get('metacritic')
            rottenTomatoesScore = response.json().get('rottenTomatoes')


    return {'imdb': imdbScore, 'metacritic': metacriticScore, 'rottentomatoes': rottenTomatoesScore}

def main():
    res = getScoresAPIs("Do the Right Thing: Original Motion Picture Score")   

if __name__ == '__main__':
    main()


