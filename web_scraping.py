#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.6.1

'''
Web Scraping: scraping all the link in special url, and output the [text:link] to *.csv file.

Reference: https://www.jianshu.com/p/ba02079ecd2f
'''

import sys
import pandas as pd
from requests_html import HTMLSession

url = 'https://www.jianshu.com/p/85f4624485b9'
session = HTMLSession()
web = session.get(url)

def get_text_link_from_sel(sel):
    
    link_list = []
    try:
        results = web.html.find(sel)
        for result in results:
            link_name = result.text
            link_link = list(result.absolute_links)[0]
            link_list.append((link_name, link_link))
        #return link_list
    except:
        return None
    df = pd.DataFrame(link_list)
    df.columns = ['text', 'link']
    df.to_csv('output.csv', encoding='utf_8_sig', index=False) # utf-8 encoding no BOM, will error codes

def main():
    
    print('Start Scraping ...')
    sel = 'body > div.note > div.post > div.article > div.show-content > div > p > a'
    get_text_link_from_sel(sel)
    print('End Scraping ...')

if __name__ == '__main__':
    
    main()
    sys.exit()