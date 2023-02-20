import pandas as pd
import streamlit as st
import numpy as np
from streamlit import caching


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

@st.cache
def random():
    df = pd.read_csv("./data/output.csv")
    random = df.sample(4)
    random.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']
    random.columns = ['hanzi', 'pinyin', 'spanish']
    return random

random=random()

ask=random['pinyin']['Row_1']
correct=random['spanish']['Row_1']
answers=random['spanish'].sample(3)
st.write('pinyin: {}'.format(ask))
st.write(ask,correct)

for answer in answers:
    if st.button(answer):
        if str(answer) == str(correct):
            st.success('This is a success message!')
    else:
        pass
    #st.write('Goodbye')
