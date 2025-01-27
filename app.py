import streamlit as st #1. streamlit imported
import pickle
import pandas as pd

#   9. recommend ka function jo button walay code kay andar call hoga
def recommend(game):
        game_index = games[games['title'] == game].index[0]
        # 10 similarity matrix wapis pickle kay through imported
        distances = similarity[game_index]
        games_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_games = []
        for i in games_list:
            recommended_games.append(games.iloc[i[0]].title)
        return recommended_games

#11 similarity pickle file say yahan imported
similarity=pickle.load(open('similarity.pkl', 'rb'))

#5. games_list may pickle say aay wala dataframe hoga
games_dict=pickle.load(open('game_dict.pkl', 'rb'))
#6. games_list kay values column ki values saari stored usmay hee
games=pd.DataFrame(games_dict)

#2. Streamlit library used to create interface
#3. st.title main heading of the page
st.title('Videogame Recommender System')

#adding select box where the game can be selected
selected_game_name=st.selectbox(
    'Please select a game to generate recommendations', #Info line
    (games['title'].values) #7.   Options where you can select the game from

)

# 8. Button ka code
# Button kay click pay jo selected naam hai wo function kay andar ja kay
if st.button('Generate recommendations'):
    recommendation=recommend(selected_game_name)
    for i in recommendation:
        st.write(i)

