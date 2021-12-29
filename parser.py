import csv
import json
data2 = {}


count = 0
file = open("data.tsv", encoding="utf8")
data = csv.reader(file, delimiter="\t")
firstline = True

for line in data:
    if(not firstline):
        movieId = line[0]
        movieType = line[1]
        movieTitle = line[3]
        movieDate = line[5]

        if(movieType == "movie" or movieType == "tvSeries"):
            count+=1
            print(count)
            #print("ID: " + movieId + ", Title: " + movieTitle + ", Type: " + movieType + ", Date: " + movieDate)
            data2[movieTitle] = movieDate
            with open('movieTitles.json', 'w') as outfile:
                json.dump(data2, outfile, indent=2)
    
    firstline = False
    if(count == 10): break




    
    
    
