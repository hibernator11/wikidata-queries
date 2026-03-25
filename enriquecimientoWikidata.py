from SPARQLWrapper import SPARQLWrapper, JSON, RDFXML, POST


def get_wikidataId(municipio, provincia):
    
    sparql = SPARQLWrapper(
        "https://query.wikidata.org/sparql"
    )

    sparql.setMethod(POST)
    sparql.setReturnFormat(JSON)
    
    
    string = """
    SELECT ?municipio ?municipioLabel ?provincia ?provinciaLabel ?provinciaEs
    where {{?municipio wdt:P31 wd:Q2074737 .
           ?municipio wdt:P17 wd:Q29 .
           ?municipio rdfs:label ?municipioEs . FILTER( LANG(?municipioEs)="es" )
           FILTER(CONTAINS(?municipioEs, "{}")).   
           ?municipio wdt:P131 ?provincia .
           ?provincia rdfs:label ?provinciaEs . FILTER( LANG(?provinciaEs)="es" )
           FILTER(CONTAINS(?provinciaEs, "{}")).    
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es". }}
    }}
    LIMIT 10
    """.format(municipio, provincia)
    
    print(string)

    sparql.setQuery(string)
    
    try:
        ret = sparql.queryAndConvert()
        #print(ret)
        for r in ret["results"]["bindings"]:
            print(r["municipio"]["value"] + " - " + r["provincia"]["value"])
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    get_wikidataId("Elda", "Alicante")
    get_wikidataId("Monóvar", "Alicante")
    get_wikidataId("Novelda", "Alicante")
    get_wikidataId("Aspe", "Alicante")
