var global_map;
var global_layer;
var global_restos;
var global_location;

var userPrefs = JSON.parse(localStorage.getItem("userPrefs"));

if(userPrefs == null) {
userPrefs = {}
userPrefs.gluten_free = false;
userPrefs.vegan = false;
}

function display_closest_restaurant () {
  // Need to have fetched all the restaurants and the current location
  if (!global_restos)
    return;
  if (!global_location)
    return;

  closest_resto = _.min(global_restos, function(resto) { return resto.latlng.distanceTo(global_location) });

  // Use user's position as origin of the point of symetry so it stays centered
  var symetry = [ 2 * global_location.lat - closest_resto.latlng.lat, 2 * global_location.lng - closest_resto.latlng.lng]

  global_map.fitBounds([global_location, closest_resto.latlng, symetry]);
}

function map_init (map, options) {
    global_map = map;
    // markercluster
    var markers_cluster = new L.MarkerClusterGroup({ disableClusteringAtZoom: 17 });

    if(global_layer != null && map.hasLayer(global_layer))
      global_map.removeLayer(global_layer);

    $.getJSON("restaurants.json", function(data) {
      // Add restaurant markers
      for (var i = 0; i < data.length; i ++) {
        var resto = data[i];

        resto.latlng = L.latLng(resto.lat, resto.lon)
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

      global_restos = data;
      display_closest_restaurant();
    })

    map.addOneTimeEventListener('locationfound', function (e) {
      global_location = e.latlng;
      display_closest_restaurant();
    });

    // Locate user
    var lc = L.control.locate({ 'setView': false }).addTo(map);
    lc.locate();

    global_layer = markers_cluster;
    map.addLayer(markers_cluster);
}
