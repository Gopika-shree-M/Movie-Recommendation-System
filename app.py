import streamlit as st
import pickle
import pandas as pd
import requests

# Proxy configuration
proxy = {
    'http': 'http://154.94.12.38:3128',
    'https': 'http://154.94.12.38:3128',
}

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d3cc62b42360ac6adb74898700e815a0&language=en-US'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except (requests.exceptions.RequestException, requests.exceptions.HTTPError):
        response = requests.get(url, proxies = proxy, timeout = 5)
        response.raise_for_status()
        
    data = response.json()  
    return f"http://image.tmdb.org/t/p/w500/{data['poster_path']}"

# Load movie data and similarity data
movies = pickle.load(open('movies.pkl', 'rb'))
movies_names = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    arr = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:8]
    rec = []
    posters = []
    
    for i in arr:
        rec.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movies.iloc[i[0]].id))
    
    return rec, posters

#Design

background_html = """
    <style>
        body {
            background-color: #ffffff;
        }
    </style>
"""
st.markdown(background_html, unsafe_allow_html=True)

title = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap');
        h1{
            font-size: 40px;
            text-align: left;
            margin-bottom: 30px; 
            padding: 0;
        }
    </style>
    <h1>Movie Recommendation System</h1>
"""
st.markdown(title, unsafe_allow_html=True)

movie = st.sidebar.selectbox(
    "Find your favourite movies",
    movies_names,
    index=None,
    placeholder="Select your Option",
)

dis = movie is None

col1, col2, col3, col4 = st.columns(4)
col5, col6, col7 = st.columns(3)

st.sidebar.markdown('<br>' * 17, unsafe_allow_html=True)

if st.sidebar.button("Recommend movies", disabled=dis):
    recommended_movies, posters = recommend(movie)

    st.sidebar.markdown('<br>', unsafe_allow_html=True)
    with col1:
        st.text(recommended_movies[0])
        st.image(posters[0], width=150)
    with col2:
        st.text(recommended_movies[1])
        st.image(posters[1], width=150)
    with col3:
        st.text(recommended_movies[2])
        st.image(posters[2], width=150)
    with col4:
        st.text(recommended_movies[3])
        st.image(posters[3], width=150)

    st.sidebar.markdown('<br>', unsafe_allow_html=True)

    with col5:
        st.text(recommended_movies[4])
        st.image(posters[4], width=150)
    with col6:
        st.text(recommended_movies[5])
        st.image(posters[5], width=150)
    with col7:
        st.text(recommended_movies[6])
        st.image(posters[6], width=150)
