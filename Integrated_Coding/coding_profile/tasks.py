from celery import shared_task
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

@shared_task
def scrape_hackerrank_profile(url):
    return "done"

@shared_task
def scrape_codechef_profile(url):
    return "done"

@shared_task
def scrape_codeforces_profile(url):
    return "done"

@shared_task
def scrape_leetcode_profile(url):
    return "done"

@shared_task
def scrape_spoj_profile(url):
    return "done"
