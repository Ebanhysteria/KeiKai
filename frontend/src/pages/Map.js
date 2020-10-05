import React from 'react'
import { Layout } from 'antd';
import MapKeikai from '../components/Map';
import Filters from '../components/Filters'
import styled from '@emotion/styled';


const { Header, Footer, Sider, Content } = Layout;


const HeaderStyled = styled(Header)`
    background-color: #fff;
`

const SiderStyled = styled(Sider)`
    background-color: #fff;
    width: 40rem;
    padding: 2rem 2rem;
`

const LayoutStyled = styled(Layout)`
    min-height: 1000px;
`

const MapPage = () => {
    return ( 
        <>
            <LayoutStyled>
                <HeaderStyled>
                    <h1>The expansion of artificial night light into sanctuaries of biodiversity</h1>
                </HeaderStyled>
                <Layout>
                    <SiderStyled
                        width={300}
                    >
                        <Filters/>
                    </SiderStyled>
                    <Content><MapKeikai/></Content>
                </Layout>
                <Footer>Keikai &copy; 2020</Footer>
            </LayoutStyled>
        </>
     );
}
 
export default MapPage;