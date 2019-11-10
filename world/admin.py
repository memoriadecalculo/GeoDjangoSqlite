from django.contrib.gis import admin
from .models import WorldBorder

# Using OpenLayers
admin.site.register(WorldBorder, admin.GeoModelAdmin)

# Using OpenStreetMaps
# admin.site.register(WorldBorder, admin.OSMGeoAdmin)
