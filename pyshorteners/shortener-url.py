import pyshorteners
import streamlit as st
# pyshortener = the shortener tool
# streamlit   = to make easy webs

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#Creation of the web to make the url shortener visual
st.set_page_config(page_title= "URL shortener", page_icon="/", layout="centered")
st.image("image/www.png", use_column_width=True)
st.title("URL shortener")
url = st.text_input("Enter the URL")
if st.button("Generate a nwe URL"):
    st.write("URL shortened: ", shorten_url(url))