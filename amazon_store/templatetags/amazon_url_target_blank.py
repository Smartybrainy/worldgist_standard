from django import template

register = template.Library()


def blank_target(text):
    return text.replace('<a ', "<a target='_blank' ")


blank_target = register.filter(blank_target, is_safe=True)
