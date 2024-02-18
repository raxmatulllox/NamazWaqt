from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from bs4 import BeautifulSoup
from requests import get

from .models import SendMessageModel
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
                'shom': result[17], 'hufton': result[20], 'vaqt_hijri': scripts.vaqt_hijri(), 'vaqt_mill': scripts.vaqt_mill()}
        # print(data)

        return render(request, 'Waqt/index.html', context=scripts.toshkent())

    except:
        return render(request, 'Waqt/index.html', context=scripts.toshkent())


@login_required
def SendNamazWaqtiToEmailViews(request):
    # print(request.user.email)
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            email = request.user.email
            existing_send_message = SendMessageModel.objects.filter(email=email).first()

            if existing_send_message:
                existing_send_message.delete()

            send = form.save(commit=False)
            send.email = email
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


def show_email(request):
    send_messages = SendMessageModel.objects.all()
    emails = [send_message.email for send_message in send_messages]
    print(emails)
    return render(request, 'Waqt/test.html', {'emails': emails})


def send_email_according_to_recurrent(request):
    objects_to_send_email = SendMessageModel.objects.all()
    for obj in objects_to_send_email:
        if obj.recurrent == '1':
            subject = 'namazwaqti.uz xabarnomasi'
            message = 'Sizning xabaringiz matni'
            sender_email = settings.EMAIL_HOST_USER
            recipient_email = obj.email
            send_mail(subject, message, sender_email, [recipient_email])

        elif obj.recurrent == '2':
            current_date = timezone.now()
            two_days_ago = current_date - timedelta(days=2)
            if obj.date.date() <= two_days_ago.date():
                subject = 'namazwaqti.uz xabarnomasi'
                message = 'Sizning xabaringiz matni!'
                sender_email = settings.EMAIL_HOST_USER
                recipient_email = obj.email
                send_mail(subject, message, sender_email, [recipient_email])

    return render(request, 'Waqt/sendform.html')


def week(req):
    return render(req, 'Waqt/week.html')
