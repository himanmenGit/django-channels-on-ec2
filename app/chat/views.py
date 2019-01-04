from django.views.generic import TemplateView

from chat.models import Room


class Home(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        Room.objects.get_or_create(name='노티룸', group_name='main')
        return super().get(request, *args, **kwargs)
