import React, {useState, useEffect} from 'react'
import DeckGL from '@deck.gl/react';

import {StaticMap, Source, Layer} from 'react-map-gl';
import { useQuery, gql } from '@apollo/client';
import {HeatmapLayer} from '@deck.gl/aggregation-layers';

// GraphQL Queries
const TEST_QUERY = gql`
query {
    lightPList{
      edges{
        node{
          id,
          latitude,
          longitude
        }
      }
    }
  }
`


// Mapbox access
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoibWFudWVsY2hpbWFsIiwiYSI6ImNrZnM5d2NvZjExeXUyc3FqenRxNTUwYWwifQ.D92Arb1lUbmbPnSd1GQb2Q';


// Viewport settings
const INITIAL_VIEW_STATE = {
    longitude: -124.07404299999999,
    latitude:  40.886975,
    zoom: 2,
    pitch: 0,
    bearing: 0
  };
  
const LIGHT_URL = 'https://keikai-data.s3.us-east-2.amazonaws.com/NTL/10km/NTL_2014_10.json' // 
const BAT_URL = 'https://keikai-data.s3.us-east-2.amazonaws.com/Chiroptera_gbif/Tadarida_brasiliensis_2014.0.json' // eslint-disable-line
  




// Function to fetch data

function fetchData(url, handleState){
  fetch(url)
    .then(response => response.json())
    .then((jsonData) => {
      // jsonData is parsed json object received from url
      handleState(jsonData);
    })
    .catch((error) => {
      // handle your errors here
      console.error(error)
    })
}

const MapKeikai = () => {
    const [batdata, handleBatdata] = useState([]);
    const [lightdata, handleLightdata] = useState([]);

    

    useEffect(() =>{
      fetchData(LIGHT_URL, handleLightdata);
      fetchData(BAT_URL, handleBatdata);

    }, [])
    

        
    const layers = [
        new HeatmapLayer({
          data: lightdata,
          id: 'heatmp-light',
          getPosition: d => d.COORDINATES,
          getWeight: d => d.WEIGHT,
          radiusPixels: 10,
        }),
        new HeatmapLayer({
          data: batdata,
          id: 'heatmp-bats',
          getPosition: d => d.COORDINATES,
          getWeight: d => d.WEIGHT,
          radiusPixels: 20,
          colorRange: [[1, 152, 189, 255], [73, 227, 206, 255], [216, 254, 181, 255], [254, 237, 177, 255],[254, 173, 84, 255],[209, 55, 78, 255]]
        }),

    ]



    return (
        <> 
            <DeckGL
            initialViewState={INITIAL_VIEW_STATE}
            controller={true}
            layers={layers}
            >
              <StaticMap 
              mapStyle='mapbox://styles/mapbox/dark-v9'   
              preventStyleDiffing={true} 
              mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN}/>
               
            </DeckGL>
        </>
     );
}
 
export default MapKeikai;