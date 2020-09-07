from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import BorderSerializer, SchoolSerializer, FacilitySerializer, BusstopSerializer
from .models import Border, School, Facility, Busstop

class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class BorderViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = False

class BusstopViewSet(viewsets.ModelViewSet):
    queryset = Busstop.objects.all()
    serializer_class = BusstopSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter, InBBoxFilter)
    distance_filter_field = bbox_filter_field = 'geom'
    distance_filter_convert_meters = True



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json
from django.core.serializers import serialize

class GeojsonAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            encjson  = serialize('geojson', Border.objects.filter(n03_004="中央区"),srid=4326, geometry_field='geom', fields=('n03_003','n03_004',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)
        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        return response


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    contexts = {}

    return render(request, 'world/index.html', contexts)