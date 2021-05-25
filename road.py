
import geopandas as gpd
import fiona

file = 'https://gist.githubusercontent.com/soobrosa/b3500853a0d4633fd963/raw/ecd9998983ec1dcad1b34d47c90871c9a9fc7e5d/sensor.kml'

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
df = gpd.read_file(file, driver='KML')

print(df)