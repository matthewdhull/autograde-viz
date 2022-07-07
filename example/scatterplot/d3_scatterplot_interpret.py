from bs4  import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from autograde_viz.d3_scales import *
import re
import json
import numpy as np
import pandas as pd

"""
Scratch file for figuring how to scrape a d3 scatterplot 
run a local server as indicated in readme.md
"""

if __name__ == '__main__':

    url = 'http://localhost:3000/submission.html'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(
        executable_path="utils/chromedriver",
        options=chrome_options)

    driver.get(url)  # must be running a localserver in the submission/ dir

    # set chromedrive window dimensions to plot page dimensions
    rendered_width = driver.execute_script("return document.documentElement.scrollWidth")
    rendered_height = driver.execute_script("return document.documentElement.scrollHeight")
    driver.set_window_size(rendered_width,rendered_height)        

    # Title Tag
    title = driver.find_element_by_id("title").text

    # Scatterplot Circle Marks
    circle_marks = WebDriverWait(driver, 10) \
        .until(EC.presence_of_element_located((By.ID, "symbols"))) \
        .find_elements_by_tag_name("circle")

    # Filter data where Miles_per_Gallon & Horsepower are not missing. 
    df = pd.read_csv("data/cars.csv")
    df = df.dropna(subset=['Miles_per_Gallon', 'Horsepower'])
    df = df.reset_index(drop=True)

    # Circle Mark Colors
    circle_mark_colors = list(set([l.value_of_css_property("fill") for l in circle_marks]))
    circle_mark_hex_colors = [Color.from_string(c).hex for c in circle_mark_colors]

    # TODO
    # y_axis_height = WebDriverWait(driver, 10) \
    #     .until(EC.presence_of_element_located((By.ID, "y-axis-lines"))) \
    #     .find_element_by_class_name("domain") \
    #     .rect['height']
    
    # x_axis_width = WebDriverWait(driver, 10) \
    #     .until(EC.presence_of_element_located((By.ID, "x-axis-lines"))) \
    #     .find_element_by_class_name("domain") \
    #     .rect['width']
