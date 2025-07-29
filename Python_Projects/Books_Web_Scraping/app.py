import streamlit as st
from books_web_scraping import scrape_books, get_categories

st.title('Books Scraping App')

categories = get_categories().keys()
selected_category = st.selectbox('Select a category:', categories)

if selected_category:
    with st.spinner('Loading...'):
        books_df = scrape_books(selected_category)
    st.markdown(f"### Books in category: {selected_category}")
    st.markdown(books_df.to_markdown(index=False))