from django import template

register = template.Library()

@register.filter
def minus_one_comment(value):
    return value - 1
