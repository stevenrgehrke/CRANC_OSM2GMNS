
import osm2gmns as og

place_name = "Arizona, US"

try:
    # Use the relation ID retrieved earlier
    rel_id = 162018
    print(f"OSM Relation ID: {rel_id}")

    # Download the OSM data
    og.downloadOSMData(rel_id, 'arizona.osm')
    print("OSM data downloaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")