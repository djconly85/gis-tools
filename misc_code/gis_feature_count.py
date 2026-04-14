"""Code snippet to quickly count features, even in a very large file, without loading the entire dataset into memory."""

import fiona
import geopandas as gpd

# Use a context manager to open the file safely
test = r"D:\Users\dconly\projects_aws\ucd_acc_tool\data\raw\parcel.gdb.zip"
testlyr = gpd.list_layers(test).name.values[0]
with fiona.open(test, layer=testlyr) as source:
    # Accessing __len__ specifically returns the count from metadata
    feature_count = len(source)
    print(f"Total features: {feature_count}")