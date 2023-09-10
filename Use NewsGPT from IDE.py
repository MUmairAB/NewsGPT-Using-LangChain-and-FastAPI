"""
This script contains the Python code to use NewsGPT from the local IDE. You can replace the "article_url" variable
with your desired news article's URL. Also, replace the "url" variable that stores the API end-point with
your own end-point.
"""

#Import the necessary libraries
import json
import requests

#Public URL for the web server
url = "https://ea78-35-194-207-7.ngrok.io/summary"

#URL of the news article that we want to summarize
article_url = "https://www.theguardian.com/world/2023/sep/10/chinas-good-for-marriage-womens-trend-ignites-social-media-debate"

#Send the GET request to the webserver to summarize the web article
response = requests.get(url=url, params={"URL": article_url})

#Print the response
print("Response Status:", response)

#Print the prediction text
print("Response Text:", response.text)
