from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        # Logic for handling GET request
        return render(request, 'core/index.html')
