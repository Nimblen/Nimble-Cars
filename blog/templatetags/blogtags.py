from django import template
from blog.services.scraper_for_blog import create_post




register = template.Library()


@register.simple_tag(name='create_post')
def get_new_post():
    return create_post()