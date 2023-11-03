from rest_framework import viewsets, status
from rest_framework.response import Response
import src.app.service as service
from src.app.serializers import UserEventSerializer
from rest_framework.renderers import JSONRenderer


class EventController(viewsets.ViewSet):

    def get_result(self, request):
        json = None
        if service.check_user_ip(request):
            serializer = UserEventSerializer(service.get_last_5_events(), many=True)
            json = JSONRenderer().render(serializer.data)
            st = status.HTTP_200_OK
        else:
            st = status.HTTP_400_BAD_REQUEST
        return Response(data=json, status=st)

    def create(self, request):
        if service.create_event(request):
            st = status.HTTP_201_CREATED
        else:
            st = status.HTTP_400_BAD_REQUEST
        return Response(status=st)
