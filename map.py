import folium

title_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Natalie's Travels</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<nav>
    <div class="map-title">
      <span>Natalie's Travels</span>
    </div>
  </a>
</nav>
'''

# Centered roughly on Europe
map_center = [51.522881, 15.215209] #Grill Bar u Wacka, Poland

# Create the map object
my_map = folium.Map(location=map_center, tiles="Cartodb Positron", zoom_start=4)

my_map.get_root().html.add_child(folium.Element(title_html))

def create_custom_icon(image_path):
    return folium.CustomIcon(
        icon_image=image_path,
        icon_size=(30, 40),
        icon_anchor=(15, 15),
        popup_anchor=(0, 0), 
        )

locations = [
    {
        "city": "Uppsala, Sweden",
        "location": [59.8586, 17.6389],
        "blog": "blog/uppsala.html",
        "icon": "images/location_icon.png"
    },
    {
        "city": "Bergen, Norway",
        "location": [60.3913, 5.3221],
        "blog": "blog/bergen.html",
        "icon": "images/location_icon.png"
    },
    {
        "city": "Dublin, Ireland",
        "location": [53.3498, -6.2603],
        "blog": "blog/dublin.html",
        "icon": "images/location_icon.png"
    },
    {
        "city": "Brussels, Belgium",
        "location": [50.8503, 4.3517],
        "blog": "blog/brussels.html",
        "icon": "images/location_icon.png"
    },
    {
        "city": "Prague, Czech Republic",
        "location": [50.0755, 14.4378],
        "blog": "blog/prague.html",
        "icon": "images/location_icon.png"
    },
]

for place in locations:
    popup_html = f'<div class="map_words">My trip to <a href="{place["blog"]}" target="_blank" class="map_links">{place["city"]}</a>!</div>'
    popup = folium.Popup(popup_html, max_width=500)
    marker = folium.Marker(
        location=place["location"],
        popup=popup,
        icon=create_custom_icon(place["icon"])
    )
    marker.add_to(my_map)

# Add custom CSS
css_link = '<link rel="stylesheet" type="text/css" href="css/style.css">'
css_element = folium.Element(css_link)
my_map.get_root().html.add_child(css_element)

my_map.save("index.html")
print("Map generated