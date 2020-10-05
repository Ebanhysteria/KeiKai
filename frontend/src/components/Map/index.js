import React, {useState, useEffect, useContext} from 'react'
import DeckGL from '@deck.gl/react';
import { StaticMap } from 'react-map-gl';
import {HeatmapLayer} from '@deck.gl/aggregation-layers';
import MapContext from '../../context/map/mapContext';
import { GeoJsonLayer } from '@deck.gl/layers';


// Mapbox access
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoibWFudWVsY2hpbWFsIiwiYSI6ImNrZnM5d2NvZjExeXUyc3FqenRxNTUwYWwifQ.D92Arb1lUbmbPnSd1GQb2Q';


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

    // Context
    const { Year,region, initial_view_state, polygons } = useContext(MapContext);

    
    const PROTECTED_URL = polygons[0]

    const LIGHT_URL = `https://keikai-data.s3.us-east-2.amazonaws.com/NTL/1km/${region}/${region}_${Year}_1km.json` 
    
    // Data States
    const [lightdata, handleLightdata] = useState([]);
    const [protecteddata, handleProtectedData] = useState([]);
    

    

    useEffect(() =>{
      
      fetchData(LIGHT_URL, handleLightdata);
      
      fetchData(PROTECTED_URL, handleProtectedData);
      // eslint-disable-next-line

    }, [LIGHT_URL, PROTECTED_URL])

    useEffect(() => {
      
      // fetchData(EVI_URL, handleEvidata);
    }, [])
    

        
    const layers = [
        new HeatmapLayer({
          data: lightdata,
          id: 'heatmp-light',
          getPosition: d => d.COORDINATES,
          getWeight: d => d.WEIGHT,
          radiusPixels: 2,
        }),

        new GeoJsonLayer({
          data: protecteddata,
          opacity: 0.8,
          stroked: false,
          filled: true,
          extruded: true,
          wireframe: true,
    
          getFillColor: [48, 193, 50],
          getLineColor: [255, 255, 255],
    
          pickable: true
        })

    ]



    return (
        <div style={{"height": '90vh', "width": '100vw', "position": 'relative' }} >
            <DeckGL
            initialViewState={initial_view_state}
            layers={[layers]}

            >
              <StaticMap 
              
              preventStyleDiffing={true} 
              mapStyle="mapbox://styles/mapbox/dark-v9"
              mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN}/>
              
            </DeckGL>
        </div>
     );
}
 
export default MapKeikai;