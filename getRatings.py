from imdb import IMDb
import requests

# create an instance of the IMDb class
ia = IMDb()

def getComments(name):

    if name.find("/")!=-1:
        name = name.split("/",1)[0]

    
    # searching the name 
    movie = ia.search_movie(name)

    if(movie != []):
        id = movie[0].movieID
    
        # get a movie
        movie = ia.get_movie(id)
        
        print("MOVIE:" + movie['title'])

        idSearch = f'''https://imdb-api.com/en/API/Reviews/k_1sgoqh33/tt{id}''' #api key with 1000 calls per day

        '''     Key         ||          Nr utilizações (hoje)
    _______________________________________________________________

            k_27jpecqz      ||              100
            k_1sgoqh33      ||              34
            k_xl3klfyq      ||              90
            k_ys3qbbq2      ||              0
        '''
            
        payload = {}
        headers = {}

        titleResponse = requests.request("GET", idSearch, headers=headers, data=payload)
        reviews = titleResponse.json()['items']

        movieReviews = []

        if reviews == None: reviews = []

        if(len(reviews)>5):
            reviews = reviews[:5]

        for r in reviews:   #First 5 comments
            reviewTitle = r.get('title')
            reviewText = r.get('content')

            movieReviews.append({'comment_title':reviewTitle, 'comment_text':reviewText})
            
        for c in movieReviews:
            print(c)

    else: movieReviews = []
    
    return movieReviews


    