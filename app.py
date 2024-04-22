import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Function to check if a URL is likely to be phishing
def is_phishing(url):
    # Check if the URL contains the word "phishing"
    return "phishing" in url.lower()

# Function to get the HTML content of a webpage
def get_html_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        pass
    return None

# Streamlit app
def main():
    st.title("URL Phishing Detection")
    st.write("Enter a URL below to check if it's a phishing URL or not.")

    # Input field for the URL
    url = st.text_input("Enter URL:", "")

    # Detect phishing button
    if st.button("Detect Phishing"):
        if url:
            if is_phishing(url):
                st.error("This URL is likely a phishing URL!")
            else:
                st.success("This URL seems safe.")

            # Display the website preview
            st.subheader("Website Preview")
            html_content = get_html_content(url)
            if html_content:
                # Create iframe to embed website preview
                st.write(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)
            else:
                st.warning("Failed to retrieve website content.")
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()
