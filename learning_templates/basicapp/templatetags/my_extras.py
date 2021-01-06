from django import template
register = template.Library()
@register.filter(name='curt')
def curt(value,arg):
    return value.replace(arg,'')

