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

        
def filterTitles():
    file = open("data.tsv", encoding="utf8")
    data = csv.reader(file, delimiter="\t")
    file2 = open('filteredRegions.tsv', 'a+', encoding="utf8", newline='')
    writer = csv.writer(file2, delimiter='\t')
    count = 0
    firstLine = True
    for row in data:
        if not firstLine:
            if row[7] == "1" :
                print(row)
                break
                #writer.writerow(row)
        else: writer.writerow(row)
        count+=1
        firstLine = False
        print(count)


def main():
    #filterMovies()
    #createMoviesJson()
    filterTitles()
    
    

if __name__ == '__main__':
    main()

'''ia = imdb.IMDb()
movie = ia.get_movie(movieId)

if 'plot' in movie.keys():
movies[movieTitle].append(movie['plot'][0])
else: movies[movieTitle].append('\\N')

movies[movieTitle].append(movie['country'][0]) 



def filterMovies():
file = open("data.tsv", encoding="utf8")
data = csv.reader(file, delimiter="\t")
file2 = open('test.tsv', 'a+', encoding="utf8", newline='')
writer = csv.writer(file2, delimiter='\t')
count = 0
firstLine = True
for row in data:
if not firstLine:
if row[1] == "movie" or row[1] == "tvSeries":
writer.writerow(row)
else: writer.writerow(row)
count+=1
firstLine = False
print(count)'''
    
    
