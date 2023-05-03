import pandas as pd
import pickle
import streamlit as st
import requests

st.set_page_config(layout="wide")
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index =movies[movies['title'] == movie].index[0]

    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in distance[0:5]:
        movie_id=movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>",unsafe_allow_html=True)
st.write("")
st.write("")
movie_list=movies['title'].values
selected_movie_name=st.selectbox('Select a movie from the dropdown',movie_list)
st.write("")
if selected_movie_name:
    names,poster=recommend(selected_movie_name)
    # col1, col2, col3, col4, col5,col6,col7,col8,col9=st.columns(9)
    # with col1:
    #     st.write(names[0])
    #     st.image(poster[0],width=180)
    # with col3:
    #     st.text(names[1])
    #     st.image(poster[1],width=180)
    # with col5:
    #     st.text(names[2])
    #     st.image(poster[2],width=180)
    # with col7:
    #     st.text(names[3])
    #     st.image(poster[3],width=180)
    # with col9:
    #     st.text(names[4])
    #     st.image(poster[4],width=180)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        if (len(names[0]) < 40):
            st.write(names[0])
            st.write("")
            st.write("")
        else:
            st.write(names[0])
        coll1,coll2=col1.columns(2)
        with coll1:
         st.image(poster[0], width=180)
    with col2:
        if (len(names[1]) < 38):
            st.write(names[1])
            st.write("")
            st.write("")
        else:
            st.write(names[1])
        coll1, coll2 = col2.columns(2)
        with coll1:
            st.image(poster[1], width=180)
    with col3:
        if (len(names[2]) < 38):
            st.write(names[2])
            st.write("")
            st.write("")
        else:
            st.write(names[2])
        coll1, coll2 = col3.columns(2)
        with coll1:
            st.image(poster[2], width=180)
    with col4:
        if(len(names[3])<38):
            st.write(names[3])
            st.write("")
            st.write("")
        else:
            st.write(names[3])
        coll1, coll2 = col4.columns(2)
        with coll1:
            st.image(poster[3], width=180)
    with col5:
        if (len(names[4]) < 38):
            st.write(names[4])
            st.write("")
            st.write("")
        else:
            st.write(names[4])
        coll1, coll2 = col5.columns(2)
        with coll1:
            st.image(poster[4], width=180)
        st.write("")
        st.caption("Made in India with ❤️ by Manul Rastogi")
