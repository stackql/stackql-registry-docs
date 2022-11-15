import React from 'react';
import GoogleMapReact from 'google-map-react';

const Map = props => {
    const { mapsApiKey, lat, long, defaultZoom, markerTitle } = props;
   
    const mapProps = {
        mapsApiKey: `${mapsApiKey}`,
        center: {
          lat: lat,
          lng: long
        },
        zoom: defaultZoom,
      };
    
      const renderMarkers = (map, maps) => {
        let marker = new maps.Marker({
        position: { lat: lat, lng: long },
        map,
        title: `${markerTitle}`
        });
        return marker;
       };

    return (
        <GoogleMapReact
        //style={{width: "100%", height: "100"}}
        defaultCenter={mapProps.center}
        defaultZoom={mapProps.zoom}
        />
    );
}

export default Map;