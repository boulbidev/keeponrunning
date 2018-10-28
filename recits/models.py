from django.db import models
from django.utils import timezone

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class RecitsIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    # Mise à jour du contexte pour lister les récits par ordre chronologique inverse de date de l'évènement
    # Et filtrage des récits publié seulement-> live()
    def get_context(self, request):
        context = super().get_context(request)
        context['recitspages'] = RecitPage.objects.live().child_of(self).order_by('-event_date')
        return context


class RecitPage(Page):
    event_date = models.DateField("Date de l'évènement", default=timezone.now)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('event_date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    promote_panels = [
        ImageChooserPanel('hero_image'),
    ]

class RecitPageGalleryImage(Orderable):
    page = ParentalKey(RecitPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]