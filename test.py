import time
import pytesseract
from PIL import ImageGrab
import numpy as np
import cv2
import requests
import pyautogui
from bs4 import BeautifulSoup as bs
import new_functions as f
import tkinter as tk


# Click to top left
time.sleep(2)
pyautogui.FAILSAFE = False
pyautogui.click(0, 0)
pyautogui.click(0, 800)
pyautogui.scroll(20000)

# Sort the ads
pyautogui.move(1750, 670)
time.sleep(.5)
pyautogui.click(1750, 670)
time.sleep(.5)
pyautogui.click(1750, 770)

# click the first ad url
pyautogui.rightClick(1259, 875)
time.sleep(.1)
pyautogui.click(1349, 737)
root = tk.Tk()
root.withdraw()
url = str(root.clipboard_get())

if f.price_getter() == "":
    time.sleep(180)
session = requests.Session()
html = session.get(url)
# create a new soup
soup = bs(html.text, "lxml")

# making a new ad
pyautogui.rightClick(1451, 115)
time.sleep(.2)
pyautogui.click(1569, 133)
time.sleep(.2)
pyautogui.click(486, 0)
time.sleep(.2)

# Pasting the Title
pyautogui.click(419, 456)
time.sleep(.2)
pyautogui.typewrite(f.title_getter())

# Clicking on CDs
pyautogui.click(500, 579)
time.sleep(.2)
pyautogui.moveTo(445, 274)
pyautogui.scroll(500)
pyautogui.click(445, 274)

# Main Page Logic
pyautogui.click(856, 588)
time.sleep(.1)
if f.cat_getter1() == "Dvd's":
    pyautogui.click(856, 700)
    time.sleep(.1)
    pyautogui.click(1208, 585)
    time.sleep(.1)
if f.cat_getter1() == "Blu-ray":
    pyautogui.click(785, 650)
    pyautogui.click(1274, 581)
    time.sleep(.1)
    pyautogui.click(1208, 585)
    time.sleep(.1)
    pyautogui.click(1169, 648)
if f.cat_getter2() == "Overige":
    pyautogui.click(1192, 544)
if f.cat_getter2() == "Tv en Series":
    pyautogui.click(1195, 518)
if f.cat_getter2() == "Thrillers and Misdaad":
    pyautogui.click(1195, 499)
if f.cat_getter2() == "Tekenfilms en Animatie":
    pyautogui.click(1195, 471)
if f.cat_getter2() == "Sport en Fitness":
    pyautogui.click(1195, 449)
if f.cat_getter2() == "Klassiekers":
    pyautogui.click(1195, 419)
if f.cat_getter2() == "Science Fiction en Fantasy":
    pyautogui.click(1195, 397)
if f.cat_getter2() == "Religie en Gospel":
    pyautogui.click(1195, 369)
if f.cat_getter2() == "Nederlandstalig":
    pyautogui.click(1195, 343)
if f.cat_getter2() == "Muziek en Concerten":
    pyautogui.click(1195, 323)
if f.cat_getter2() == "Kinderen en Jeugd":
    pyautogui.click(1195, 294)
if f.cat_getter2() == "Komedie":
    pyautogui.click(1195, 272)
if f.cat_getter2() == "Horror":
    pyautogui.click(1195, 249)
if f.cat_getter2() == "Filmhuis":
    pyautogui.click(1195, 223)
if f.cat_getter2() == "Drama":
    pyautogui.click(1195, 195)
if f.cat_getter2() == "Documentaire en Educatief":
    pyautogui.click(1195, 168)
if f.cat_getter2() == "Cabaret en Sketches":
    pyautogui.click(1195, 145)
if f.cat_getter2() == "Avontuur":
    pyautogui.click(1195, 118)
if f.cat_getter2() == "Actie":
    pyautogui.click(1195, 97)

# Click Continue
pyautogui.click(401, 678)

# Paste The Ad Description
pyautogui.scroll(-800)
pyautogui.click(602, 834)
pyautogui.typewrite(f.description_getter())

# Changing the propreties
pyautogui.scroll(-600)
if f.cat_getter2() == "Blu-ray":
    if f.condition_getter():
        pyautogui.click(379, 885)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(977, 938)
    if f.genre_getter():
        pyautogui.click(423, 792)
        time.sleep(.1)
        if f.genre_getter() == "Overige genres":
            pyautogui.click(416, 753)
        elif f.genre_getter() == "Tv en Series":
            pyautogui.click(403, 721)
        elif f.genre_getter() == "Thrillers en Misdaad":
            pyautogui.click(441, 698)
        elif f.genre_getter() == "Tekenfilms en Animatie":
            pyautogui.click(397, 665)
        elif f.genre_getter() == "Sport en Fitness":
            pyautogui.click(435, 636)
        elif f.genre_getter() == "Science Fiction en Fantasy":
            pyautogui.click(430, 611)
        elif f.genre_getter() == "Religie en Gospel":
            pyautogui.click(401, 582)
        elif f.genre_getter() == "Nederlandstalig":
            pyautogui.click(401, 553)
        elif f.genre_getter() == "Muziek en Concerten":
            pyautogui.click(419, 527)
        elif f.genre_getter() == "Klassiekers":
            pyautogui.click(454, 498)
        elif f.genre_getter() == "Kinderen en Jeugd":
            pyautogui.click(454, 469)
        elif f.genre_getter() == "Humor en Cabaret":
            pyautogui.click(432, 443)
        elif f.genre_getter() == "Horror":
            pyautogui.click(432, 414)
        elif f.genre_getter() == "Filmhuis":
            pyautogui.click(432, 384)
        elif f.genre_getter() == "Drama":
            pyautogui.click(432, 356)
        elif f.genre_getter() == "Documentaire en Educatief":
            pyautogui.click(454, 331)
        elif f.genre_getter() == "Avontuur":
            pyautogui.click(454, 303)
        elif f.genre_getter() == "Actie":
            pyautogui.click(454, 274)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(432, 831)
    pyautogui.typewrite(f.price_getter())



elif f.cat_getter2() == "Overige":
    if f.condition_getter():    # If the condition is new, it clicks the box
        pyautogui.click(379, 885)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(379, 941)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(466, 838)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Tv en Series":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(381, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(383, 924)
    if f.genre_getter():
        pyautogui.click(462, 662)
        time.sleep(.1)
        if f.genre_getter() == "Actie en Avontuur":
            pyautogui.click(413, 738)
        elif f.genre_getter() == "Drama":
            pyautogui.click(396, 767)
        elif f.genre_getter() == "Horror":
            pyautogui.click(397, 795)
        elif f.genre_getter() == "Komedie":
            pyautogui.click(402, 822)
        elif f.genre_getter() == "Science Fiction en Fantasy":
            pyautogui.click(402, 849)
        elif f.genre_getter() == "Thriller":
            pyautogui.click(412, 875)
        elif f.genre_getter() == "Non-fictie":
            pyautogui.click(409, 906)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(409, 935)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(438, 818)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Thrillers and Misdaad":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(381, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(383, 924)
    if f.genre_getter():
        pyautogui.click(462, 662)
        time.sleep(.1)
        if f.genre_getter() == "Actiethriller":
            pyautogui.click(413, 738)
        elif f.genre_getter() == "Bovennatuurlijke thriller":
            pyautogui.click(396, 767)
        elif f.genre_getter() == "Detective en Krimi":
            pyautogui.click(397, 795)
        elif f.genre_getter() == "Maffia en Misdaad":
            pyautogui.click(402, 822)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(402, 849)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(473, 817)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Tekenfilms en Animaties":
    pyautogui.scroll(-240)
    if f.condition_getter():
        pyautogui.click(380, 854)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(378, 906)
    if f.sort_getter():
        pyautogui.click(480, 545)
        time.sleep(.1)
        if f.sort_getter() == "Amerikaans":
            pyautogui.click(438, 610)
        elif f.sort_getter() == "Anime (Japans)":
            pyautogui.click(443, 641)
        elif f.sort_getter() == "Europees":
            pyautogui.click(410, 669)
        elif f.sort_getter() == "Overige soorten":
            pyautogui.click(422, 694)
    if f.type_getter():
        pyautogui.click(467, 649)
        time.sleep(.1)
        if f.type_getter() == "Poppen of Stop-motion":
            pyautogui.click(445, 718)
        elif f.type_getter() == "Tekenfilm":
            pyautogui.click(415, 746)
        elif f.type_getter() == "Overige typen":
            pyautogui.click(422, 773)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(455, 799)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Sport en Fitness":
    pyautogui.scroll(-240)
    if f.condition_getter():
        pyautogui.click(380, 854)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(378, 906)
    if f.sort_getter():
        pyautogui.click(469, 536)
        time.sleep(.1)
        if f.type_getter() == "Cursus of Instructie":
            pyautogui.click(450, 611)
        elif f.type_getter() == "Documentaire":
            pyautogui.click(418, 640)
        elif f.type_getter() == "Speelfilm":
            pyautogui.click(418, 666)
        elif f.type_getter() == "Overige typen":
            pyautogui.click(410, 694)
    if f.genre_getter():
        pyautogui.click(426, 646)
        time.sleep(.1)
        if f.genre_getter() == "Vechtsport":
            pyautogui.click(426, 718)
        elif f.genre_getter() == "Voetbal":
            pyautogui.click(437, 743)
        elif f.genre_getter() == "Yoga, Fitness of Dans":
            pyautogui.click(430, 779)
        elif f.genre_getter() == "Overige typen":
            pyautogui.click(478, 803)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(466, 801)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Klassiekers":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(378, 977)
    if f.genre_getter():
        pyautogui.click(444, 671)
        time.sleep(.1)
        if f.genre_getter() == "Actie en Avontuur":
            pyautogui.click(482, 735)
        elif f.genre_getter() == "Drama":
            pyautogui.click(425, 766)
        elif f.genre_getter() == "Horror":
            pyautogui.click(439, 794)
        elif f.genre_getter() == "Komedie":
            pyautogui.click(448, 823)
        elif f.genre_getter() == "Science Fiction en Fantasy":
            pyautogui.click(481, 851)
        elif f.genre_getter() == "Thrillers en Misdaad":
            pyautogui.click(440, 879)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(433, 912)
    if f.period_getter():
        pyautogui.click(414, 778)
        time.sleep(.1)
        if f.period_getter() == "Voor 1940":
            pyautogui.click(460, 846)
        elif f.period_getter() == "1940 tot 1960":
            pyautogui.click(451, 872)
        elif f.period_getter() == "1960 tot 1980":
            pyautogui.click(425, 901)
        elif f.period_getter() == "1980 tot heden":
            pyautogui.click(410, 928)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(454, 878)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Science Fiction en Fantasy":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(378, 920)
    if f.genre_getter():
        pyautogui.click(421, 667)
        time.sleep(.1)
        if f.genre_getter() == "Fantasy":
            pyautogui.click(401, 742)
        elif f.genre_getter() == "Science Fiction":
            pyautogui.click(401, 770)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(470, 824)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Religie en Gospel":
    if f.condition_getter():
        pyautogui.click(379, 885)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 939)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(491, 835)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Nerdelandstalig":
    pyautogui.scroll(-240)
    if f.condition_getter():
        pyautogui.click(379, 850)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(381, 905)
    if f.type_getter():
        pyautogui.click(491, 544)
        time.sleep(.1)
        if f.type_getter() == "Film":
            pyautogui.click(442, 616)
        elif f.type_getter() == "Tv fictie":
            pyautogui.click(449, 642)
        elif f.type_getter() == "Tv non-fictie":
            pyautogui.click(464, 674)
    if f.genre_getter():
        pyautogui.click(459, 650)
        time.sleep(.1)
        if f.genre_getter() == "Documentaire":
            pyautogui.click(474, 721)
        elif f.genre_getter() == "Actie en Avontuur":
            pyautogui.click(455, 751)
        elif f.genre_getter() == "Drama":
            pyautogui.click(439, 778)
        elif f.genre_getter() == "Filmhuis":
            pyautogui.click(420, 805)
        elif f.genre_getter() == "Horror":
            pyautogui.click(420, 836)
        elif f.genre_getter() == "Komedie":
            pyautogui.click(453, 860)
        elif f.genre_getter() == "Muziek":
            pyautogui.click(454, 890)
        elif f.genre_getter() == "Thriller":
            pyautogui.click(465, 917)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(472, 946)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(492, 798)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Muziek eb Concerten":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(380, 869)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 921)
    if f.sort_getter():
        pyautogui.click(447, 669)
        time.sleep(.1)
        if f.sort_getter() == "Documentaire":
            pyautogui.click(457, 738)
        elif f.sort_getter() == "Muziek en Concerten":
            pyautogui.click(470, 773)
        elif f.sort_getter() == "Tv-serie of Tv-programma":
            pyautogui.click(514, 803)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(486, 820)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Kinderen en Jeugd":
    pyautogui.scroll(-240)
    if f.condition_getter():
        pyautogui.click(379, 853)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 903)
    if f.type_getter():
        pyautogui.click(485, 543)
        time.sleep(.1)
        if f.type_getter() == "Film":
            pyautogui.click(485, 617)
        elif f.type_getter() == "Tv fictie":
            pyautogui.click(434, 645)
        elif f.type_getter() == "Tv non-fictie":
            pyautogui.click(458, 670)
    if f.genre_getter():
        pyautogui.click(552, 645)
        time.sleep(.1)
        if f.genre_getter() == "Avontuur":
            pyautogui.click(467, 720)
        elif f.genre_getter() == "Dieren":
            pyautogui.click(504, 754)
        elif f.genre_getter() == "Educatief":
            pyautogui.click(465, 780)
        elif f.genre_getter() == "Komedie":
            pyautogui.click(494, 805)
        elif f.genre_getter() == "Poppen":
            pyautogui.click(447, 835)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(464, 864)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(522, 798)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Komedie":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 922)
    if f.genre_getter():
        pyautogui.click(526, 667)
        time.sleep(.1)
        if f.genre_getter() == "Actiekomedie":
            pyautogui.click(525, 737)
        elif f.genre_getter() == "Romantische komedie":
            pyautogui.click(445, 769)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(513, 796)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(476, 819)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Horror":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 924)
    if f.genre_getter():
        pyautogui.click(526, 667)
        time.sleep(.1)
        if f.genre_getter() == "Gore":
            pyautogui.click(577, 738)
        elif f.genre_getter() == "Monsters":
            pyautogui.click(495, 771)
        elif f.genre_getter() == "Slasher":
            pyautogui.click(466, 804)
        elif f.genre_getter() == "Spoken Geesten":
            pyautogui.click(499, 828)
        elif f.genre_getter() == "Vampiers of Zombies":
            pyautogui.click(475, 855)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(529, 880)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(430, 820)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Filmhuis":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 922)
    if f.country_getter():
        pyautogui.click(500, 665)
        time.sleep(.1)
        if f.country_getter() == "Afrika":
            pyautogui.click(477, 743)
        elif f.country_getter() == "Azië":
            pyautogui.click(454, 769)
        elif f.country_getter() == "Duisland":
            pyautogui.click(486, 799)
        elif f.country_getter() == "Frankrijk":
            pyautogui.click(491, 824)
        elif f.country_getter() == "Italië":
            pyautogui.click(462, 850)
        elif f.country_getter() == "Scandinavië":
            pyautogui.click(477, 811)
        elif f.country_getter() == "Spanje":
            pyautogui.click(460, 913)
        elif f.country_getter() == "Overige gebieden":
            pyautogui.click(482, 939)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(440, 819)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Drama":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 924)
    if f.genre_getter():
        pyautogui.click(500, 665)
        time.sleep(.1)
        if f.genre_getter() == "Drama":
            pyautogui.click(548, 740)
        elif f.genre_getter() == "Historisch of Kostuumdrama":
            pyautogui.click(574, 768)
        elif f.genre_getter() == "Waargebeurd drama":
            pyautogui.click(523, 798)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(533, 824)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(464, 818)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Documentaire en Efucatief":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 870)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 924)
    if f.genre_getter():
        pyautogui.click(500, 665)
        time.sleep(.1)
        if f.genre_getter() == "Biografie":
            pyautogui.click(578, 741)
        elif f.genre_getter() == "Kunst of Cultuur":
            pyautogui.click(512, 771)
        elif f.genre_getter() == "Natuur":
            pyautogui.click(521, 799)
        elif f.genre_getter() == "Oorlog of Misdaad":
            pyautogui.click(431, 830)
        elif f.genre_getter() == "Politiek of Geschiedenis":
            pyautogui.click(508, 854)
        elif f.genre_getter() == "Wetenschap of Techniek":
            pyautogui.click(543, 879)
        elif f.genre_getter() == "Overige typen":
            pyautogui.click(531, 907)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(473, 819)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Cabaret en Sketches":
    if f.condition_getter():
        pyautogui.click(380, 996)
    if f.type_getter():
        pyautogui.click(517, 794)
        time.sleep(.1)
        if f.type_getter() == "Stand-up of Theatershow":
            pyautogui.click(494, 867)
        elif f.type_getter() == "Tv-programma of Skethes":
            pyautogui.click(442, 897)
        elif f.type_getter() == "Overige typen":
            pyautogui.click(447, 925)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(473, 890)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Avontuur":
    if f.condition_getter():
        pyautogui.click(379, 886)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(380, 938)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(460, 838)
    pyautogui.typewrite(f.price_getter())

elif f.cat_getter2() == "Actie":
    pyautogui.scroll(-120)
    if f.condition_getter():
        pyautogui.click(379, 871)
    if f.box_set_getter() == "Boxset":
        pyautogui.click(379, 926)
    if f.genre_getter():
        pyautogui.click(572, 666)
        time.sleep(.1)
        if f.genre_getter() == "Actie":
            pyautogui.click(525, 746)
        elif f.genre_getter() == "Actiekomedie":
            pyautogui.click(545, 770)
        elif f.genre_getter() == "Actiethriller":
            pyautogui.click(508, 797)
        elif f.genre_getter() == "Martial Arts":
            pyautogui.click(501, 825)
        elif f.genre_getter() == "Oorlog":
            pyautogui.click(473, 854)
        elif f.genre_getter() == "Overige genres":
            pyautogui.click(514, 881)
    # Putting the price
    pyautogui.scroll(-360)
    pyautogui.click(490, 821)
    pyautogui.typewrite(f.price_getter())
# Placing the ad
pyautogui.scroll(-10000)
