import requests

def recommmend(df,movie,similarity):
    # Getting index of the movie
    index = df[df['title'] == movie].index[0]
    
    # Sorting the Distances of the vectors  
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    # Getting Top 5 Similar Movies
    movie_names=[]
    movie_posters=[]
    for i in distances[1:6]:
        movie_id=df.iloc[i[0]].movie_id
        # i[0] -> Gives Index
        movie_posters.append(fetch_poster(movie_id))
        movie_names.append(df.iloc[i[0]].title)
        
    return movie_names,movie_posters

def fetch_poster(movie_id):
    response=requests.get(url="https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data=response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

