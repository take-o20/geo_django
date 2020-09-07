from django.contrib.gis import admin

# Register your models here.
from world.models import Border, School, Facility, Busstop

from leaflet.admin import LeafletGeoAdmin

class BorderAdmin(LeafletGeoAdmin):
    search_fields = ['n03_001', 'n03_003', 'n03_004']
    list_filter = ('n03_003')

admin.site.register(Border, LeafletGeoAdmin)
admin.site.register(School, LeafletGeoAdmin)
admin.site.register(Facility, LeafletGeoAdmin)
admin.site.register(Busstop, LeafletGeoAdmin)