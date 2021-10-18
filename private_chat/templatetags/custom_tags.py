from django import template

register = template.Library()


@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value


@register.filter
def modify_name(value, arg):
    print(value, arg)
    data = arg
    return data


register.filter('modify_name', modify_name)
