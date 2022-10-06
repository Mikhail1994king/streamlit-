from filecmp import clear_cache
from readline import clear_history

from tkinter.tix import COLUMN
from traceback import clear_frames
from typing_extensions import Self
import streamlit as st
import pandas as pd
import twint
import streamlit as st

import pandas as pd

import numpy as np
from textblob import TextBlob
import plotly.express as px
import altair as alt
import snownlp as SnowNLP
import os
from spacy.lang.en import English
nlp = English
from spacy.lang.ru import Russian
nlp2 = Russian






with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    limit = st.slider('How many tweets do you want to get?', 
                        min_value=0, 
                        max_value=1000, 
                        step=1)
    output_csv = st.radio('Save a CSV file?', 
                            ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submit_button = st.form_submit_button(label='Search')
if submit_button:
    c = twint.Config()
    c.Search = search_term
    c.Limit = limit
    c.Store_csv = True
    if c.Store_csv:
        c.Output = f'{file_name}.csv'
    twint.run.Search(c)
    data = pd.read_csv(f'{file_name}.csv', 
                        usecols=['date','tweet'])
    st.table(data)





column_tweet = pd.read_csv(f'{file_name}.csv', 
                        usecols=['tweet'])







try:
    st.write(column_tweet)
except ValueError:
    pass
dict= {
    'tweet': column_tweet}


@st.experimental_memo
def square(x):
    return x**2

if st.button("Clear Square"):
    # Clear square's memoized values:
    for i in column_tweet:
        del (i)

if st.button("Clear All"):
    # Clear values from *all* memoized functions:
    st.experimental_memo.clear()



@st.cache(allow_output_mutation=True)
def mutable_cache():
    return  column_tweet
mutable_object = mutable_cache()

if st.button("Clear history cache"):
    mutable_object.clear()




tweet_data = pd.DataFrame(dict, columns = ["t"])


tweetstr = tweet_data['t'].to_string()







tokens2 = nlp(column_tweet)



try:
    for sent in tokens.sents:
        st.write(sent.string.strip())
except ValueError:
    os.remove(column_tweet)
    


s2 =TextBlob(sent)


try:
    st.write(sent.sentiment)
except ValueError:
    pass





def textblob_polarity(tweet_data):
    polarity = []
    for mess in tweet_data:
        mood = TextBlob(mess)
        polarity.append(mood.sentiment.polarity)
    return polarity

textblob_polarity = textblob_polarity(tweet_data)
tweet_data['textblob_polarity'] = textblob_polarity


def remove_floats(row):
    if isinstance(row, str):
        return row
    else:
        return None

for i in tweet_data:
    tweet_data.apply(lambda i: remove_floats(i))







def main():
    st.title("Twitter sentiment analysis")
    st.subheader("Hello streamlit")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        with st.form(key="Nlp form"):
            st.write(tweet_data)
            submit_button= st.form_submit_button(labe=1)

        
        col1,col2 =st.columns
        if submit_button:
            with col1:
                st.info("Results")
                sentiment = TextBlob(tweet_data).sentiment
                st.write(sentiment)
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

            with col2:
                st.info("Sentence Sentiment")




try:
    main
except ValueError:
    pass



def convert_to_df(sentiment_result):
    sentiment_dict = {"polarit": sentiment.polarity, "subjectivity": sentiment.subjectivity}
    sentiment_df = pd.DataFrame(dict(sentiment_result.items(), columns=["metric",'value']))
    return sentiment_df






