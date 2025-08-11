# wikidata-queries
Examples of Wikidata SPARQL queries

### Jupyter Notebook examples

These examples show how to query Wikidata using SPARQL:
- [Retrieve from Wikidata touristc locations in Alicante](https://nbviewer.org/github/hibernator11/wikidata-queries/blob/main/notebooks/wikidata-dataspace-example.ipynb)

## Running the notebooks
**To execute the notebook in Binder:**

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hibernator11/wikidata-queries/HEAD)

### Works from the Biblioteca Virtual Miguel de Cervantes with an unknown author
```
select ?sLabel
where {
      ?s wdt:P3976 ?idwork .
      ?s p:P50 ?o . 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```

### Works from the BnF with an unknown author
```
select ?s ?sLabel
where {
      ?s wdt:P268 ?idwork .
      ?s p:P50 ?o . 
      ?o pq:P3831 wd:Q4233718
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} limit 1000
```

### Works from the National Library of Spain with an unknown author
```
select ?s ?sLabel
where {
      ?s wdt:P950 ?idwork .
      ?s p:P50 ?o . 
      ?o pq:P3831 wd:Q4233718
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} limit 1000
```

### Works from the National Library of Spain with an author with preferred rank (see, for instance, https://www.wikidata.org/wiki/Q233780)
```
select *
where {
      ?s wdt:P950 ?idwork .
      ?s p:P50 ?o . 
      ?o wikibase:rank wikibase:PreferredRank
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} limit 1000
```

### Other examples: Research Organization Registry (ROR) institutions: https://w.wiki/8w6j

```
#defaultView:Map
SELECT ?s ?sLabel ?countryLabel ?img ?coord
WHERE { 
    VALUES ?type {wd:Q31855 wd:Q3918}
    ?s wdt:P31 ?type .
    ?s wdt:P17 ?country .
    ?s wdt:P6782 ?ror .
    ?country wdt:P625 ?coord.
    OPTIONAL {?s wdt:P18 ?img .}   
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 100
```
## Museums

### Museo del Prado and place of birth of the artists: https://w.wiki/E5fo

```
#defaultView:Map
SELECT ?s ?sLabel ?nacimientoLabel ?img ?coord
WHERE { 
    ?s wdt:P19 ?nacimiento .
    ?s wdt:P5321 ?idPrado .
    ?nacimiento wdt:P625 ?coord.
    OPTIONAL {?s wdt:P18 ?img .}   
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es". }
}
LIMIT 100
```

### Properties of museums in Spain: https://w.wiki/E5mb
```
SELECT ?museo ?museoLabel ?propiedad ?propiedadLabel
WHERE {
  ?museo wdt:P31/wdt:P279* wd:Q33506 . 
  ?museo wdt:P17 wd:Q29 .
  ?museo wdt:P1687 ?propiedad
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es". }
}
LIMIT 100
```

### Properties of museums in Wikidata: https://w.wiki/E73G
```
SELECT distinct ?museo ?museoLabel ?propiedad ?propiedadLabel
WHERE {
  ?museo wdt:P31/wdt:P279* wd:Q33506 . 
  ?museo wdt:P1687 ?propiedad
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,mul". }
}
order by ?museoLabel
LIMIT 500
```

### Items per property in Art museums with more than 5000 records connected: https://w.wiki/EzrX

```SELECT distinct ?museo ?museoLabel ?propiedad ?propiedadLabel (count(?item) as ?total)
WHERE {
  ?museo wdt:P31/wdt:P279* wd:Q207694 . 
  ?museo wdt:P1687 ?propiedad .
  ?propiedad wdt:P31 wd:Q44847669 .
  BIND(URI(REPLACE(STR(?propiedad), STR(wd:), STR(wdt:))) AS ?id)
  ?item ?id ?value
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
group by ?museo ?museoLabel ?propiedad ?propiedadLabel
having(?total>5000)
order by ?total
LIMIT 100 OFFSET 0
```

### Items per property in museums with at least 1000 items connected: https://w.wiki/E73u

```
SELECT distinct ?museo ?museoLabel ?propiedad ?propiedadLabel (count(?item) as ?total)
WHERE {
  ?museo wdt:P31/wdt:P279* wd:Q33506 . 
  ?museo wdt:P1687 ?propiedad .
  BIND(URI(REPLACE(STR(?propiedad), STR(wd:), STR(wdt:))) AS ?id)
  ?item ?id ?value
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,mul". }
}
group by ?museo ?museoLabel ?propiedad ?propiedadLabel
having(?total>1000)
order by ?museoLabel
LIMIT 500
```

### Works provided by El Prado museum : https://w.wiki/EEpE

```
SELECT *
WHERE{
  ?s wdt:P31 wd:Q3305213.
  ?s wdt:P571 ?inception .
  ?s wdt:P1476 ?title .
  ?s wdt:P135 ?movement . ?movement rdfs:label ?movementLabel . FILTER (lang(?movementLabel) = 'es') .
  ?s wdt:P276 ?location . ?location rdfs:label ?locationLabel . FILTER (lang(?locationLabel) = 'es') .
  ?s wdt:P136 ?genre . ?genre rdfs:label ?genreLabel . FILTER (lang(?genreLabel) = 'es') .
  ?s wdt:P170 ?author . ?author rdfs:label ?authorLabel . FILTER (lang(?authorLabel) = 'es') .
  ?s wdt:P180 ?depicts . ?depicts rdfs:label ?depictsLabel . FILTER (lang(?depictsLabel) = 'es') .
  ?s wdt:P1071 ?locationcreation . ?locationcreation rdfs:label ?locationcreationLabel . FILTER (lang(?locationcreationLabel) = 'es') .
  ?s wdt:P8905 ?idPrado .
}
LIMIT 1000
```

## Monuments in Alicante
```
#defaultView:Map
select ?s ?type ?typeLabel ?sLabel ?coord ?location ?image ?statusLabel ?describedAt ?website ?inception ?architech ?architechLabel ?styleLabel
where {
  {
      values ?type {wd:Q4989906 wd:Q1772504 wd:Q2080521 wd:Q207694 wd:Q174782 wd:Q41176 wd:Q860861 wd:Q44613 wd:Q16560 wd:Q56750657 wd:Q2388635 wd:Q1007870}
      ?s wdt:P31 ?type .
      ?s wdt:P131 wd:Q11959 . 
      ?s wdt:P625 ?coord .
      optional {?s wdt:P276 ?location .}
      optional {?s wdt:P18 ?image .}  
      optional {?s wdt:P1435 ?status}
      optional {?s wdt:P973 ?describedAt}
      optional {?s wdt:P856 ?website}
      optional {?s wdt:P571 ?inception}
      optional {?s wdt:P84 ?architech}
      optional {?s wdt:P149 ?style}
   }
   UNION 
   {
      values ?type {wd:Q22996476}
      ?s wdt:P31 ?type .
      ?s wdt:P1001 wd:Q11959 . 
      ?s wdt:P625 ?coord .
      optional {?s wdt:P276 ?location .}
      optional {?s wdt:P18 ?image .}  
      optional {?s wdt:P1435 ?status}
      optional {?s wdt:P973 ?describedAt}
      optional {?s wdt:P856 ?website}
      optional {?s wdt:P571 ?inception}
      optional {?s wdt:P84 ?architech}
     optional {?s wdt:P149 ?style}
   }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es". }
}
```

### References

- https://www.semantic-web-journal.net/content/assessing-weaker-logical-status-claims-wikidata-cultural-heritage-records-1
- Gustavo Candela: An automatic data quality approach to assess semantic data from cultural heritage institutions. J. Assoc. Inf. Sci. Technol. 74(7): 866-878 (2023). https://doi.org/10.1002/asi.24761
- https://en.wikibooks.org/wiki/SPARQL/WIKIDATA_Qualifiers,_References_and_Ranks
- https://www.wikidata.org/wiki/Help:Qualifiers
