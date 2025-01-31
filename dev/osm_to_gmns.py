import osm2gmns as og

# Path to your OSM file
osm_file = "arizona.osm"  # Update if needed

# Load the network (without 'network_type')
net = og.getNetFromFile(osm_file)

# Output GMNS format files
og.outputNetToCSV(net, output_folder="gmns_network")

print("OSM to GMNS conversion completed! GMNS files saved in 'gmns_network' folder.")


#method2
# import osm2gmns as og

# # Specify the OSM file you downloaded
# osm_file = 'arizona-small.osm'

# try:
#     # Get the network from the OSM file
#     net = og.getNetFromFile(osm_file)

#     # Output the network to CSV files in GMNS format
#     og.outputNetToCSV(net)
#     print(f"GMNS network data has been saved to CSV.")
    
# except Exception as e:
#     print(f"An error occurred: {e}")