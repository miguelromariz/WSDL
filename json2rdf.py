import json
import string
import datetime
import pytz
import re

allowed_movies = False
#allowed_movies = set(["Pulp Fiction", "Inglourious Basterds", "Reservoir Dogs", "Kill Bill: Vol. 2", "The Hateful Eight"])


def redux_movie(m):
    return "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(m).replace(" ", ""))))

def init_movie(movie_name, date, type, duration, genre):
    redux = "".join(list(filter(lambda c: str.isalnum(c) or c == ' ', string.capwords(movie_name).replace(" ", ""))))
    comm = movie_name.replace("&", "and")
    genre2 = genre.replace(",", "")

    file1 = open("rdfs\moviesRdfs.owl","a")
    

    rdf = f"""<!--     <owl:NamedIndividual rdf:about="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{redux}">
        <rdf:type rdf:resource="http://www.semanticweb.org/wsdl/ontologies/2021/11/showinsight-ontology-12#{type}"/>
        <genre>{genre2}</genre>
        <release_date>{date}</release_date>
        <synopsis>Very cool resource</synopsis>
        <title>{comm}</title>
        <total_duration rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{duration}</total_duration>
    </owl:NamedIndividual> -->"""

    file1.write(rdf)
    file1.write("\n")

    return rdf

def init_director(director, d):
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

    return rdf

def prepare_dir_rdf(file):
    dir_rdf = {}
    with open(file, "r") as f:
        d = json.loads(f.read())
        for dirs in d.keys():
            dir_rdf[dirs] = init_director(dirs, d)

    return dir_rdf

def prepare_movie_rdf(file):
    movie_rdf = {}
    count = 0
    with open(file, "r") as f:
        d = json.loads(f.read())
        for mov in d.keys():
            if(count != 20):
                movie_rdf[mov] = init_movie(mov, int(d[mov][1]), d[mov][2], d[mov][3], d[mov][4])
            else: break
            count+=1
            
    return movie_rdf

def prepare_act_rdf(file):
    act_rdf = {}
    with open(file, "r") as f:
        d = json.loads(f.read())
        for act in d.keys():
            act_rdf[act] = init_actor(act, d)

    return act_rdf

def print_t(t):
    for k in t.keys():
        if t[k]:
            print(t[k])
            print("")
def main():
    t = prepare_movie_rdf(".\jsons\movieTitles.json")
    print_t(t)

if __name__ == '__main__':
    main()