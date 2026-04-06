# ## Building streamlit ui

# import streamlit as st
# from scrape import scrape_website

# # Adding a streamlit title

# st.title("AI Web Scrapper")

# # Adding a text input

# url=st.text_input("Enter a Website URL:")

# # Website Scrapping functionality

# if st.button("Scrape Site"):
#     st.write("Scrapping the website")
#     result=scrape_website(url)
#     print(result)

import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from llm_parse import parse_with_ollama

st.title("AI Web Scraper")


url = st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    if url:
        st.write("Scraping the website...")
        result = scrape_website(url)
        body_content=extract_body_content(result)
        clean_content=clean_body_content(body_content)
        
        st.session_state.dom_content=clean_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content",clean_content,height=300)

# Passing the DOM Content into an llm

if "dom_content" in st.session_state:
    parse_description=st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result=parse_with_ollama(dom_chunks,parse_description)
            st.write(result)
