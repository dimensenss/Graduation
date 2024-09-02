from django import template

register = template.Library()

def group_by(value, n):
    return [value[i:i+n] for i in range(0, len(value), n)]

register.filter('group_by', group_by)