from django import template
register = template.Library()

@register.filter(name='multiply')
def multiply(value, multipllier):
    return value * multipllier

@register.filter(name='division')
def division(value, division):
    result = value / division
    if result > 1:
        return "{:.2f}".format(result)
    else:
        return "{:.6f}".format(result)