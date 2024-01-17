from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.utils.timezone import now
from requests import get


# Create your views here.
def NamazTimesViews(request):
    # bs4 scraping
    url = "http://www.islom.uz/"
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find('div', class_='in_header_p')
    result = element.text.split()

    # print(result)
    return render(request, 'Waqt/index.html', {'city': result[2], 'bomdod': result[5],
                                               'quyosh': result[8], 'peshin': result[11], 'asr': result[14],
                                               'shom': result[17], 'hufton': result[20]})


def AndijonNamazWaqt(request):
    url2 = "https://namozvaqtlari.com/namoz/17-xiva-namoz-vaqtlari-bugungi-namoz-vaqti.html"
    response2 = get(url2)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    element2 = soup2.find('div', class_='namoz-time')
    result = element2.text.split()

    return render(request, 'Waqt/index.html', {'city': result[2], 'bomdod': result[1],
                                               'quyosh': result[4], 'peshin': result[7], 'asr': result[10],
                                               'shom': result[13], 'hufton': result[16]})


# ['Bomdod', '07:01', 'Xiva', 'Quyosh', '08:22', 'Xiva', 
# 'Peshin', '13:08', 'Xiva', 'Asr', '16:14', 'Xiva', 
# 'Shom', '18:00', 'Xiva', 'Xufton', '19:17', 'Xiva']


# url1 = "https://namozvaqtlari.com/namoz/15-qarshi-namoz-vaqtlari-bugungi-namoz-vaqti.html"
# response1 = get(url1)
# soup1 = BeautifulSoup(response1.text, 'html.parser')
# # print(soup1)
# element1 = soup1.find('div', class_='content')
# # date_time1 = soup1.find('div', class_='date_time')

# # # print(date_time.text)
# result1 = element1.text.split()
# print(result1)
