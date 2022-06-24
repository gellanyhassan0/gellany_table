from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import argparse


class gellany_table():

              def __init__(self, url = None , key = None , element = None , search = None , table = None):
                   
                         self.url = url
                         self.key = key
                         self.element = element
                         self.search = search
                         self.table = table



              def driver(self):

                         options = Options()
                         options.add_argument("no-sandbox");
                         options.add_argument("headless");
                         options.add_argument("start-maximized");
                         options.add_argument("window-size=1900,1080");
                         options.add_argument("127.0.0.1:4444");
                         global driver
                         driver = webdriver.Chrome(chrome_options=options, executable_path="/usr/bin/chromedriver")
                         driver.implicitly_wait(0.5)
                         driver.get(self.url)

                         html = driver.page_source
                         print(html)

              def container(self):
                         
                         containers = driver.find_elements(by='xpath', value=self.element)
                         #print(containers)
                         titles = []
                         subtitles = []
                         links = []
                         for container in containers:
                             title = container.find_element(by='xpath', value='./a/h2').text
                             subtitle = container.find_element(by='xpath', value='./a/p').text
                             link = container.find_element(by='xpath', value='./a').get_attribute('href')
                             titles.append(title)
                             subtitles.append(subtitle)
                             links.append(link)

                         # Exporting data to a CSV file
                         my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
                         df_headlines = pd.DataFrame(my_dict)
                         df_headlines.to_csv('headline.csv')
                         print(df_headlines.head())

              def pd_csv(self):
                      
                         df_csv = pd.read_csv(self.url)
                         print(df_csv)

              def pd_html(self):
             
                         df_html = pd.read_html(self.url)
                         print(df_html[int(self.table)].head())
                         

              def send(self):

                         # Sending key in search box by search element
                         m = driver.find_element_by_name(self.search)
                         m.send_keys(self.key)
                         time.sleep(0.2)
                         m.send_keys(Keys.ENTER)
                         html = driver.page_source
                         print(html)

                         

              def main(self):

                         
                              self.driver()

                              if isinstance(self.element, str) == True:
                                           try :
                                                  self.container()
                                           except:
                                                  print("error in container")
                                                  #driver.quit()

                              if (self.url[-4:]) == '.csv':
                                           try :
                                                  self.pd_csv()
                                           except:
                                                  print("error in panda csv")
                                                  #driver.quit()

                              if isinstance(self.table, str) == True or self.table == "1":
                                           try :
                                                  self.pd_html()
                                           except:
                                                  print("error in panda html")
                                                  #driver.quit()



                              if isinstance(self.search, str) == True:
                                           try :
                                                  self.send()
                                                  
                                           except:
                                                  print("error in send")
                                                  #driver.quit()

                              driver.quit() 
                                     
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--url')
my_parser.add_argument('--element')
my_parser.add_argument('--search')
my_parser.add_argument('--key')
my_parser.add_argument('--table')
args = my_parser.parse_args()                           
                         

#gellany_table(url = "https://www.thesun.co.uk/sport/football/" , element = '//div[@class="teaser__copy-container"]', search = "s", key = "goals").main()
#gellany_table(url = "https://www.football-data.co.uk/mmz4281/2122/E0.csv").main()
#gellany_table(url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)", table = 1).main()

gellany_table(url = args.url , element = args.element, search = args.search, key = args.key, table = args.table).main()
