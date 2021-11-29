from bs4 import BeautifulSoup
import requests
import re

text= "cardiologists"
url = 'https://google.com/search?q=' + text
  
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
  
# Creating soup from the fetched request
soup = BeautifulSoup(request_result.text,
                         "html.parser")

#print(soup.prettify())
# soup.find.all( h3 ) to grab
# all major headings of our search result,
#heading_object=soup.find_all( 'h3')
url_fetch = soup.find_all(href=re.compile("cardio"))
# Iterate through the object
# and print it as a string.
for info in url_fetch:
    print(info.getText())
    print("------")


if __name__ == '__main__':
    main()
