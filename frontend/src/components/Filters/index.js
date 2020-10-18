import React, { useContext, useState } from 'react';
import { Select,  Radio, Divider, Badge } from 'antd';
import MapContext from '../../context/map/mapContext';
import {FlyToInterpolator} from 'deck.gl';
import {
    FileTextOutlined,
    GithubOutlined
  } from '@ant-design/icons';
const { Option } = Select;


const Filters = () => {


    const { changeYear, changeInitialViewState, changePolygons, changeRegion } = useContext(MapContext);

    const [value, handleValue] = useState("SAfrica");

    // Change year
    function handleChange(value) {
        changeYear(value);
    }

    // Change region
    const onChange = e => {
        handleValue(e.target.value);
        // Switch case
        switch(e.target.value){
            case "Korea":
                changeRegion(e.target.value);

                changeInitialViewState({
                    "longitude": 127.857694,
                    "latitude":  36.697944,
                    "zoom": 5,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3500,
                    "transitionInterpolator": new FlyToInterpolator()
                });

                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/KoreaS_polygon.json']);


                break;

            case "SAfrica":
                changeRegion(e.target.value);

                changeInitialViewState({
                    "longitude": 24.946635,
                    "latitude":  -30.028632,
                    "zoom": 5,
                    "maxZoom": 5,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3500,
                    "transitionInterpolator": new FlyToInterpolator()
                })

                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/SAfrica_polygon.json']);
                
                break;
            
            case "Thai":
                changeRegion('Asia1');

                changeInitialViewState({
                    "longitude": 100.308428,
                    "latitude":  14.895377,
                    "zoom": 5,
                    "maxZoom": 5,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3500,
                    "transitionInterpolator": new FlyToInterpolator()
                })
                
                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/Thai_polygon.json']);
                break;
            case "Cambodia":
                    changeRegion('Asia1');
    
                    changeInitialViewState({
                        "longitude": 104.308428,
                        "latitude":  14.895377,
                        "zoom": 5,
                        "maxZoom": 5.5,
                        "pitch": 0,
                        "bearing": 0,
                        "transitionDuration": 3000,
                        "transitionInterpolator": new FlyToInterpolator()
                    })
                    
                    changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/Cambodia_polygon.json']);
                    break;
            case "Laos":
                    changeRegion('Asia1');
    
                    changeInitialViewState({
                        "longitude": 104.308428,
                        "latitude":  14.895377,
                        "zoom": 5,
                        "maxZoom": 5.5,
                        "pitch": 0,
                        "bearing": 0,
                        "transitionDuration": 3000,
                        "transitionInterpolator": new FlyToInterpolator()
                    })
                    
                    changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/Laos_polygon.json']);
                    break;
            case "Mexico":
                changeRegion(e.target.value);

                changeInitialViewState({
                    "longitude": -97.552784,
                    "latitude":  23.634501,
                    "zoom": 4.5,
                    "maxZoom": 4.5,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3000,
                    "transitionInterpolator": new FlyToInterpolator()
                })
                
                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/Mexico_polygon.json']);
                break;

            case "Brazil":
                changeRegion(e.target.value);

                changeInitialViewState({
                    "longitude": -48.92528,
                    "latitude":  -14.235004,
                    "zoom": 4,
                    "maxZoom": 4,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3000,
                    "transitionInterpolator": new FlyToInterpolator()
                })
                
                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/Brasil_polygon.json']);
                break;
            default:
                changeRegion(e.target.value);

                changeInitialViewState({
                    "longitude": 127.857694,
                    "latitude":  36.697944,
                    "zoom": 4,
                    "maxZoom": 4,
                    "pitch": 0,
                    "bearing": 0,
                    "transitionDuration": 3000,
                    "transitionInterpolator": new FlyToInterpolator()
                });

                changePolygons(['https://keikai-data.s3.us-east-2.amazonaws.com/protected_polygons/KoreaS_polygon.json']);
        }
        
    };

    const radioStyle = {
        display: 'block',
        height: '30px',
        lineHeight: '30px',
      };
    
    return (
        <div style={{"marginBottom": "200px"}}>
            <h2>Region</h2>
            <Radio.Group onChange={onChange} value={value}>
                <Radio style={radioStyle} value="Korea">
                    Republic of Korea
                </Radio>
                <Radio style={radioStyle} value="SAfrica">
                    South Africa
                </Radio>
                <Radio style={radioStyle} value="Thai">
                    Thailand
                </Radio>
                <Radio style={radioStyle} value="Laos">
                    Laos
                </Radio>
                <Radio style={radioStyle} value="Cambodia">
                    Cambodia
                </Radio>
                <Radio style={radioStyle} value="Mexico">
                    Mexico
                </Radio>
                <Radio style={radioStyle} value="Brazil">
                    Brazil
                </Radio>
            </Radio.Group>
            <Divider/>
            <h2>Year</h2>
            <Select
                placeholder="Select a year"
                defaultValue="1992" 
                style={{ width: 120 }}
                onChange={handleChange}>
                <Option value="1992">1992</Option>
                <Option value="1993">1993</Option>
                <Option value="1994">1994</Option>
                <Option value="1995">1995</Option>
                <Option value="1996">1996</Option>
                <Option value="1997">1997</Option>
                <Option value="1998">1998</Option>
                <Option value="1999">1999</Option>
                <Option value="2000">2000</Option>
                <Option value="2001">2001</Option>
                <Option value="2002">2002</Option>
                <Option value="2003">2003</Option>
                <Option value="2004">2004</Option>
                <Option value="2005">2005</Option>
                <Option value="2006">2006</Option>
                <Option value="2007">2007</Option>
                <Option value="2008">2008</Option>
                <Option value="2009">2009</Option>
                <Option value="2010">2010</Option>
                <Option value="2011">2011</Option>
                <Option value="2012">2012</Option>
                <Option value="2013">2013</Option>
                <Option value="2014">2014</Option>
                <Option value="2015">2015</Option>
                <Option value="2016">2016</Option>
                <Option value="2017">2017</Option>
                <Option value="2018">2018</Option>

            </Select>
            <Divider/>
            <Badge color="#33cc33" text="Protected area" />
            <br/>
            <Badge color="#993333" text="Light pollution" />
            <Divider/>
            <a href="http://keikai-documentation.s3-website-us-east-1.amazonaws.com/" target="_blank" rel="noopener noreferrer">Documentation <FileTextOutlined/></a>
            <br/>
            <a href="https://github.com/Ebanhysteria/KeiKai" target="_blank" rel="noopener noreferrer">Keikai Github <GithubOutlined /></a>
        </div>

        
        
    );
}
 
export default Filters;