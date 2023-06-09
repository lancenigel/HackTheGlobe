from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Athlete
from .serializers import AthleteSerializer
from rest_framework import generics, serializers
from django.shortcuts import get_object_or_404, render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import render


class AthleteCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AthleteSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data).is_valid()
            if not serializer:
                raise serializers.ValidationError(
                    {'detail': 'Invalid data provided'},
                )
            athlete = Athlete.objects.create(
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                ethnicity=request.data.get('ethnicity'),
                sex=request.data.get('sex'),
                weight=request.data.get('weight'),
                height=request.data.get('height'),
                blood_type=request.data.get('blood_type'),
                sport=request.data.get('sport'),
                phone=request.data.get('phone'),
                email=request.data.get('email'),
                contact_method=request.data.get('contact_method'),
                coach=self.request.user,
                athlete_image=request.data.get('athlete_image'),
            )

            serializer = AthleteSerializer(athlete)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AthleteAll(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AthleteSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    template_name = 'index.html'

    def get_queryset(self):
        athletes = Athlete.objects.filter(coach=self.request.user)
        return athletes

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AthleteSerializer(queryset, many=True)
        return render(request, self.template_name, {'athletes': serializer.data})


class AthleteCRUD(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AthleteSerializer
    template_name = 'card.html'

    def get_queryset(self):
        athlete_id = self.kwargs.get('athlete_id')
        athletes = Athlete.objects.filter(id=athlete_id, coach=self.request.user)
        return athletes

    def delete(self, request, *args, **kwargs):
        athlete = self.get_object()
        athlete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AthleteSerializer(queryset, many=True)
        return render(request, self.template_name, {'athletes': serializer.data})