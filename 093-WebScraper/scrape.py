"""
Requirements:
Using what you have learnt about web scraping, scrape a website for data that
you are interested in. Try to build a CSV with the scraped data. What you
scrape is up to you.

Notes:
This is, therefore, another step in my over-elaborate ruse to create automated
Spotify playlists featuring artists active in town over the coming month.
"""
import csv
from  pprint import pprint
import random
import re
import time

from bs4 import BeautifulSoup
import requests


# Default search order is led by who's playing in town today/this/week/month
URL_ROOT = 'https://musiclivecolchester.com'
START_URL = URL_ROOT + '/artists/search?town=colchester'

OUTFILE = 'artists.csv'

SLEEP = 1
NUM_ARTISTS = 30


# TODO: Exception handling
def get_page_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def parse_artist_page(soup: BeautifulSoup) -> tuple:
    artist = soup.h1.text

    # eg https://open.spotify.com/artist/1eHaSUbQG7HYvIOTioukbE
    spotify_url = soup.find('a', href=re.compile(r"open.spotify.com/artist"))

    if spotify_url:
        spotify_id = spotify_url.get('href').split('/')[-1]
        print(f" -> got spotify: {spotify_id}")
        return (artist, spotify_id)


def write_to_file(contents: list):
    with open(OUTFILE, 'w', newline='\n') as fh:
        writer = csv.writer(fh)
        writer.writerows(contents)


def main():

    soup = get_page_soup(START_URL)
    results = soup.select('div.search-output h5 a')
    links = [result.get('href') for result in results]

    found = 0
    artists = []
    for link in links:
        time.sleep(SLEEP)

        URL_ARTIST = URL_ROOT + link

        print(f"getting {URL_ARTIST}")
        soup = get_page_soup(URL_ARTIST)

        artist_dtls = parse_artist_page(soup)

        if artist_dtls:
            artists.append(artist_dtls)
            found += 1

        if found >= NUM_ARTISTS:
            break

    random.shuffle(artists)
    pprint(artists)
    write_to_file(artists)


# main ------------------------------------------------------------------------


if __name__ == '__main__':
    main()
