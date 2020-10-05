import {
    CHANGE_YEAR,
    CHANGE_RESOLUTION,
    CHANGE_INITIAL_VIEW_STATE,
    CHANGE_POLYGONS,
    CHANGE_REGION,
    CHANGE_LOAD
} from '../../types';

export default (state, action) => {
    switch (action.type) {
        case CHANGE_YEAR:
            return {
                ...state,
                Year: action.payload
            }

        case CHANGE_RESOLUTION:
            return {
                ...state,
                Resolution: action.payload
            }

        case CHANGE_REGION:
            return {
                ...state,
                region: action.payload
            }


        case CHANGE_POLYGONS:
            return {
                ...state,
                polygons: action.payload
            }

        case CHANGE_LOAD:
            return {
                ...state,
                loading: action.payload
            }

        case CHANGE_INITIAL_VIEW_STATE:
            return {
                ...state,
                initial_view_state: action.payload
            }

        default:
            return state;
    }
}