import React from 'react';

// Apollo
import { ApolloProvider } from '@apollo/client';
import clientApollo from './config/apollo';
import MapState from './context/map/mapState';


// import './App.css';

import MapPage from './pages/Map'

function App() {
  return (
    <ApolloProvider client={clientApollo}>
      <MapState>
        <div className="App">
          <MapPage/>
        </div>
      </MapState>
    </ApolloProvider>
  );
}

export default App;
