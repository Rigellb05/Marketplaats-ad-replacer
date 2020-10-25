import time
import pytesseract
from PIL import ImageGrab
import numpy as np
import cv2
import requests
import pyautogui
from bs4 import BeautifulSoup as bs

session = requests.Session()
html = session.get(
    "https://www.marktplaats.nl/a/cd-s-en-dvd-s/blu-ray/m1610386579-blu-ray-the-conjuring-2013-vera-farmiga-patrick-wilson.html?c=3c1f5dcc18d02a99040ca8de656940d2&previousPage=lr")
# create a new soup
soup = bs(html.text, "lxml")

def title_getter():
    results = soup.find("h1", attrs={"id": "title"})
    results = str(results.text)
    return results


def price_getter():
    results = soup.find("span", attrs={"class": "price"})
    results = results.text
    results = results.replace('€ ', '')
    return results


def cat_getter1():
    results = soup.find_all("h2", attrs={"class": "mp-Nav-breadcrumb-item crumb"})
    results = results[1].text
    cat1, sep, cat2 = results.partition("|")
    cat1 = cat1.replace(" ", "")
    return cat1


def cat_getter2():
    results = soup.find_all("h2", attrs={"class": "mp-Nav-breadcrumb-item crumb"})
    results = results[1].text
    cat1, sep, cat2 = results.partition("|")
    cat2 = cat2.replace(" ", "")
    if cat2 == "":
        return "Blu-ray"
    else:
        return cat2


def condition_getter():
    global rs1, rs2, rs3, rs4, rs5
    new = "Nieuw in verpakking"
    results = soup.find_all("td", attrs={"class": "value"})
    rs0 = results[0].text
    try:
        rs1 = results[1].text
    except IndexError:
        rs1 = ""
    try:
        rs2 = results[2].text
    except IndexError:
        rs2 = ""
    try:
        rs3 = results[3].text
    except IndexError:
        rs3 = ""
    try:
        rs4 = results[4].text
    except IndexError:
        rs4 = ""
    try:
        rs5 = results[5].text
    except IndexError:
        rs5 = ""
    listing = [rs0, rs1, rs2, rs3, rs4, rs5]
    if new in listing:
        return True
    elif new not in listing:
        pass


def genre_getter():
    all_list = ("Overige genres", "Overige typen", "Tv en Series", "Thrillers en Misdaad", "Tekenfilms en Animatie",
                "Sport en Fitness", "Science Fiction en Fantasy", "Religie en Gospel", "Nederlandstalig",
                "Muziek en Concerten", "Klassiekers", "Kinderen en Jeudg", "Humor en Cabaret", "Horror", "Filmhuis",
                "Drama", "Documentaire en Educatief", "Avontuur", "Actie", "Non-fictie", "Thriller", "Actie en Avontuur",
                "Komedie", "Actiethriller", "Bovennatuurlijke thriller", "Dectective en Krimi", "Vechtsport", "Voetbal",
                "Yoga, Fitness of Dans", "Overige typen", "Science Fiction", "Fantasy", "Muziek", "Dieren", "Educatief",
                "Poppen", "Actiekomedie", "Romantische komedie", "Gore", "Monsters", "Slasher", "Spoken en Geesten",
                "Vampiers of Zombies", "Historisch of Kostuumdrama", "Waargebeurd drama", "Wetenschap of Techniek",
                "Politiek of Geschiedenis", "Oorlog of Misdaad", "Natuur", "Kunst of Cultuur", "Biografie",
                "Martial Arts")
    results = soup.find_all("td", attrs={"class": "value"})
    try:
        if results[0].text in all_list:
            return results[0].text
    except IndexError:
        pass
    try:
        if results[1].text in all_list:
            return results[1].text
    except IndexError:
        pass
    try:
        if results[2].text in all_list:
            return results[2].text
    except IndexError:
        pass
    try:
        if results[3].text in all_list:
            return results[3].text
    except IndexError:
        pass
    try:
        if results[4].text in all_list:
            return results[4].text
    except IndexError:
        pass
    try:
        if results[5].text in all_list:
            return results[5].text
    except IndexError:
        pass


def period_getter():
    all_list = ("Voor 1940", "1940 to 1960", "1960 tot 1980", "1980 to heden")
    results = soup.find_all("td", attrs={"class": "value"})
    try:
        if results[0].text in all_list:
            return results[0].text
    except IndexError:
        pass
    try:
        if results[1].text in all_list:
            return results[1].text
    except IndexError:
        pass
    try:
        if results[2].text in all_list:
            return results[2].text
    except IndexError:
        pass
    try:
        if results[3].text in all_list:
            return results[3].text
    except IndexError:
        pass
    try:
        if results[4].text in all_list:
            return results[4].text
    except IndexError:
        pass
    try:
        if results[5].text in all_list:
            return results[5].text
    except IndexError:
        pass


def sort_getter():
    all_list = ("Amerikaans", "Anime (Japans)", "Europees", "Overige soorten", "Documentaire", "Muziek en Concerten",
                "Tv-serie of Tv-programma")
    results = soup.find_all("td", attrs={"class": "value"})
    try:
        if results[0].text in all_list:
            return results[0].text
    except IndexError:
        pass
    try:
        if results[1].text in all_list:
            return results[1].text
    except IndexError:
        pass
    try:
        if results[2].text in all_list:
            return results[2].text
    except IndexError:
        pass
    try:
        if results[3].text in all_list:
            return results[3].text
    except IndexError:
        pass
    try:
        if results[4].text in all_list:
            return results[4].text
    except IndexError:
        pass
    try:
        if results[5].text in all_list:
            return results[5].text
    except IndexError:
        pass


def type_getter():
    all_list = ("Poppen of Stop-motion", "Tekenfilm", "Overige typen", "Cursis of Instructie", "Documentaire",
                "Speelfilm", "Overige typen", "Film", "Tv non-fictie", "Tv fictie", "Stand-up of Theatershow",
                "Tv-programma of Sketches")
    results = soup.find_all("td", attrs={"class": "value"})
    try:
        if results[0].text in all_list:
            return results[0].text
    except IndexError:
        pass
    try:
        if results[1].text in all_list:
            return results[1].text
    except IndexError:
        pass
    try:
        if results[2].text in all_list:
            return results[2].text
    except IndexError:
        pass
    try:
        if results[3].text in all_list:
            return results[3].text
    except IndexError:
        pass
    try:
        if results[4].text in all_list:
            return results[4].text
    except IndexError:
        pass
    try:
        if results[5].text in all_list:
            return results[5].text
    except IndexError:
        pass


def country_getter():
    all_list = ("Afrika", "Azië", "Duitsland", "Frankrijk", "Italië", "Scandinavië", "Spanje", "Overige gebieden")
    results = soup.find_all("td", attrs={"class": "value"})
    try:
        if results[0].text in all_list:
            return results[0].text
    except IndexError:
        pass
    try:
        if results[1].text in all_list:
            return results[1].text
    except IndexError:
        pass
    try:
        if results[2].text in all_list:
            return results[2].text
    except IndexError:
        pass
    try:
        if results[3].text in all_list:
            return results[3].text
    except IndexError:
        pass
    try:
        if results[4].text in all_list:
            return results[4].text
    except IndexError:
        pass
    try:
        if results[5].text in all_list:
            return results[5].text
    except IndexError:
        pass


def description_getter():
    results = str(soup.find("div", attrs={"id": "vip-ad-description"}))
    results = results.replace('<div class="wrapped" id="vip-ad-description">', '')
    results = results.replace('</div>', '')
    results = results.replace('\n', '')
    return results


def box_set_getter():
    global rs1, rs2, rs3, rs4, rs5
    box = "Boxset"
    results = soup.find_all("td", attrs={"class": "value"})
    rs0 = results[0].text
    try:
        rs1 = results[1].text
    except IndexError:
        rs1 = ""
    try:
        rs2 = results[2].text
    except IndexError:
        rs2 = ""
    try:
        rs3 = results[3].text
    except IndexError:
        rs3 = ""
    try:
        rs4 = results[4].text
    except IndexError:
        rs4 = ""
    try:
        rs5 = results[5].text
    except IndexError:
        rs5 = ""
    listing = [rs0, rs1, rs2, rs3, rs4, rs5]
    if box in listing:
        box_set_index = listing.index(box)
    elif box not in listing:
        pass
    print(results[box_set_index].text)


def three_d_getter():
    global rs1, rs2, rs3, rs4, rs5
    three_d = "3D"
    results = soup.find_all("td", attrs={"class": "value"})
    rs0 = results[0].text
    try:
        rs1 = results[1].text
    except IndexError:
        rs1 = ""
    try:
        rs2 = results[2].text
    except IndexError:
        rs2 = ""
    try:
        rs3 = results[3].text
    except IndexError:
        rs3 = ""
    try:
        rs4 = results[4].text
    except IndexError:
        rs4 = ""
    try:
        rs5 = results[5].text
    except IndexError:
        rs5 = ""
    listing = [rs0, rs1, rs2, rs3, rs4, rs5]
    if three_d in listing:
        return listing.index(three_d)
    elif three_d not in listing:
        pass
