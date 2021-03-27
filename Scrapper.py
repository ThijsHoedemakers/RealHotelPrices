from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.fletcher.nl/nl/hotels/lijst').text

soup = BeautifulSoup(source,'lxml')

hotel = soup.find('div', class_='hotel')
#number_people = soup.find('div', class_='selectmenu selectmenu--occupation selectmenu--active"').
number_people = soup.find('div', class_="m-bit-100 bit-20 book__occupation")
# Number of people
parents = soup.find('input', class_="form__input form__input--occupation occupationAdults")['value']
kids = soup.find('input', class_="form__input form__input--occupation occupationKids")['value']
babys = soup.find('input', class_="form__input form__input--occupation occupationNewborn")['value']

next_page = soup.find('form', class_="hotel_reservation_form").text

print(next_page.prettify())
#print(ouders)

print(number_people.prettify())
original_price = 4
#print(hotel.prettify())

# csv_writer = csv.writer(csv_file, lineterminator = '\n')
# csv_writer.writerow(['headline', 'summary', 'video_link'])
# csv_writer.writerow(['r2','r2','r2'])
# i=0
# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     #print(headline)
#
#     sumtext = article.find('div', class_='entry-content').p.text
#     #print(sumtext)
#
#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']
#
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         #print(vid_id)
#         yt_link = f'http://youtube.com/watch?v={vid_id}'
#     except TypeError:
#         yt_link = None
#         #print('No YT player in current article')
#
#     #print(yt_link)
#
#     #print()
#     i+=1
#     csv_writer.writerow([headline, sumtext, yt_link])
#     print(i)
# csv_file.close()