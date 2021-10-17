from chat.models import ChatRoom
from django.db.models import Count


def salas(View):
        salas = ChatRoom.objects.all().annotate(num_users=Count('users')).order_by('-num_users')
        return {'salas': salas}
