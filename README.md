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

### References

- https://www.semantic-web-journal.net/content/assessing-weaker-logical-status-claims-wikidata-cultural-heritage-records-1
- Gustavo Candela: An automatic data quality approach to assess semantic data from cultural heritage institutions. J. Assoc. Inf. Sci. Technol. 74(7): 866-878 (2023). https://doi.org/10.1002/asi.24761
- https://en.wikibooks.org/wiki/SPARQL/WIKIDATA_Qualifiers,_References_and_Ranks
- https://www.wikidata.org/wiki/Help:Qualifiers
