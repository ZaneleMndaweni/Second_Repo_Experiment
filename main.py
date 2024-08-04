#!/usr/bin/env Python3

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__": 
    print("--> Fetching Billboard 100...")
    print()
    billboard_100 = requests.get("https://www.billboard.com/charts/hot-100/")
    soup = BeautifulSoup(billboard_100.text, "html.parser")
    songs = soup.find_all("div", class_ = "o-chart-results-list-row-container")
    

    print("-" * 40)

    for song in songs:
        Song_Details = {}
        Song_Details["No. on Billboard"] = song.find_all("span")[0].text.strip()
        Song_Details["Song Name"] = song.find("h3").text.strip()
        if song.find_all("span")[1].text.strip() == "NEW" or song.find_all("span")[1].text.strip().startswith("RE"):
            Song_Details["Artist"] = song.find_all("span")[3].text.strip() 
        else:
            Song_Details["Artist"] = song.find_all("span")[1].text.strip()
        print(f"No. on Billoard: {Song_Details["No. on Billboard"]}")
        print(f"Song Name: {Song_Details["Song Name"]}")
        print(f"Artist: {Song_Details["Artist"]}")
        print("-" * 40)