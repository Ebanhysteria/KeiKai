import { ApolloClient, InMemoryCache } from '@apollo/client';


const clientApollo = new ApolloClient({
    uri: 'http://127.0.0.1:8000/graphql',
    cache: new InMemoryCache(),
})


export default clientApollo;
