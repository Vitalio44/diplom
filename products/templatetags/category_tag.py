from django import template

from products.models import Category

register = template.Library()


@register.inclusion_tag('category_menu.html')
def category_menu(req):
    def create_child(children):
        child_list = []
        for ch in children:
            child_list.append({
                'name': ch.name,
                'url': ch.get_absolute_url(),
                'child': True if len(ch.children.all()) > 0 else False,
                'parent': True if len(ch.parents.all()) > 0 else False,
                'children': create_child(ch.children.all())})
        return child_list

    format_ctr = list()
    for c in Category.objects.all():
        format_ctr.append(
            {'name': c.name, 'url': c.get_absolute_url(),
             'child': True if len(c.children.all()) > 0 else False,
             'parent': True if len(c.parents.all()) > 0 else False,
             'children': create_child(c.children.all())})
    return {'categories': format_ctr, 'request': req}
