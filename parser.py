import csv
import json
#import imdb


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
            type = "Movie"
            movies[movieTitle] = [movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime, type]

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
            if seriesEpisodeDuration != "":
                seriesEpisodeDuration = str(abs(float(seriesEpisodeDuration))/60)            
            type = "TVSeries"
            movies[seriesTitle] = [seriesIRI, seriesAbstract, seriesLanguage, seriesRelease, seriesCompletion, seriesProducer, seriesExecutiveProducer, seriesEpisodes, seriesSeasons, seriesEpisodeDuration, type]

        firstline = False
    
    with open('jsons\series.json', 'w', encoding="utf8") as outfile:
        json.dump(movies, outfile, ensure_ascii=False, indent=2)

def filterMovies():
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
    createMoviesJson()
    #createSeriesJson()    
    
    

if __name__ == '__main__':
    main()



    
    
