from django import template
from django.utils.timesince import timesince
import datetime

register = template.Library()


@register.simple_tag
def stampconvert(timestamp):
    normal_date = datetime.datetime.fromtimestamp(timestamp)
    return timesince(normal_date) + ' ago'

register.filter(stampconvert)
