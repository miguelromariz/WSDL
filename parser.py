import csv
import json

from getScores import getScoresAPIs


def createMoviesJson():
    movies = {}
    count = 0
    file = open("moviesFiltered.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    firstline = True

    for line in data:
        if(not firstline):
            movieIRI = line[0]
            movieTitle = line[1]
            movieDirector = line[2]
            movieAbstract = line[3]
            movieCountry = line[4]
            movieLanguage = line[5]
            movieReleaseDate = line[6]
            movieRunTime = line[7]

            if movieRunTime != "":
                movieRunTime = str(float(movieRunTime)/60)

            if movieLanguage.find("http://")!=-1:
                movieLanguageAux = movieLanguage.split("resource/",1) [1]
                movieLanguage = movieLanguageAux.split("_language",1)[0]

            if movieCountry.find("http://")!=-1:
                movieCountry = movieCountry.split("resource/",1) [1]

            if movieDirector.find("http://")!=-1:
                movieDirector = movieDirector.split("resource/",1)[1]

            type = "Movie"
            
            scores = getScoresAPIs(movieTitle)
            movieGenre = scores.get('genre')
            movieIMDBscore = scores.get('imdb')
            movieMetacriticScore = scores.get('metacritic')
            movieRottenTomatoesScore = scores.get('rottentomatoes')

            writers = scores.get('writers')
            cast = scores.get('cast')
            awards = scores.get('awards')       

            #count += 1
            #print("LINHA:" + str(count))

            movies[movieTitle] = [movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime,movieGenre, movieIMDBscore, movieMetacriticScore, movieRottenTomatoesScore, writers, cast, awards, type]

        firstline = False
    
    with open('jsons\movies.json', 'w', encoding="utf8") as outfile:
        json.dump(movies, outfile, ensure_ascii=False, indent=2)

def createSeriesJson():
    movies = {}
    count = 0
    file = open("seriesFiltered.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    firstline = True

    for line in data:
        if(not firstline):
            seriesIRI = line[0]
            seriesTitle = line[1]
            seriesAbstract = line[2]
            seriesLanguage = line[3]
            seriesRelease = line[4]
            seriesCompletion = line[5]
            seriesProducer = line[6]
            seriesExecutiveProducer = line[7]
            seriesEpisodes = line[8]
            seriesSeasons = line[9]
            seriesEpisodeDuration = line[10]
            seriesCountry = line[11] 
            seriesGenre = line[12]

            #Parse episode duration    
            if seriesEpisodeDuration != "":
                seriesEpisodeDuration = str(abs(float(seriesEpisodeDuration))/60)       
            
            #Parse language url  
            if seriesLanguage.find("http://")!=-1:
                seriesLanguageAux = seriesLanguage.split("resource/",1) [1]
                seriesLanguage = seriesLanguageAux.split("_language",1)[0]

            #Parse country url
            if seriesCountry.find("http://")!=-1:
                seriesCountry = seriesCountry.split("resource/",1) [1]

            #Parse producer url
            if seriesProducer.find("http://")!=-1:
                seriesProducer = seriesProducer.split("resource/",1)[1]

            #Parse executive producer url
            if seriesExecutiveProducer.find("http://")!=-1:
                seriesExecutiveProducer = seriesExecutiveProducer.split("resource/",1)[1]

            #Parse genre url
            if seriesGenre.find("http://")!=-1:
                seriesGenre = seriesGenre.split("resource/",1)[1]
            if(seriesGenre.find("_series")!=-1):                         #Animated_series p.ex.
                seriesGenre = seriesGenre.split("_series",1)[0] 
            if(seriesGenre.find("_(genre)")!=-1):                        #Western_(genre) p.ex. 
                seriesGenre = seriesGenre.split("_(genre)",1)[0]
            if(seriesGenre.find("_film")!=-1):                           #Action_film p.ex.
                seriesGenre = seriesGenre.split("_film",1)[0]

            scores = getScoresAPIs(seriesTitle)
            seriesIMDBscore = scores.get('imdb')
            seriesMetacriticScore = scores.get('metacritic')
            seriesRottenTomatoesScore = scores.get('rottentomatoes')

            writers = scores.get('writers')
            cast = scores.get('cast')
            awards = scores.get('awards')

            #count += 1
            #print("LINHA:" + str(count))

            type = "TVSeries"
            movies[seriesTitle] = [seriesIRI, seriesAbstract, seriesLanguage, seriesRelease, seriesCompletion, seriesProducer, seriesExecutiveProducer, seriesEpisodes, seriesSeasons, seriesEpisodeDuration, seriesCountry, seriesGenre,seriesIMDBscore, seriesMetacriticScore,seriesRottenTomatoesScore, writers, cast, awards, type]

        firstline = False
    
    with open('jsons\series.json', 'w', encoding="utf8") as outfile:
        json.dump(movies, outfile, ensure_ascii=False, indent=2)

def filterMovies():
    file = open("movies.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    file2 = open('moviesFiltered.tsv', 'a+', encoding="utf8", newline='')
    writer = csv.writer(file2, delimiter='\t')
    count = 0
    titulos = []
    for row in data:
        ##print(titulos)
        ##print(row[0])
        if row[0] not in titulos:
            print(row[0])
            writer.writerow(row)
            count+=1
        titulos.append(row[0])
    print(count)

def filterSeries():
    file = open("series.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    file2 = open('seriesFiltered.tsv', 'a+', encoding="utf8", newline='')
    writer = csv.writer(file2, delimiter='\t')
    count = 0
    titulos = []
    for row in data:
        ##print(titulos)
        ##print(row[0])
        if row[0] not in titulos:
            print(row[0])
            writer.writerow(row)
            count+=1
        titulos.append(row[0])
    print(count)


def main():
    #filterMovies()
    #filterSeries()

    #print("------------MOVIES-------------")
    createMoviesJson()
    #print("------------SERIES-------------s")
    #createSeriesJson()    
    
    

if __name__ == '__main__':
    main()



    
    
