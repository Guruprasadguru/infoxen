from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from app.models import Lead
from app.serializers import Leadserializer
from rest_framework.pagination import PageNumberPagination


class LeadApiView(ListCreateAPIView):
    queryset = Lead.objects.all().order_by('time_stamp')
    serializer_class = Leadserializer
    pagination_class = PageNumberPagination


from django.shortcuts import render

# Create your views here.
