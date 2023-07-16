import pandas as pd
import streamlit as st
import docx2txt
import title
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import helper
from io import StringIO
import requests
from bs4 import BeautifulSoup
from PIL import Image
nltk.download('punkt')
st.set_page_config(layout="wide")


st.title("Text Summarization")
user_input = st.radio("Choose ",("Text","File","Link"),horizontal=True)

if user_input == "Text":
    text = st.text_area("Enter Your Text",height=200, placeholder="Enter the Text")
    num_sentences = int(st.number_input("Enter number of Sentences", step=1))
    if st.button('Submit'):
        summary = helper.summary(text,num_sentences)
        p=summary

        title = title.get_heading(text.title())
        st.header(title)

        words = p.split()

        df = pd.read_csv("synonyms.csv")

        filtered_df = df[df['Word'].isin(words)]
        filtered_df = filtered_df.reset_index(drop=True)
        col1, col2 = st.columns(2, gap= "large")

        col1,col2 = st.columns([4,2])
        # col1.header("Summary")
        # col1.write(p)

        with col1.container():
            background_color = "White"
            st.header("Summary")
            N = 1
            current_string = ""

            for i in p:
                if i == ".":
                    if current_string != "":
                        st.write(N, current_string,'.')
                        N += 1
                        current_string = ""
                else:
                    current_string += i
            if current_string != "":
                st.write(N, current_string,'.')
            
            # st.write(p)


        with col2.container():

            col2.header("Synonyms")
            col2.table(filtered_df)
        


elif user_input == "File":
    uploaded_file = st.file_uploader("Choose a file")
    num_sentences = int(st.number_input("Enter number of sentences", step=1))
    if st.button("Submit"):
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        text = stringio.read()
        summary = helper.summary(text,num_sentences)
        #st.write(summary[:])
        p=summary
        
        title = title.get_heading(text.title())
        st.header(title)

        words = p.split()

        df = pd.read_csv("synonyms.csv")

        filtered_df = df[df['Word'].isin(words)]
        filtered_df = filtered_df.reset_index(drop=True)
        col1, col2 = st.columns(2)

        with col1.container():
            background_color = "white"
            st.header("Summary")
            N = 1
            current_string = ""

            for i in p:
                if i == ".":
                    if current_string != "":
                        st.write(N, current_string,'.')
                        N += 1
                        current_string = ""
                else:
                    current_string += i
            if current_string != "":
                st.write(N, current_string,'.')

            #st.write(p)

        with col2.container():

            col2.header("Synonyms")
            col2.table(filtered_df)

else:
    url = st.text_input("Paste URL here", placeholder="Enter URL")
    num_sentences = int(st.number_input("Enter number of sentences", step=1))
    # Get the website content
    if st.button("Submit"):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the article text
        article = soup.body
        text = ""
        for i in article.strings:
            text += i
        summary = helper.summary(text,num_sentences)
        p=summary
        

        title = title.get_heading(text.title())
        st.header(title)
        
        words = p.split()

        df = pd.read_csv("synonyms.csv")

        filtered_df = df[df['Word'].isin(words)]
        filtered_df = filtered_df.reset_index(drop=True)
        col1, col2 = st.columns(2)

        with col1.container():
            background_color = "white"
            st.header("Summary")
            N = 1
            current_string = ""

            for i in summary:
                if i == ".":
                    if current_string != "":
                        st.write(N, current_string,'.')
                        N += 1
                        current_string = ""
                else:
                    current_string += i
            if current_string != "":
                st.write(N, current_string,'.')
                #st.write(p)


        with col2.container():

            col2.header("Synonyms")
            col2.table(filtered_df)

#footer
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
# Add Font Awesome CSS
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)

# Custom CSS code for styling
custom_css = """
<style>
.footer {
  background-color: #262730;
  padding: 20px;
  text-align: center;
}

.social-links {
  list-style-type: none;
  padding: 0;
}

.social-links li {
  display: inline-block;
  margin-right: 10px;
}

.social-links a {
  color: #FAFAFA;
  text-decoration: none;
}

.social-links a:hover {
  color: #007bff;
}
</style>
"""

# Add custom CSS to the app
st.markdown(custom_css, unsafe_allow_html=True)

# Content of your app

# Footer with text and social links
st.markdown(
    """
    <footer class="footer">
      
      <ul class="social-links">
        <li><a href="https://twitter.com/Aniket4548" target="_blank"><i class="fab fa-twitter"></i></a></li>
        <li><a href="https://www.linkedin.com/in/aniket-kumar-4b1b68141/" target="_blank"><i class="fab fa-linkedin"></i></a></li>
        <li><a href="https://github.com/Aniket4548" target="_blank"><i class="fab fa-github"></i></a></li>
        <li><a href="https://www.instagram.com/aniket_kumar_4548/" target="_blank"><i class="fab fa-instagram"></i></a></li>
        <li><a href="mailto:kumaraniket8802@gmail.com"><i class="far fa-envelope"></i></a></li>
      </ul>
      <p>© 2023 Aniket&Mukul, Inc</p>
    </footer>
    """,
    unsafe_allow_html=True
)
