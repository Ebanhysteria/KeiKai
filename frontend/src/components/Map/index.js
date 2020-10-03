import React from 'react'
import DeckGL from '@deck.gl/react';
import { LineLayer } from '@deck.gl/layers';
import { StaticMap } from 'react-map-gl';
import { useQuery, gql } from '@apollo/client';

// GraphQL Queries
const TEST_QUERY = gql`
query {
    lightPList{
      edges{
        node{
          id,
          prueba
        }
      }
    }
  }
`


// Mapbox access
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoibWFudWVsY2hpbWFsIiwiYSI6ImNrZnM5d2NvZjExeXUyc3FqenRxNTUwYWwifQ.D92Arb1lUbmbPnSd1GQb2Q';


// Viewport settings
const INITIAL_VIEW_STATE = {
    longitude: -122.41669,
    latitude: 37.7853,
    zoom: 13,
    pitch: 0,
    bearing: 0
  };
  
  // Data to be used by the LineLayer
  const data = [
    {sourcePosition: [-122.41669, 37.7853], targetPosition: [-122.41669, 37.781]}
  ];

  


const MapKeikai = () => {
    // GraphQl
    const { loading, error, data } = useQuery(TEST_QUERY);

    if (data){
        console.log(data)
    }

    const layers = [
        new LineLayer({id: 'line-layer', data})
    ]

    return (
        <> 
            {loading ? null : <p>Listo</p>}
            <DeckGL
            initialViewState={INITIAL_VIEW_STATE}
            controller={true}
            layers={layers}
            >
                
                <StaticMap mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN} />
            </DeckGL>
        </>
     );
}
 
export default MapKeikai;