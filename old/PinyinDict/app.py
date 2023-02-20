import streamlit as st
import pandas as pd

from mydb import *


def main():
    st.title('Pinyin Dictionary')

    menu = ['create', 'read', 'delete']
    choice = st.sidebar.selectbox('menu', menu)

    create_table()
    if choice == 'create':

        col1, col2 = st.columns(2)

        with col1:
            word = st.text_input('something')

        if st.button('add word'):
            add_data(word)
            st.success('successfully added word into bbdd:{}'.format(word))

if __name__ == '__main__':
    main()
