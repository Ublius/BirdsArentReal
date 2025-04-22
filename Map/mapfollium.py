import folium

# Create a map centered on the United States
us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Example datapoints: (name, latitude, longitude)
locations = [
    ("birds1", 47.6062, -122.3321),
    ("bird2", 34.0522, -118.2437),
    ("bird3", 39.7392, -104.9903),
    ("bird4", 41.8781, -87.6298),
    ("bird5", 29.7604, -95.3698),
    ("bird6", 40.7128, -74.0060),
    ("bird8", 25.7617, -80.1918),
    ("clear", 33.7490, -84.3880),
    ("asdfjkl;", 33.4484, -112.0740)
]

# Add markers to the map
for name, lat, lon in locations:
    folium.Marker(
        location=[lat, lon],
        popup=name,
        tooltip=f"Click for more about {name}"
    ).add_to(us_map)

# Save the map to an HTML file
us_map.save("us_map_with_markers.html")
