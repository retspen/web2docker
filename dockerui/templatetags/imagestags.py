from django import template

register = template.Library()


@register.simple_tag
def showrepo(data):
    return data[0].split(':')[0]

register.filter(showrepo)


@register.simple_tag
def showtag(data):
    return data[0].split(':')[1]

register.filter(showtag)
