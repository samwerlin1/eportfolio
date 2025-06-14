from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Page

def page_detail_view(request, slug):
    # This function gets project/experience pages (or other custom portfolio pages)
    # All of these pages need to have an associated "page" data object in the Django models/database
    page = get_object_or_404(Page, slug=slug)

    context = {'page': page}  # Data about the page from the Django model/database

    if page.html_filename:
        # If the page object defines a specific html file to use from templates, just use that
        template_name = f'core/{page.html_filename}'
    else: # Otherwise, look for defined components and build the page from those
        template_name = 'core/components.html'

    return render(request, template_name, context)

def skill_page_view(request, skill_slug):
    skill_labels = {slug: label for slug, label in Page.Skill.choices}
    # This is making the skill names look-up-able from their slugs
    skill_label = skill_labels.get(skill_slug)

    if not skill_label:
        raise Http404('No "21st Century Skill" exists at that location.')

    pages_with_skill = Page.objects.filter(skill=skill_slug)  # Finds all pages with matching 21st Century Skill

    context = { # Data about the skill name and all the pages tagged with it
        'skill_label': skill_label,
        'pages': pages_with_skill,
    }

    return render(request, 'core/skill.html', context)

def about_view(request):
    # This is the home page for your eportfolio, which requires code in the about.html file in templates
    return render(request, 'core/about.html')