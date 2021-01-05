from flask import escape
import base64
import math
import json
import os
import io
import requests

def send_response(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'url' in request_json:
        name = request_json['url']
    elif request_args and 'url' in request_args:
        name = request_args['url']
    else:
        url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

    html = getpagedata(url)
    results = {"html": html}
    return results


def getpagedata(url):
    from selenium import webdriver
    from fake_useragent import UserAgent

    # initiating the webdriver. Parameter includes the path of the webdriver.
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={UserAgent().random}')
    options.headless = True
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)

    # this is just to ensure that the page is loaded
    # time.sleep(2)

    html = driver.page_source

    driver.close()  # closing the webdriver
    return html
