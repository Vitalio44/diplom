from django import template

from products.models import Category

register = template.Library()


@register.inclusion_tag('category_menu.html')
def category_menu(req):
    new_cat = list()
    for c in Category.objects.all():
        if len(c.children.all()) > 0:
            new_cat.append({'name': c.name, 'url': c.get_absolute_url(), 'child': True, 'parent': True if len(c.parents.all()) > 0 else False, 'children': [{'name': ch.name, 'url': ch.get_absolute_url(), 'child': True if len(ch.children.all()) > 0 else False, 'children': []} for ch in c.children.all()]})
        else:
            new_cat.append({'name': c.name, 'url': c.get_absolute_url(), 'child': False, 'parent': True if len(c.parents.all()) > 0 else False, 'children': []})
    return {'categories': new_cat, 'request': req}
