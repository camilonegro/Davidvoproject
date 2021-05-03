from .models import Page

def add_nav_links(request):
    nav_links = Page.objects.filter(is_in_navigation=True).order_by("rank")

    return {
        "nav_links": nav_links

    }