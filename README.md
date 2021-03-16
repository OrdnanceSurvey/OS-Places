# OS Places API Demos

This repo contains working examples of how to use the Ordnance Survey Places API, a RESTful API based on OS [AddressBase Premium](https://www.ordnancesurvey.co.uk/business-and-government/products/addressbase-premium.html) datasets. The API returns queries to the service in either XML or JSON, and through a ['find'](https://apidocs.os.uk/docs/os-places-find) resource enables rapid searches of AddressBase Premium to drill down and isolate ambiguous addressing details. The ['match'](https://apidocs.os.uk/docs/os-places-match) resource is for more granular matching and cleansing of existing address databases. Neither features needs any database management of AddressBase Premium. ['Postcode'](https://apidocs.os.uk/docs/os-places-postcode) searches need the area and district integers as a minimum. There are JQuery examples using [getJSON](http://api.jquery.com/jquery.getjson/) and examples using [typeahead.js](https://twitter.github.io/typeahead.js/). Additionally [Leaflet](http://leafletjs.com/) and Openlayers examples are provided to facilliate the Geosearch resources.

Register for an API key of OS Places API [here](https://developer.ordnancesurvey.co.uk/user/register).

Full documentation for the OS Places API can be found [here](https://apidocs.os.uk/docs/os-places-overview), while service terms for OS Places API can be found [here](https://developer.ordnancesurvey.co.uk/sites/default/files/OS_Places_v2-1.pdf).

## License

These demos are released under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0.html).
