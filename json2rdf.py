import json
import string
import datetime
import pytz
import re

def createMovieRDF(movieTitle, movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime,movieGenre, movieIMDBscore, movieMetacriticScore, movieRottenTomatoesScore, type):
    titleNoSpaces = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(movieTitle).replace(" ", ""))))
    title = movieTitle.replace("&", "and")

    if( movieCountry == "" ): movieCountry = "Unknown"
    if( movieLanguage == "" ): movieLanguage = "Unknown"
    if( movieReleaseDate == "" ): movieReleaseDate = "Unknown"
    if( movieRunTime == "" ): movieRunTime = "Unknown"

    file1 = open("rdfs\movies.owl","a")
    

    rdf =f'''<!--     <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{type}"/>
                <hasAwards rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Award1"/>
                <hasCast rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Actor1"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment1"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment2"/>
                <hasScore rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Score"/>
                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Staff1"/>
                <country>{movieCountry}</country>
                <genre>{movieGenre}</genre>
                <language>{movieLanguage}</language>
                <release_date>{movieReleaseDate}</release_date>
                <synopsis>{movieAbstract}</synopsis>
                <title>{title}</title>
                <total_duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{movieRunTime}</total_duration>
            </owl:NamedIndividual> --> \n'''

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

    totalDuration = int(seriesEpisodes) * float(seriesEpisodeDuration)

    #Parse actors list
    actorsArray = seriesCast.split(', ')
    #print("ACTORS from " + seriesTitle + ": " + str(actorsArray))

    file1 = open("rdfs\series.owl","a",  encoding="utf8")
    

    rdf =f'''<!--    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}">
                <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{type}"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment1"/>
                <hasComments rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Comment2"/>
                <hasScore rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{titleNoSpaces}Score"/>
                <hasStaff rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#Staff1"/>
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
                <awards> {seriesAwards} </awards>'''

    if seriesCast != '':
        rdf += "\n"
        for actorName in actorsArray:
            name = actorName.replace(" ", "")
            rdf += f'''                <hasCast rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{name}"/>\n'''

    rdf += '''            </owl:NamedIndividual> -->\n'''


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
            type = movies[moviesTitle][11]
            
            movie_rdf[moviesTitle] = createMovieRDF(moviesTitle, movieIRI, movieDirector, movieAbstract, movieCountry, movieLanguage, movieReleaseDate, movieRunTime,movieGenre, movieIMDBscore, movieMetacriticScore, movieRottenTomatoesScore, type)
            
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

def main():
    #t = prepare_movie_rdf(".\jsons\movies.json")
    f= prepare_series_rdf(".\jsons\series.json")
    #print_t(t)
    #print_t(f)

if __name__ == '__main__':
    main()



'''
def redux_movie(m):
    return "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(m).replace(" ", ""))))

def prepare_act_rdf(file):
    act_rdf = {}
    with open(file, "r") as f:
        d = json.loads(f.read())
        for act in d.keys():
            act_rdf[act] = init_actor(act, d)

    return act_rdf

def prepare_dir_rdf(file):
    dir_rdf = {}
    with open(file, "r") as f:
        d = json.loads(f.read())
        for dirs in d.keys():
            dir_rdf[dirs] = init_director(dirs, d)

    return dir_rdf'''

'''def init_director(director, d):
    first_name = director.split(",")[-1].strip()
    last_name = director.split(",")[0].strip()
    dtemp = string.capwords(" ".join(director.split(",")[::-1])).replace(" ","")
    dname = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', "".join(dtemp))))
    rdf = f"""
    <!-- http://www.ime.usp.br/~renata/FOAF-modified#{dname} -->
    <owl:NamedIndividual rdf:about="http://www.ime.usp.br/~renata/FOAF-modified#{dname}">
        <rdfs:label>{first_name + " " + last_name}</rdfs:label>
        <rdf:type rdf:resource="http://www.ime.usp.br/~renata/FOAF-modifiedDirector"/>
    """

    tempL = []
    for mov in d[director].keys():
        if d[director][mov].isnumeric():
            if not allowed_movies:
                tempL.append(f'    <renata:FOAF-modifiedmade rdf:resource="http://www.ime.usp.br/~renata/FOAF-modified#{redux_movie(mov)}"/>\n')
            elif mov in allowed_movies:
                tempL.append(f'    <renata:FOAF-modifiedmade rdf:resource="http://www.ime.usp.br/~renata/FOAF-modified#{redux_movie(mov)}"/>\n')
    if tempL == []:
        return ""
    rdf +=  "".join(tempL)
    rdf += f"""
        <renata:FOAF-modifiedfirstName rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{first_name}</renata:FOAF-modifiedfirstName>
        <renata:FOAF-modifiedfamilyName rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{last_name}</renata:FOAF-modifiedfamilyName>
    </owl:NamedIndividual>
    """

    return rdf

def init_actor(actor, d):
    first_name = actor.split(",")[-1].strip()
    last_name = actor.split(",")[0].strip()
    atemp = string.capwords(" ".join(actor.split(",")[::-1])).replace(" ","")
    aname = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', "".join(atemp))))
    rdf = f"""
        <!-- http://www.ime.usp.br/~renata/FOAF-modified#{aname} -->
    <owl:NamedIndividual rdf:about="http://www.ime.usp.br/~renata/FOAF-modified#{aname}">
        <rdfs:label>{first_name + " " + last_name}</rdfs:label>
        <rdf:type rdf:resource="http://www.ime.usp.br/~renata/FOAF-modifiedActor"/>
    """

    tempL = []
    for mov in d[actor].keys():
        if d[actor][mov].isnumeric():
            if not allowed_movies:
                tempL.append(f'    <renata:FOAF-modifiedacts rdf:resource="http://www.ime.usp.br/~renata/FOAF-modified#{redux_movie(mov)}"/>\n')
            elif mov in allowed_movies:
                tempL.append(f'    <renata:FOAF-modifiedacts rdf:resource="http://www.ime.usp.br/~renata/FOAF-modified#{redux_movie(mov)}"/>\n')
    if tempL == []:
        return ""

    rdf +=  "".join(tempL)
    rdf += f"""
        <renata:FOAF-modifiedfirstName rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{first_name}</renata:FOAF-modifiedfirstName>
        <renata:FOAF-modifiedfamilyName rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{last_name}</renata:FOAF-modifiedfamilyName>
    </owl:NamedIndividual>
    """

    return rdf'''