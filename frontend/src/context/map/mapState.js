import React, { useReducer } from 'react'
import MapContext from './mapContext';
import MapReducer from './mapReducer';
import {
    CHANGE_YEAR,
    CHANGE_RESOLUTION,
    CHANGE_INITIAL_VIEW_STATE,
    CHANGE_POLYGONS,
    CHANGE_REGION,
    CHANGE_LOAD
} from '../../types';


const MapState = props => {

    const initialState = {
        loading: false,
        Year: 1992,
        Resolution: 100,
        region: "SAfrica",
        polygons: ['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/SAfrica_polygon.json'],
        initial_view_state : {
            "longitude": 24.946635,
            "latitude":  -30.028632,
            "zoom": 5,
            "pitch": 0,
            "bearing": 0
          }
    }

    const changeYear = (year) =>{
        dispatch({ type: CHANGE_YEAR, payload: year})
    }

    const changeResolution = (resolution) => {
        dispatch({ type: CHANGE_RESOLUTION, payload: resolution})
    }

    const changeInitialViewState = (data) => {
        dispatch({ type: CHANGE_INITIAL_VIEW_STATE, payload: data})
    }

    const changePolygons = (data) => {
        dispatch({ type: CHANGE_POLYGONS, payload: data})
    }

    const changeRegion = (data) => {
        dispatch({ type: CHANGE_REGION, payload: data})
    }

    const changeLoading = (data) => {
        dispatch({ type: CHANGE_LOAD, payload: data})
    }

    const [state, dispatch] = useReducer(MapReducer, initialState);

    return ( 
        <MapContext.Provider
            value={{
                Year: state.Year,
                region: state.region,
                Resolution: state.Resolution,
                polygons: state.polygons,
                loading: state.loading,
                initial_view_state: state.initial_view_state,
                changeInitialViewState,
                changeResolution,
                changePolygons,
                changeLoading,
                changeRegion,
                changeYear
                
            }}
        >
            {props.children}
        </MapContext.Provider>
     );
}
 
export default MapState;
