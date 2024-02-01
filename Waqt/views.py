from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from requests import get
from django.conf import settings
from django.http import HttpResponse

from .models import SendMessageModel, ProfileModel
from .forms import SendMessageForm
from . import scripts


# Create your views here.
def NamazTimesViews(request):
    # bs4 scraping
    try:
        url = "http://www.islom.uz/"
        response = get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find('div', class_='in_header_p')
        result = element.text.split()
        # print(request.user.email)
        # print(result)
        data = {'city': 'Toshkent', 'bomdod': result[5], 'quyosh': result[8], 'peshin': result[11], 'asr': result[14],
                'shom': result[17], 'hufton': result[20]}

        return render(request, 'Waqt/index.html', data)

    except AttributeError:
        return render(request, 'Waqt/index.html', context=scripts.toshkent())


@login_required
def SendNamazWaqtiToEmailViews(request):
    # print(request.user.email)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            send = form.save(commit=False)
            send.email = request.user.email
            send.save()
            return redirect('home')
    else:
        form = SendMessageForm()

    return render(request, 'Waqt/sendform.html', {'form': form})


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


def MapView(request):
    api_key = settings.GOOGLE_MAPS_API_KEY
    return render(request, 'Waqt/map.html', {'api_key': api_key})


def testmap(request):
    return render(request, 'Waqt/test.html')
