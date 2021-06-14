import itertools

from django.shortcuts import render, redirect

# header code behind
from eshop_products.models import Product
from eshop_settings.models import SiteSetting
from eshop_sliders.models import Slider


def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Product.objects.get_active_products().order_by('-visit_count').all()[:8]
    latest_products = Product.objects.get_active_products().order_by('-id').all()[:8]
    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products)
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'about_page.html', context)

# import threading
# from threading import Thread
#
# from django.core.mail import EmailMessage
#
#
# class EmailThread(threading.Thread):
#     def __init__(self, subject, body, recipient_list):
#         self.subject = subject
#         self.recipient_list = recipient_list
#         self.body = body
#         threading.Thread.__init__(self)
#
#
#     def run (self):
#         msg = EmailMessage(
#             subject=self.subject,
#             body=self.body,
#             from_email='you email address that you defined in settings.py',
#             to=self.recipient_list,
#             headers={'Content-Type': 'text/plain'}
#             )
#         msg.send()
#
# EmailThread(
#             subject='Your Subject',
#             body='body',
#             recipient_list=['Reciever Email Addresses in a list']
#         ).run()
