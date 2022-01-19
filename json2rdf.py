import json
import string
import datetime
import pytz
import re

def createMovieRDF(movieTitle, movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime,movieGenre, movieIMDBscore, movieMetacriticScore, movieRottenTomatoesScore,movieWriters, movieCast, movieAwards, type):
    titleNoSpaces = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(movieTitle).replace(" ", ""))))
    title = movieTitle.replace("&", "and")

    if( movieCountry == "" ): movieCountry = "Unknown"
    if( movieLanguage == "" ): movieLanguage = "Unknown"
    if( movieReleaseDate == "" ): movieReleaseDate = "Unknown"
    if( movieRunTime == "" ): movieRunTime = "Unknown"
    if( movieDirector == "" ): movieDirector = "Unknown"
    if( movieGenre == ""): movieGenre = "Unknown"
    if(movieAwards == "" or movieAwards == "N/A"): movieAwards = "0"

    nameaux = movieDirector.replace(" ", "")
    movieDirector = nameaux.replace("_", "")

    actorsArray = movieCast.split(', ')
    writersArray = movieWriters.split(', ')

    file1 = open("rdfs\series.owl","a")
    

    rdf =f'''<!--     <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{type}"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment1"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment2"/>
                <hasScore rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}Score"/>
                <country>{movieCountry}</country>
                <genre>{movieGenre}</genre>
                <language>{movieLanguage}</language>
                <release_date>{movieReleaseDate}</release_date>
                <synopsis>{movieAbstract}</synopsis>
                <title>{title}</title>
                <total_duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{movieRunTime}</total_duration>
                <awards> {movieAwards} </awards> \n'''

    if movieDirector != "Unkwnown":
        rdf += f'''                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{movieDirector}"/>\n'''

    if movieWriters != 'N/A':
        for writerName in writersArray:
            nameaux = writerName.replace(" ", "")
            name = nameaux.replace("_", "")
            if name != movieDirector:
                rdf += f'''                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    if movieCast != '':
        for actorName in actorsArray:
            nameaux = actorName.replace(" ", "")
            name = nameaux.replace("_", "")
            rdf += f'''                <hasCast rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''


    rdf += '''        </owl:NamedIndividual> -->\n'''

    scoreRdf = f'''<!--         <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}Score">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Score"/>
                <classifies rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}"/>
                <imdb_score rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{movieIMDBscore}</imdb_score>
                <metacritic_score rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{movieMetacriticScore}</metacritic_score>
                <rottentotomatoes_score rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">{movieRottenTomatoesScore}</rottentotomatoes_score>
            </owl:NamedIndividual> -->\n'''

    file1.write(rdf)
    file1.write("\n")
    file1.write(scoreRdf)
    file1.write("\n")

    return rdf

def createSeriesRDF(seriesTitle, seriesIRI, seriesAbstract, seriesLanguage, seriesRelease, seriesCompletion, seriesProducer, seriesExecutiveProducer, seriesEpisodes, seriesSeasons, seriesEpisodeDuration,seriesCountry, seriesGenre,seriesIMDBscore, seriesMetacriticScore,seriesRottenTomatoesScore,seriesWriters, seriesCast, seriesAwards, type):
    titleNoSpaces = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(seriesTitle).replace(" ", ""))))
    title = seriesTitle.replace("&", "and")

    if( seriesLanguage == "" ): seriesLanguage = "Unknown"
    if( seriesRelease == "" ): seriesRelease = "Unknown"
    if( seriesCompletion == "" ): seriesCompletion = "Unknown"
    if( seriesProducer == "" ): seriesProducer = "Unknown"
    if( seriesExecutiveProducer == "" ): seriesExecutiveProducer = "Unknown"
    if( seriesCountry == ""): seriesCountry="Unknown"
    if( seriesGenre == ""): seriesGenre = "Unknown"
    if( seriesAwards == "" or seriesAwards == "N/A"): seriesAwards = "0"

    totalDuration = int(seriesEpisodes) * float(seriesEpisodeDuration)

    #Parse arrays
    actorsArray = seriesCast.split(', ')
    producersArray = seriesProducer.split(', ')
    executiveProducersArray = seriesExecutiveProducer.split(', ')
    writersArray = seriesWriters.split(', ')

    file1 = open("rdfs\series.owl","a",  encoding="utf8")
    

    rdf =f'''<!--    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{type}"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment1"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment2"/>
                <hasScore rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}Score"/>
                <country>{seriesCountry}</country>
                <episode_duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{seriesEpisodeDuration}</episode_duration>
                <language>{seriesLanguage}</language>
                <genre>{seriesGenre}</genre>
                <nr_episodes rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{seriesEpisodes}</nr_episodes>
                <nr_seasons rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{seriesSeasons}</nr_seasons>
                <release_date>{seriesRelease}</release_date>
                <synopsis>{seriesAbstract}</synopsis>
                <title>{title}</title>
                <total_duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{totalDuration}</total_duration>
                <awards> {seriesAwards} </awards>\n'''

    if seriesProducer != 'Unknown':
        for producerName in producersArray:
            nameaux = producerName.replace(" ", "")
            name = nameaux.replace("_", "")
            rdf += f'''                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    if seriesExecutiveProducer != 'Unknown':
        for execName in executiveProducersArray:
            if(execName not in producersArray):
                nameaux = execName.replace(" ", "")
                name = nameaux.replace("_", "")
                rdf += f'''                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    if seriesWriters != 'N/A':
        for writerName in writersArray:
                nameaux = writerName.replace(" ", "")
                name = nameaux.replace("_", "")
                rdf += f'''                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    if seriesCast != '':
        for actorName in actorsArray:
            nameaux = actorName.replace(" ", "")
            name = nameaux.replace("_", "")
            rdf += f'''                <hasCast rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    rdf += '''        </owl:NamedIndividual> -->\n'''


    scoreRdf = f'''<!--         <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}Score">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Score"/>
                <classifies rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}"/>
                <imdb_score rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{seriesIMDBscore}</imdb_score>
                <metacritic_score rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{seriesMetacriticScore}</metacritic_score>
                <rottentotomatoes_score rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">{seriesRottenTomatoesScore}</rottentotomatoes_score>
            </owl:NamedIndividual> -->\n'''

    file1.write(rdf)
    file1.write("\n")
    file1.write(scoreRdf)
    file1.write("\n")

    return rdf


def prepare_movie_rdf(file):
    movie_rdf = {}
    with open(file, "r") as f:
        movies = json.loads(f.read())
        for moviesTitle in movies.keys():

            movieIRI = movies[moviesTitle][0]
            movieDirector = movies[moviesTitle][1]
            movieAbstract = movies[moviesTitle][2]
            movieCountry = movies[moviesTitle][3]
            movieLanguage = movies[moviesTitle][4]
            movieReleaseDate = movies[moviesTitle][5]
            movieRunTime = movies[moviesTitle][6]
            movieGenre = movies[moviesTitle][7]
            movieIMDBscore = movies[moviesTitle][8]
            movieMetacriticScore = movies[moviesTitle][9]
            movieRottenTomatoesScore = movies[moviesTitle][10]
            movieWriters = movies[moviesTitle][11]
            movieCast = movies[moviesTitle][12]
            movieAwards = movies[moviesTitle][13]

            type = movies[moviesTitle][14]
            
            movie_rdf[moviesTitle] = createMovieRDF(moviesTitle, movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime,movieGenre, movieIMDBscore, movieMetacriticScore, movieRottenTomatoesScore, movieWriters, movieCast, movieAwards, type)
            
    return movie_rdf

def prepare_series_rdf(file):
    movie_rdf = {}
    with open(file, "r",  encoding="utf8") as f:
        series = json.loads(f.read())
        for seriesTitle in series.keys():

            seriesIRI = series[seriesTitle][0]
            seriesAbstract = series[seriesTitle][1]
            seriesLanguage = series[seriesTitle][2]
            seriesRelease = series[seriesTitle][3]
            seriesCompletion = series[seriesTitle][4]
            seriesProducer = series[seriesTitle][5]
            seriesExecutiveProducer = series[seriesTitle][6]
            seriesEpisodes = series[seriesTitle][7]
            seriesSeasons = series[seriesTitle][8]
            seriesEpisodeDuration = series[seriesTitle][9]
            seriesCountry = series[seriesTitle] [10]
            seriesGenre = series[seriesTitle] [11]
            seriesIMDBscore = series[seriesTitle] [12]
            seriesMetacriticScore = series[seriesTitle] [13]
            seriesRottenTomatoesScore = series[seriesTitle] [14]
            writers = series[seriesTitle] [15]
            cast = series[seriesTitle] [16]
            awards = series[seriesTitle] [17]

            type = series[seriesTitle][18]
            
            movie_rdf[seriesTitle] = createSeriesRDF(seriesTitle, seriesIRI, seriesAbstract, seriesLanguage, seriesRelease, seriesCompletion, seriesProducer, seriesExecutiveProducer, seriesEpisodes, seriesSeasons, seriesEpisodeDuration, seriesCountry, seriesGenre, seriesIMDBscore, seriesMetacriticScore,seriesRottenTomatoesScore,writers, cast, awards,type)
            
    return movie_rdf

def print_t(t):
    for k in t.keys():
        if t[k]:
            print(t[k])
            print("")

def prepareActorsList(file, file2):
    actorsList = {}
    with open(file, "r",  encoding="utf8") as f:
        series = json.loads(f.read())
        for seriesTitle in series.keys():
            cast = series[seriesTitle][16]
            if(cast != ""):
                cast = cast.split(",")
                for actor in cast:
                    if actor not in actorsList:
                        actorsList[actor] = [[],[]]
                        actorsList[actor][1].append(seriesTitle)
                        if "actor" not in actorsList[actor][0]:
                            actorsList[actor][0].append("actor")
                    else: 
                        actorsList[actor][1].append(seriesTitle)
                        if "actor" not in actorsList[actor][0]:
                            actorsList[actor][0].append("actor")

    with open(file2, "r",  encoding="utf8") as f:
        movies = json.loads(f.read())
        for moviesTitle in movies.keys():
            cast = movies[moviesTitle][12]
            if(cast != "" and cast != "N/A"):
                cast = cast.split(",")
                for actor in cast:
                    actor=actor.replace(" ","")
                    if actor not in actorsList:
                        actorsList[actor] = [[],[]]
                        actorsList[actor][1].append(moviesTitle)
                        if "actor" not in actorsList[actor][0]:
                            actorsList[actor][0].append("actor")
                    else: 
                        actorsList[actor][1].append(moviesTitle)
                        if "actor" not in actorsList[actor][0]:
                            actorsList[actor][0].append("actor")
    return actorsList

def prepareDirectorList(file):
    directorsList = {}
    with open(file, "r",  encoding="utf8") as f:
        movies = json.loads(f.read())
        for moviesTitle in movies.keys():
            movieDirector = movies[moviesTitle][1]
            movieDirector = movieDirector.replace("_","")
            if(movieDirector not in directorsList):
                directorsList[movieDirector] = [[],[]]
                directorsList[movieDirector][1].append(moviesTitle)
                if "director" not in directorsList[movieDirector][0]:
                    directorsList[movieDirector][0].append("director")
            else: 
                directorsList[movieDirector][1].append(moviesTitle)
                if "director" not in directorsList[movieDirector][0]:
                    directorsList[movieDirector][0].append("director")
    return directorsList

def prepareWritersList(file, file2):
    writersList = {}
    with open(file, "r",  encoding="utf8") as f:
        series = json.loads(f.read())
        for seriesTitle in series.keys():
            writers = series[seriesTitle][15]
            if(writers != "" and writers != "N/A"):
                writers = writers.split(",")
                ##print(writers)
                for writer in writers:
                    writer = writer.replace(" ","")
                    if writer not in writersList:
                        writersList[writer] = [[],[]]
                        writersList[writer][1].append(seriesTitle)
                        if "writer" not in writersList[writer][0]:
                            writersList[writer][0].append("writer")
                    else: 
                        if "writer" not in writersList[writer][0]:
                            writersList[writer][0].append("writer")
        
    with open(file2, "r",  encoding="utf8") as f:
        movies = json.loads(f.read())
        for seriesTitle in movies.keys():
            writers = movies[seriesTitle] [11]
            if(writers != "" and writers != "N/A"):
                writers = writers.split(",")
                ##print(writers)
                for writer in writers:
                    writer = writer.replace(" ","")
                    if writer not in writersList:
                        writersList[writer] = [[],[]]
                        writersList[writer][1].append(seriesTitle)
                        if "writer" not in writersList[writer][0]:
                            writersList[writer][0].append("writer")
                    else: 
                        writersList[writer][1].append(seriesTitle)
                        if "writer" not in writersList[writer][0]:
                            writersList[writer][0].append("writer")
    return writersList

def prepareProducersList(file):
    producersList = {}
    with open(file, "r",  encoding="utf8") as f:
        series = json.loads(f.read())
        for seriesTitle in series.keys():
            seriesProducer = series[seriesTitle][5]
            if(seriesProducer != "" and seriesProducer != "N/A"):
                seriesProducer = seriesProducer.split(",")
                ##print(writers)
                for producer in seriesProducer:
                    producer = producer.replace(" ","")
                    if producer not in producersList:
                        producersList[producer] = [[],[]]
                        producersList[producer][1].append(seriesTitle)
                        if "writer" not in producersList[producer][0]:
                            producersList[producer][0].append("producer") 
                    else: 
                        producersList[producer][1].append(seriesTitle)
                        if "writer" not in producersList[producer][0]:
                            producersList[producer][0].append("producer")
    #print(len(producersList))
    return producersList

def prepareExecProducersList(file):
    execProducersList = {}
    with open(file, "r",  encoding="utf8") as f:
        series = json.loads(f.read())
        for seriesTitle in series.keys():
            seriesExecutiveProducer = series[seriesTitle][6]
            if(seriesExecutiveProducer != "" and seriesExecutiveProducer != "N/A"):
                seriesExecutiveProducer = seriesExecutiveProducer.split(",")
                ##print(writers)
                for execProducer in seriesExecutiveProducer:
                    execProducer = execProducer.replace(" ","")
                    if execProducer not in execProducersList:
                        execProducersList[execProducer] = [[],[]]
                        execProducersList[execProducer][1].append(seriesTitle)
                        if "writer" not in execProducersList[execProducer][0]:
                            execProducersList[execProducer][0].append("executiveProducer")
                    else: 
                        execProducersList[execProducer][1].append(seriesTitle)
                        if "writer" not in execProducersList[execProducer][0]:
                            execProducersList[execProducer][0].append("executiveProducer")
    #print(len(execProducersList))
    return execProducersList

def mergeLists(list1, list2):
    for key2 in list2.keys():
        if key2 not in list1:
            list1[key2] = list2[key2]
        else:
            #print(list2[key2][0][0])
            list1[key2][0].append(list2[key2][0][0])
            for movie in list2[key2][1]:
                if movie not in list1[key2][1]:
                    list1[key2][1].append(movie)
    return list1

def writeActorsRDF(lista):
    file1 = open("rdfs\series.owl","a",  encoding="utf8")
    rdf=""
    for key in lista.keys():
        key2 = key.replace(" ","")
        key2 = key2.replace("_","")
        rdf += f'''<!--\t<owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{key2}">\n\t\t<rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Cast"/>\n'''
        for movie in lista[key][1]:
            movie = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(movie).replace(" ", ""))))
            movie = movie.replace("&", "and")
            rdf += f'''\t\t<participates rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{movie}"/>\n'''      
        rdf +=f'''\t\t<person_name>{key}</person_name>\n\t</owl:NamedIndividual>-->\n'''
    
    file1.write(rdf)
    file1.write("\n")

    return rdf

def writeStaffRDF(lista):
    file1 = open("rdfs\series.owl","a",  encoding="utf8")
    rdf=""
    for key in lista.keys():
        key2 = key.replace(" ","")
        key2 = key2.replace("_","")
        rdf += f'''<!--\t<owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{key2}">\n'''

        for movie in lista[key][1]:
            movie = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(movie).replace(" ", ""))))
            movie = movie.replace("&", "and")
            rdf += f'''\t\t<collaborates rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{movie}"/>\n'''

        rdf +=f'''\t\t<person_name>{key}</person_name>\n'''
        
        for role in lista[key][0]:
            rdf +=f'''\t\t<role>{role}</role>\n'''

        rdf+='''\t</owl:NamedIndividual>-->\n'''
    
    file1.write(rdf)
    file1.write("\n")

    return rdf


def main():
    t = prepare_movie_rdf(".\jsons\movies.json")
    f= prepare_series_rdf(".\jsons\series.json")
    actors = prepareActorsList(".\jsons\series.json",".\jsons\movies.json")
    directors = prepareDirectorList(".\jsons\movies.json")
    writers = prepareWritersList(".\jsons\series.json",".\jsons\movies.json")
    producers = prepareProducersList(".\jsons\series.json")
    execProducers = prepareExecProducersList(".\jsons\series.json")

    list = mergeLists(directors, writers)
    list = mergeLists(list, producers) 
    list = mergeLists(list, execProducers)
    #print(list)
    writeActorsRDF(actors)
    writeStaffRDF(list)

if __name__ == '__main__':
    main()