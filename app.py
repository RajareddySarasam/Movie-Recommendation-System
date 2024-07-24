import streamlit as st
import pandas as pd
import pickle 
import helper


Movies_dict=pickle.load(open('Movies_dict.pkl','rb'))
Movies_df=pd.DataFrame(Movies_dict)
# So,Now we Dataframe of Movies.

movies_list=Movies_df['title'].values

similarity=pickle.load(open('similarity.pkl','+rb'))

st.title('Movie Recommendation System')

selected_movie=st.selectbox('Select a Movie',movies_list)



if st.button('Recommend'):
    movie_names,movie_posters=helper.recommmend(Movies_df,selected_movie,similarity)
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(' ')
        st.image(movie_posters[0])
        st.text(movie_names[0])

    with col2:
        st.text(' ')
        st.image(movie_posters[1])
        st.text(movie_names[1])


    with col3:
        st.text(' ')
        st.image(movie_posters[2])
        st.text(movie_names[2])
    
    with col4:
        st.text(' ')
        st.image(movie_posters[3])
        st.text(movie_names[3])
    
    with col5:
        st.text(' ')
        st.image(movie_posters[4])
        st.text(movie_names[4])
    


