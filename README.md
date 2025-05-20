# wikidata-queries
Examples of Wikidata SPARQL queries



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

### Items per property in museums: https://w.wiki/E73e

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
order by ?museoLabel
LIMIT 500
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


### References

- https://www.semantic-web-journal.net/content/assessing-weaker-logical-status-claims-wikidata-cultural-heritage-records-1
- Gustavo Candela: An automatic data quality approach to assess semantic data from cultural heritage institutions. J. Assoc. Inf. Sci. Technol. 74(7): 866-878 (2023). https://doi.org/10.1002/asi.24761
- https://en.wikibooks.org/wiki/SPARQL/WIKIDATA_Qualifiers,_References_and_Ranks
- https://www.wikidata.org/wiki/Help:Qualifiers
