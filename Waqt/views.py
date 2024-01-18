from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import get

from . import scripts


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
    return render(request, 'Waqt/index.html', context=scripts.andijan())


def BuxoroNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.buxoro())


def DenovNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.denov())


def GulistonNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.guliston())


def JizzaxNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.jizzax())


def MargilanNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.margilan())


def NamanganNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.namangan())


def NukusNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.nukus())


def NavoiyNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.navoiy())


def QarshiNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.qarshi())


def QoqanNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.qoqan())


def SamarqandNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.samarqand())


def TermizNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.termiz())


def XivaNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.xiva())


def OlmaliqNamazWaqt(request):
    return render(request, 'Waqt/index.html', context=scripts.olmaliq())
