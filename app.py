import pickle
import streamlit as st
import bz2

#to recommend a list of games related to the selected game, it uses cosine similarity from sklearn

def recommend(game):
    index = games[games['name'] == game].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_game_names = []
    for i in distances[1:11]:
        # fetch the game poster
        game_id = games.iloc[i[0]]['name']
        recommended_game_names.append(games.iloc[i[0]]['name'])
        
    return recommended_game_names

#Header for the app
st.header('Game Recommender')

#Opening the Pickle file with read binary and bz2 is used to compress and read compressed file
gf1 = bz2.BZ2File("model/games_list",'rb')
games = pickle.load(gf1)

gf2 = bz2.BZ2File("model/similarity",'rb')
similarity = pickle.load(gf2)
#games = pickle.load(open('model/games_list.pkl','rb'))
#similarity = pickle.load(open('model/similarity.pkl','rb'))

#making a dropdown with all the games present in the list
game_list = games['name'].values
selected_game = st.selectbox(
    "Type or select a game from the dropdown",
    game_list
)

#on click show a range of related games
if st.button('Show Recommendation'):
    recommended_game_names = recommend(selected_game)
    for i in range(10):
        st.text(recommended_game_names[i])
        
        
#Hiding the streamlit branding
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
gf1.close()
gf2.close()