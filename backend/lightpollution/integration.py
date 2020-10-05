### POSIBLE PARAMETERS

"""

'key', 'offset', 'limit', 'page', 'datasetKey', 'publishingOrgKey', 'installationKey', 'publishingCountry', 'protocol', 
'lastCrawled', 'lastParsed', 'crawlId', 'extensions', 'basisOfRecord', 'occurrenceStatus', 'taxonKey', 'kingdomKey', 'phylumKey', 
'classKey', 'orderKey', 'familyKey', 'genusKey', 'speciesKey', 'acceptedTaxonKey', 'scientificName', 'acceptedScientificName', 
'kingdom', 'phylum', 'order', 'family', 'genus', 'species', 'genericName', 'specificEpithet', 'taxonRank', 'taxonomicStatus', 
'dateIdentified', 'decimalLongitude', 'decimalLatitude', 'coordinateUncertaintyInMeters', 'stateProvince', 'year', 'month', 'day', 
'eventDate', 'issues', 'modified', 'lastInterpreted', 'references', 'license', 'identifiers', 'media', 'facts', 'relations', 
'gadm', 'geodeticDatum', 'class', 'countryCode', 'recordedByIDs', 'identifiedByIDs', 'country', 'rightsHolder', 'identifier', 
'verbatimEventDate', 'datasetName', 'collectionCode', 'gbifID', 'verbatimLocality', 'occurrenceID', 'taxonID', 'catalogNumber', 
'recordedBy', 'institutionCode', 'rights', 'eventTime', 'identifiedBy', 'identificationID'

"""

### GBIF API

import requests
import json
import pandas as pd


class GBIF:
    
    year_min = 2015
    year_max = 2020

    def make_payload(self, year, page=0):
        offset = page*300
        return {"offset": offset,
                "limit": "300",
                "scientificName": "Chiroptera",
                "occurrenceStatus": "PRESENT",
                "basisOfRecord": "HUMAN_OBSERVATION",
                "year": f"{year}",
                "coordinateUncertaintyInMeters": "0,500",
                "hasCoordinate": "True",
                "hasGeospatialIssue": "False"
            }

    def get_data(self, record):
        return {"decimalLongitude": record["decimalLongitude"],
                "decimalLatitude": record["decimalLatitude"],
                "scientificName": record["scientificName"],
                "year": record["year"]}

    def validating_data(self, record):
        columns = {"decimalLongitude", "decimalLatitude", "scientificName", "year", "coordinateUncertaintyInMeters"}
        
        difference = columns.difference(set(record.keys()))
        
        return None if difference else self.get_data(record)


    page = 0
    current_year = True
    response = []

    for year in range(year_min, year_max+1):
        
        while current_year:
            
            payload = make_payload(year, page)
            
            print("payload: ", payload)
            
            _ = requests.get("https://api.gbif.org/v1/occurrence/search", params=payload)
            
            data = _.json()["results"]
            
            print("data: ", len(data))
            
            
            if data:
                _ = list(map(validating_data, data))
                
                response += list(filter(lambda record: record is not None, _))

                print("response: ", len(response))
                
                page +=1
                
                continue
                
            else:
                break
                
            
        df = pd.DataFrame(response)
                
        df['COORDINATES'] = df.apply(lambda x: [x.decimalLongitude, x.decimalLatitude], axis=1)
        df.scientificName = df.scientificName.str.lower().str.replace(' ','_').str.replace(',','')
        df.drop(['decimalLongitude', 'decimalLatitude'], axis=1, inplace=True)

        df_groups = df.groupby(['scientificName', 'year'])

        for group, tmp_data in df_groups:
            tmp_data_copy = tmp_data.copy()
            
            tmp_data_copy["WEIGHT"] = 1
            
            data_json = tmp_data_copy[["COORDINATES", "WEIGHT"]].to_dict("records")
            
            with open(f"./data/{group[0]}_{group[1]}.json", 'w') as f:
                json.dump(data_json, f)
        
        response = []
        page = 0

