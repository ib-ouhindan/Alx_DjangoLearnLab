from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
def get_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user, is_read=False)
    notifications.update(is_read=True)  # Mark notifications as read
    return Response([{"actor": n.actor.username, "verb": n.verb, "target": str(n.target)} for n in notifications])
