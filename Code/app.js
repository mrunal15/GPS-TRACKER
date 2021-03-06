// Initialize the map
var map = L.map('map', {
 scrollWheelZoom: false
});
// Set the position and zoom level of the map
map.setView([19.07, 72.87], 7);
// Initialize the base layer
var osm_mapnik = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
 maxZoom: 19,
 attribution: '&copy; OSM Mapnik <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
