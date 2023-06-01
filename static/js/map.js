document.addEventListener("DOMContentLoaded", function () {
    const dots = [];

    // Map settings
    const map_view_settings = new ol.View({
        center: ol.proj.fromLonLat([60.614522838336555, 56.83597279595725]), // Default coordinates of EKB
        maxZoom: 18,
        zoom: 12,
    });

    const map_layer_settings = new ol.layer.Tile({
        source: new ol.source.OSM({
            url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
            attributions: [ol.source.OSM.ATTRIBUTION, 'Tiles courtesy of <a href="https://geo6.be/">GEO-6</a>'],
        })
    });

    const map_controls_settings = ol.control.defaults({
        attribution: new ol.control.Attribution({
            collapsible: true
        })
    });
    // Map initialization
    const map = new ol.Map({
        controls: map_controls_settings,
        layers: [map_layer_settings],
        target: 'map',
        view: map_view_settings,
    });

    coordinates.forEach(function (currentValue) {
        dots.push(
            new ol.Feature({
                geometry: new ol.geom.Point(ol.proj.fromLonLat([currentValue[0], currentValue[1]]))
            }));
    });

    const layer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: dots
        })
    });
    map.addLayer(layer);
});