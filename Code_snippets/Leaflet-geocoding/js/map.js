// Create Leaflet tilelayer with OS Mapping API

var OS = new L.TileLayer('https://api.ordnancesurvey.co.uk/mapping_api/service/zxy/{tilematrixSet}/{layer}/{z}/{x}/{y}.{imgFormat}?apikey={apikey}', {
    apikey: 'INSERT_YOUR_API_KEY_HERE',
    tilematrixSet: 'EPSG:27700',
    layer: 'Zoom Map Tactical 27700',
    imgFormat: 'png',
    continuousWorld: true
});

var baseMaps = {
    "Ordnance Survey": OS
};

// Set up projection support and resolutions

var epsg27700 = "+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.999601 +x_0=400000 +y_0=-100000 +ellps=airy +towgs84=446.448,-125.157,542.060,0.1502,0.2470,0.8421,-20.4894 +datum=OSGB36 +units=m +no_defs";
var crs = new L.Proj.CRS(
    'EPSG:27700',
    epsg27700, {
        transformation: new L.Transformation(1, 0, -1, 1376256),
        resolutions: [896.0, 448.0, 224.0, 112.0, 56.0, 28.0, 14.0, 7.0, 3.5, 1.75, 0.875, 0.4375, 0.21875, 0.109375],
    });
    
// Create map

var map = L.map('map', {
    crs: crs,
    layers: OS,
    zoomControl: true,
    maxZoom: 13,
    minZoom: 0,
    center: ([51.507222, -0.1275]),
    zoom: 4
});

L.control.layers(baseMaps).addTo(map);

// Add OS Places geocoding with leaflet-control-geocoder

var geocoder = L.Control.geocoder({
    geocoder: new L.Control.Geocoder.OSPlaces('INSERT_YOUR_API_KEY_HERE'),
    placeholder: "Search addresses"
}).addTo(map);

// Add click nearest OS Places with leaflet-control-geocoder

var marker;

map.on('click', function(e) {
        geocoder.options.geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function(results) {
            var r = results[0];
            if (r) {
                if (marker) {
                    map.removeLayer(marker);
                }
                marker = L.marker(r.center).bindPopup(r.html || r.name).addTo(map).openPopup();
            }
        })
    });