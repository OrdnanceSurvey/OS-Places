// Create Leaflet tilelayer with OS Mapping API

var OS = new L.TileLayer('https://api.ordnancesurvey.co.uk/mapping_api/service/zxy/{tilematrixSet}/{layer}/{z}/{x}/{y}.{imgFormat}?apikey={apikey}', {
    apikey: '7XTyNJ0sXvUoiOgkcwcqJ8aSkFgHOD4H',
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
    zoom: 12
});

L.control.layers(baseMaps).addTo(map);

// Initialise the FeatureGroup to store editable layers

var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

// Initialise the draw control and pass it the FeatureGroup of editable layers

var drawControl = new L.Control.Draw({
    draw: {
        polyline: false,
        polygon: false,
        marker: false
    }
});

// Add draw control and address layer group

map.addControl(drawControl);
var addresses = new L.LayerGroup();

// On draw query OS Places and display markers

map.on('draw:created', function(e) {

    var type = e.layerType,
        layer = e.layer;

    addresses.clearLayers();

    if (type === 'rectangle') {
        var sw = proj4('WGS84', epsg27700, [layer._latlngs[0].lng, layer._latlngs[0].lat]);
        var ne = proj4('WGS84', epsg27700, [layer._latlngs[2].lng, layer._latlngs[2].lat]);
        var bbox = sw[0].toFixed(2) + ',' + sw[1].toFixed(2) + ',' + ne[0].toFixed(2) + ',' + ne[1].toFixed(2);

        $.ajax('https://api.ordnancesurvey.co.uk/places/v1/addresses/bbox?', {
            data: {
                bbox: bbox,
                key: 'cSUnSnxJXhibWYPqaC58MlSqqJldByak'
            },
            crossDomain: true
        }).done(function(data) {

            for (var i = 0; i < data.results.length; i++) {
                var coord = L.latLng(proj4(epsg27700, 'WGS84', [data.results[i].DPA.X_COORDINATE, data.results[i].DPA.Y_COORDINATE]))
                var latLng = L.latLng(coord.lng, coord.lat);
                var marker = L.marker(latLng).addTo(addresses)
                marker.bindPopup(data.results[i].DPA.ADDRESS).openPopup();

            }

            map.addLayer(addresses);

        });
    }
    else if (type === 'circle') {
        var radius = layer.getRadius().toFixed(2);
        var projpoint = (proj4('WGS84', epsg27700,[layer.getLatLng().lng, layer.getLatLng().lat]));
        var point = projpoint[0].toFixed(2) + ',' + projpoint[1].toFixed(2);

        $.ajax('https://api.ordnancesurvey.co.uk/places/v1/addresses/radius?', {
            data: {
                point: point,
                radius: radius,
                key: 'cSUnSnxJXhibWYPqaC58MlSqqJldByak'
            },
            crossDomain: true
        }).done(function(data) {

            for (var i = 0; i < data.results.length; i++) {
                var coord = L.latLng(proj4(epsg27700, 'WGS84', [data.results[i].DPA.X_COORDINATE, data.results[i].DPA.Y_COORDINATE]))
                var latLng = L.latLng(coord.lng, coord.lat);
                var marker = L.marker(latLng).addTo(addresses)
                marker.bindPopup(data.results[i].DPA.ADDRESS).openPopup();

            }

            map.addLayer(addresses);

        });
    }
});