### Example RDF (turtle):

```ttl
@prefix ludeme: <https://w3id.org/ludeme/> .
@prefix ludii: <https://w3id.org/ludeme/ontology/#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix getty: <http://vocab.getty.edu/aat/> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix wiki: <https://www.wikidata.org/wiki/> .
@prefix british: <https://www.britishmuseum.org/> .
@prefix louvre: <https://collections.louvre.fr/en/ark:> .
@prefix geonames: <http://www.geonames.org/ontology#> 


# rdf syntax generated manually:

## From Table 1: Structure of Game Table https://ludii.games/downloads/DLP_Database_Guide.pdf


# rdf for description of a game: senet and object details
<https://ludii.games/identifier.php?Id=DLP.Games.3> a schema:Game ; 
   schema:DiscoverAction "https://schema.org/DiscoverAction" ;
    schema:sameAs "http://vocab.getty.edu/aat/300217912" ;
    rdfs:label "Senet" ; #GameName
    schema:identifier "3" ; #Gameid
    schema:additionalProperty :_MainRuleset .
:_MainRuleset a schema:additionalPropery ;
    rdfs:label "Bell" ; #RulesetName
    schema:identifier "529" ; #RulesetId
    dc:description " Played on a 3x10 board. Pieces can be five or seven in number. Two players. Four casting sticks used as dice. Boustrophedon track from top left to bottom right. " ; #summary #description
    geonames:7729889 "0"^^xsd:boolean ; #Eastern Africa
    geonames:7729886 "0"^^xsd:boolean ; #Middle Africa
    geonames:7729887 "1"^^xsd:boolean ; #Northern Africa
    geonames:7729885 "0"^^xsd:boolean ; #Southern Africa
    geonames:7729887 "0"^^xsd:boolean ; #Western Africa
    geonames:7729892 "0"^^xsd:boolean ; # Central America
    geonames:7729890 "0"^^xsd:boolean ;# Northern America
    geonames:6255150 "0"^^xsd:boolean ; # South America
    geonames:7729893 "0"^^xsd:boolean ; # Central Asia
    wiki:Q27329 "0"^^xsd:boolean ; #Northern Asia !!!!
    geonames:7729894 "0"^^xsd:boolean ; #Eastern Asia
    geonames:7729896 "0"^^xsd:boolean ; #Southeastern Asia
    geonames:7729895 "0"^^xsd:boolean ; #Southern Asia
    geonames:7729897 "0"^^xsd:boolean ; #Western Asia
    geonames:7729898 "0"^^xsd:boolean ; #Australia and New Zealand
    geonames:7729891 "0"^^xsd:boolean ; #Caribbean
    geonames:7729884 "0"^^xsd:boolean ; #Eastern Europe
    geonames:7729883 "0"^^xsd:boolean ; #Northern Europe
    geonames:9408658 "0"^^xsd:boolean ; #Southern Europe
    geonames:9408659 "0"^^xsd:boolean ; #Western Europe
    geonames:7729899 "0"^^xsd:boolean ; #Melanesia
    geonames:7729900 "0"^^xsd:boolean ; #Micronesia
    geonames:7729901 "0"^^xsd:boolean . #Polynesia
```