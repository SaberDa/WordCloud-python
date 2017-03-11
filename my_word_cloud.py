#!/usr/bin/python
#-*- coding: utf-8 -*-


import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)


mask = np.array(Image.open(path.join(d, "saber.png")))

image_colors = ImageColorGenerator(mask)

text = open(u"ubw.txt").read().decode('gbk')

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")
stopwords.add("line3")
stopwords.add("line4")

wc = WordCloud(font_path=font,
               max_words=2000,
               mask=mask,
               stopwords=stopwords,
               margin=10,
               random_state=1,
               background_color = "white").generate(text)
# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=image_colors, random_state=3))
wc.to_file("a_new_hope.png")
plt.axis("off")
plt.figure()
plt.title(u"ubw-词频统计")
plt.imshow(default_colors)
plt.axis("off")
plt.show()
