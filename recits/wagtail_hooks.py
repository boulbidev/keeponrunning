from wagtail.core import hooks
from recits.models import RecitPage


########################################################################################################################
# Utilisé pour filtrer les pages par ordre croissant d'évènement dans l'explorer de wagtail
# Toutes les pages sont affichées
@hooks.register('construct_explorer_page_queryset')
def apply_default_order_to_recitsindex_section(parent_page, pages, request):

    if parent_page.slug == 'recitsindex' and 'ordering' not in request.GET:
        pages = RecitPage.objects.child_of(parent_page).order_by('-event_date')
    return pages