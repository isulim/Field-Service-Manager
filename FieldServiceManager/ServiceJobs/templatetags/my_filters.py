from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def taknie(value):

    if value == 'True':
        return 'Tak'
    if value == 'False':
        return 'Nie'
