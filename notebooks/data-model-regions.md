### Example RDF (turtle):

```ttl
@prefix : <http://mapping.example.com/> .
@prefix d2rq: <http://www.wiwiss.fu-berlin.de/suhl/bizer/D2RQ/0.1#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix fnml: <http://semweb.mmlab.be/ns/fnml#> .
@prefix fno: <https://w3id.org/function/ontology#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix grel: <http://users.ugent.be/~bjdmeest/function/grel.ttl#> .
@prefix idlab: <http://example.com/idlab/function/> .
@prefix idsf: <https://w3id.org/um/ids/rmlfunctions.ttl#> .
@prefix ludeme: <https://w3id.org/ludeme/> .
@prefix ludii: <https://w3id.org/ludeme/ontology/#> .
@prefix pubmed: <https://identifiers.org/pubmed:> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix schema: <https://schema.org/> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix wiki: <http://www.wikidata.org/entity/> .
@prefix geonames: <http://www.geonames.org/ontology#> 


# rdf syntax generated manually:
# <https://w3id.org/ludeme/game/3> a schema:Game;
#   dc:description "Senet is one of the oldest board games known in the world, documented from about 3000 BCE until the first millennium BCE in Egypt. It was also played In Cyprus for most of that time, and played at different times in the Levant. Though a full ruleset has never been found, hints from texts and tomb paintings in Egypt give us clues about the manner in which it was likely played. The game was also heavily imbued with religious significance, as the board itself represented the journey through the afterlife.";
#   rdfs:label "Senet" .

## From Table 1: Structure of Game Table https://ludii.games/downloads/DLP_Database_Guide.pdf


# rdf for description of a game: senet and object details
<https://ludii.games/identifier.php?Id=DLP.Games.3> a schema:Game ; # https://ludii.games/details.php?keyword=Senet
   schema:DiscoverAction "https://schema.org/DiscoverAction" ;
    dcterms:object "http://vocab.getty.edu/aat/300222752" ; #related vocabularies for game object or wiki: https://www.wikidata.org/wiki/Q131436
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
    geonames:7729893 "0"^^xsd:boolean ;# Central Asia
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