from django.shortcuts import render
from django.views import View
from .models import BenefitCard, IntroSlideContent

class IndexView(View):
    def get(self, request):
        intro_slide = IntroSlideContent.objects.all()
        benefit_card = BenefitCard.objects.all().order_by('id')

        context = {
            'intro_slide': intro_slide,
            'benefit_card': benefit_card
        }

        return render(request, 'core/index.html', context)
