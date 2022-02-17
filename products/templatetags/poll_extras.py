from django import template

register=template.Library()

@register.filter(name='split')
def splitting(value):
    return str(value).split(',')