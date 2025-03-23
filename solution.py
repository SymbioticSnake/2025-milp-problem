import geopandas as gpd
import numpy as np
import shapely as shp

def check_adjacent(coords1, coords2):
    match = False; currIdx = 0
    while (not match) and currIdx < 4:
        current = (coords1[currIdx], coords1[currIdx+1])
        for nextIdx in range(4):
            if ( np.array_equal(current[0], coords2[nextIdx]) and np.array_equal(current[1], coords2[nextIdx+1]) or
                 np.array_equal(current[0], coords2[nextIdx+1]) and np.array_equal(current[1], coords2[nextIdx]) ):
                match = True
                break
        currIdx += 1
    return match

parcels = gpd.read_file("land_parcels.shp").to_crs('EPSG:3347')
parcels['area'] = parcels.area / ((10**3)**2)

# Print minimum area
print("Minimum area (km^2):", min(parcels['area']))
print("Average area (km^2):", np.average(parcels['area']))
print("Maximum area (km^2):", max(parcels['area']))

print("carbon_store range:", max(parcels['carbon_sto'])-min(parcels['carbon_sto']))
print("cost range:", max(parcels['cost'])-min(parcels['cost']))

# Check for outliers by checking 3IQR below first quartile
q1 = np.percentile(parcels['area'], 25)
q3 = np.percentile(parcels['area'], 75)
range_min = q1 - 3*(q3 - q1)

count = 0
for index,row in parcels.iterrows():
    if row['area'] < range_min:
        parcels.drop(index, inplace=True)
        count += 1

print(count, "outliers detected and removed")

# Construct adjacency list by checking matching edges
coordinates = [shp.get_coordinates(geo) for geo in parcels['geometry']]
adjacency_list = []
for i in range(100-count):
    adjacents = []
    for j in range(99-count):
        if check_adjacent(coordinates[i], coordinates[(i+j+1)%100]): adjacents.append((i+j+1)%100)
    adjacency_list.append(adjacents)

