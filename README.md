# GeoDjangoSqlite
GeoDjango using Sqlite

Considering already installed:

- Ubuntu 18.04
- Python 3.6.8
- Django==2.2.7
- pkg-resources==0.0.0
- pytz==2019.3
- spatialite==0.0.3
- sqlparse==0.3.0

As described at [Techiediaries](https://href.li/?https://www.techiediaries.com/django-gis-geodjango/), firstly install the libraries GEOS, PROJ.4 and GDAL:

    sudo apt-get install libgeos-dev
    sudo apt-get install binutils libproj-dev
    sudo apt-get install gdal-bin libgdal-dev
    sudo apt-get install python3-gdal

Follow the instructions described at the [Official GeoDjango Tutorial](https://href.li/?https://docs.djangoproject.com/pt-br/2.2/ref/contrib/gis/tutorial/).

Configure the DATABASE in **settings.py** as described by [sfikas](https://href.li/?https://github.com/Archaeocomputers/geodjango-sqlite/blob/master/geodjangoSpatialite/geodjangoSpatialite/settings.py):

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.spatialite',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
     }

Unfortunately, the **United Kingdom** record was breaking the **load.py** script:

    Failed to save the feature (id: 206) into the model with the keyword arguments:
    {'fips': 'UK', 'iso2': 'GB', 'iso3': 'GBR', 'un': 826, 'name': 'United Kingdom'
    ...
    sqlite3.IntegrityError: NOT NULL constraint failed: world_worldborder.mpoly
    ...
    django.db.utils.IntegrityError: NOT NULL constraint failed: world_worldborder.mpoly

I only could handle it setting the **mpoly/geom** field **null=True** in the **models.py**:

    mpoly = models.MultiPolygonField(null=True)

It is not a complete solution because at least **United Kingdom** record was ignored. But it was a very good workaround. I don’t think there is a problem in the **TM_WORLD_BORDERS-0.3.shp**. It seems there is a problem when Django try to generate the SQL.
