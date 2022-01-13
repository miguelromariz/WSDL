import csv
import json
import imdb


def createMoviesJson():
    movies = {}
    count = 0
    file = open("filteredMovies.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    firstline = True

    for line in data:
        if(not firstline):
            movieId = line[0]
            movieType = line[1]
            movieTitle = line[3]
            movieDate = line[5]
            movieDuration = line[7]
            movieGenres = line[8]

            if((movieType == "movie" or movieType == "tvSeries") and movieDate != "\\N" and int(movieDate) > 2000):
                count+=1
                print(count)
                movies[movieTitle] = [movieId, movieDate, movieType, movieDuration, movieGenres]

        firstline = False
    
    with open('jsons\movieTitles.json', 'w') as outfile:
        json.dump(movies, outfile, ensure_ascii=False, indent=2)

def filterMovies():
    file = open("movies.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    file2 = open('test.tsv', 'a+', encoding="utf8", newline='')
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
    filterMovies()
    #createMoviesJson()
    #filterTitles()
    
    

if __name__ == '__main__':
    main()

'''ia = imdb.IMDb()
movie = ia.get_movie(movieId)

if 'plot' in movie.keys():
movies[movieTitle].append(movie['plot'][0])
else: movies[movieTitle].append('\\N')

movies[movieTitle].append(movie['country'][0]) '''




    
    
