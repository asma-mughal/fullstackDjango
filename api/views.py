from django.shortcuts import render
from rest_framework import generics, status
from . models import Room
from . serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self, request,format = None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.guest_can_pause
            votes_to_skip= serializer.data.votes_to_skip
