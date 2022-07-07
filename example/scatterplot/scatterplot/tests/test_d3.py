import os
import unittest
import re
from gradescope_utils.autograder_utils.decorators import weight, tags, number
from gradescope_utils.autograder_utils.decorators import partial_credit
from gradescope_utils.autograder_utils.files import check_submitted_files
from utils.output_blocker import NoStd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color
import numpy as np
import pandas as pd
from utils.gs_helper import load_meta_json
from autograde_viz.d3_scales import *
from autograde_viz.css_transforms import *
from bs4 import BeautifulSoup


class TestFiles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        if os.path.exists('/autograder'):  # gradescope run
            local_run = False
            url = 'http://localhost:8080/submission.html'
            driver = webdriver.Chrome(options=chrome_options)
            metadata_json = "/autograder/submission_metadata.json"

        else:
            local_run = True
            url = 'http://localhost:8080/submission.html'
            driver = webdriver.Chrome(
                executable_path="utils/chromedriver",
                options=chrome_options)
            metadata_json = "sample/submission_metadata.json"

        meta = load_meta_json(metadata_json)
        # cls.submitted_gtid = meta['users'][0]['sid']
        # cls.expected_gtid = '999999999'

        driver.get(url)

        # set chromedrive window dimensions to student submission dimensions
        rendered_width = driver.execute_script("return document.documentElement.scrollWidth")
        rendered_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.set_window_size(rendered_width,rendered_height)        
        cls.driver = driver

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cls.soup = soup

    @classmethod
    def tearDownClass(cls) -> None: 
        cls.driver.quit()

    @weight(0.0)
    def test_002_d3_imports(self):
        """Functional advisory test - determine if the d3 lib imports are correct."""
        with NoStd():
            required_imports =  ['lib/d3/d3.min.js', 'lib/d3-dsv/d3-dsv.min.js']

            submitted_imports = []
            found_tags = self.soup.find_all("script")
            for tag in found_tags:
                if 'src' in list(tag.attrs.keys()):
                    submitted_imports.append(tag.attrs['src'])
            diff = list(set(required_imports).difference(set(submitted_imports)))
            same = len(list(set(submitted_imports).intersection(set(required_imports))))
            self.assertCountEqual(required_imports, submitted_imports, f"Found {same}/3 required imports. \nThe import {diff} was not found or could be referenced with a different path than required. \nThis will prevent required libraries from loading correctly during grading.")
        print("Found all required d3 imports.")

    @weight(0.0)
    def test_01_data_representation(self):
        """Test that there is one mark present for each required data point in the dataset."""
        df = pd.read_csv("data/cars.csv")
        df = df.dropna(subset=['Miles_per_Gallon', 'Horsepower'])
        df = df.reset_index(drop=True)

        try:
            circles = WebDriverWait(self.driver, 10) \
                .until(EC.presence_of_element_located((By.ID, "symbols"))) \
                .find_elements_by_tag_name("circle")
            desired_data_len = len(df)
            submitted_data_len = len(circles)
            self.assertEqual(desired_data_len, submitted_data_len, \
                f"Expected {desired_data_len} plotted marks. Found {submitted_data_len} instead.")
        except:
            raise NoSuchElementException
        
        print(f"Found {submitted_data_len} plotted marks")
