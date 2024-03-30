<h1>At this project I create a simple web page with the function to make shorter url</h1>

Imports used:
<ul>
  <li><a href="https://pyshorteners.readthedocs.io/en/latest/">pyshorteners</a></li>
  ```Python
import pyshorteners
  def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url
  ```
  <li><a href="https://github.com/streamlit/streamlit.git">streamlit</a></li>

```Python
import streamlit as st
#Creation of the web to make the url shortener visual
st.set_page_config(page_title= "URL shortener", page_icon="/", layout="centered")
st.image("image/www.png", use_column_width=True)
st.title("URL shortener")
url = st.text_input("Enter the URL")
if st.button("Generate a nwe URL"):
    st.write("URL shortened: ", shorten_url(url))
```
</ul>
