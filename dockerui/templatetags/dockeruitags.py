from django import template
from django.utils.timesince import timesince
import datetime

register = template.Library()

@register.simple_tag
def showrepo(data):
    return data[0].split(':')[0]

register.filter(showrepo)

@register.simple_tag
def showtag(data):
    return data[0].split(':')[1]

register.filter(showtag)

@register.simple_tag
def stampconvert(timestamp):
    normal_date = datetime.datetime.fromtimestamp(timestamp)
    return timesince(normal_date) + ' ago'

register.filter(stampconvert)
