# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 07:45:42 2024

@author: 91620
"""

import requests
from bs4 import BeautifulSoup 
import regex as re
def allmovie():
    url="https://www.imdb.com/chart/top/?ref_=chtmvm_ql_3"
    head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}
    result=requests.get(url,headers=head)
    #print(result.text)
    soup = BeautifulSoup(result.content, 'html.parser')
    li=soup.find_all('h3',{'class':'ipc-title__text'})
    print(type(li))
    str1=str(li)
    print(type(str1))
    str1.strip("<h3 class=")
    #print(str1)
    l1=str1.split("h3>,")
    for i in l1:
            if re.search('\d+\.',i):
                print(i.replace('<h3 class="ipc-title__text">', '').replace('</',''))
    

def actionmovie(): 
    ur1="https://www.imdb.com/interest/in0000001/?ref_=ints_cat_1_in_i_1"
    head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

    res=requests.get(ur1,headers=head)
    soup1 = BeautifulSoup(res.content, 'html.parser')
    li=soup1.find_all('span',{'data-testid':'title'})
    for i in li:
        print(i.get_text())

def comedymovie():
        
    ur2="https://www.imdb.com/interest/in0000034/?ref_=int_sim_in_i_3"
    head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'}

    res2=requests.get(ur2,headers=head)
    soup2 = BeautifulSoup(res2.content, 'html.parser')
    li2=soup2.find_all('span',{'data-testid':'title'})
    for i in li2:
        print(i.get_text())
    
    
usrinput=input("Enter genre u want to see ")
if usrinput=="action":
    actionmovie()
elif usrinput=="comedy":
    comedymovie()
else:
    allmovie()




                  