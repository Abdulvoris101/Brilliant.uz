from django.shortcuts import render, redirect
from django.views import View
from .models import BenefitCard, IntroSlideContent, EquipmentSlideContent, Catalog, TopBlinds, Portfolio, NumOfStatistic
from .forms import ContactUsForm
from django.contrib import messages

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


class AboutView(View):
    def get(self, request):
        facts = NumOfStatistic.objects.first()
        return render(request, 'core/about.html', {'facts': facts})

class PortfolioView(View):
    def get(self, request):
        portfolio = Portfolio.objects.all()
        context = {
            'portfolio': portfolio
        }
        return render(request, 'core/portfolio.html', context)


class ContactView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'core/contact.html', {'form': form})

    
    def post(self, request):
        form = ContactUsForm(request.POST)
        

        if form.is_valid():
            messages.success(request, 'Ваща сообщения была отправлено!')
            form.save()
            # Add any other logic for form submission, such as sending emails or redirecting to success page
            return redirect('contact')
        else:
            return render(request, 'core/contact.html', {'form': form})