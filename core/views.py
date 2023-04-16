from django.shortcuts import render
from django.views import View
from .models import BenefitCard, IntroSlideContent, EquipmentSlideContent, Catalog, TopBlinds

class IndexView(View):
    def get(self, request):
        intro_slide = IntroSlideContent.objects.all()
        benefit_card = BenefitCard.objects.all().order_by('id')
        equiepments = EquipmentSlideContent.objects.all().order_by('id')
        catalogs = Catalog.objects.all().order_by('id')
        topblinds = TopBlinds.objects.all().order_by('id')

        context = {
            'intro_slide': intro_slide,
            'benefit_card': benefit_card,
            'equiepments': equiepments,
            'catalogs': catalogs,
            'topblinds': topblinds
        }

        return render(request, 'core/index.html', context)
