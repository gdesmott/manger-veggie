var global_map;
var global_layer;

var userPrefs = JSON.parse(localStorage.getItem("userPrefs"));

if(userPrefs == null) {
userPrefs = {}
userPrefs.gluten_free = false;
userPrefs.vegan = false;
}

function map_init (map, options) {
    global_map = map;

    if(global_layer != null && map.hasLayer(global_layer))
      global_map.removeLayer(global_layer);

    $.getJSON("restaurants.json", function(data) {
      for (var i = 0; i < data.length; i ++) {
        var resto = data[i];
        //filter out restaurants based on the user's preferences
        if(userPrefs.gluten_free && $.inArray("gluten-free", resto.tags))
          continue;

        if(userPrefs.vegan && !($.inArray("vegan", resto.tags) || $.inArray("vegan-friendly", resto.tags)))
          continue;

        var icon = L.AwesomeMarkers.icon({
          icon: 'cutlery',
          markerColor: tags_to_color(data[i]["tags"]),
        })

        var marker = L.marker([resto.lat, resto.lon], {icon: icon}).bindPopup(Mustache.to_html(Mustache.TEMPLATES.restopopup, {resto: resto}));
        markers_cluster.addLayer(marker);
      }
    })

    // Locate user
    var lc = L.control.locate().addTo(map);
    lc.locate();

    // markercluster
    var markers_cluster = new L.MarkerClusterGroup({ disableClusteringAtZoom: 17 });
    global_layer = markers_cluster;
    map.addLayer(markers_cluster);
}