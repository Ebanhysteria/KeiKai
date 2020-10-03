import React from 'react';

// Apollo
import { ApolloProvider } from '@apollo/client';
import clientApollo from './config/apollo';


import './App.css';

import MapKeikai from './components/Map';

function App() {
  return (
    <ApolloProvider client={clientApollo}>
      <div className="App">
        <MapKeikai/>
      </div>
    </ApolloProvider>
  );
}

export default App;
