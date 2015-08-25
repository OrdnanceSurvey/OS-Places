var places = new Bloodhound({
    datumTokenizer: function(d) {
        return Bloodhound.tokenizers.whitespace(d.value);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    remote: {
        url: 'https://api.ordnancesurvey.co.uk/places/v1/addresses/find?query=%QUERY&key=INSERT_YOUR_API_KEY_HERE',
        filter: function(places) {
            // Map the remote source JSON array to a JavaScript object array
            return $.map(places.results, function(address) {
                return {
                    ADDRESS: address.DPA.ADDRESS,
                    X_COORDINATE: address.DPA.X_COORDINATE,
                    Y_COORDINATE: address.DPA.Y_COORDINATE,
                    value: address,
                    UPRN: address.DPA.UPRN
                };
            });
        }
    }
});

places.initialize();

$('.typeahead').typeahead({
    highlight: true
}, {
    name: 'Address',
    displayKey: 'ADDRESS',
    source: places.ttAdapter(),
    templates: {
        empty: [
            '<div class="tt-empty-message">',
            'No Results',
            '</div>'
        ].join('\n'),
        header: '<h4 class="tt-tag-heading tt-tag-heading2"> OS Places</h4>'
    }
});