### Example RDF (turtle):

```ttl

@prefix ludeme: <https://w3id.org/ludeme/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix wiki: <http://www.wikidata.org/entity/>



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
    ludeme:Ancient "0"^^xsd:boolean ;
        schema:sameAs wiki:Q435608 ; #ancient history
    ludeme:Medieval "0"^^xsd:boolean ;
        schema:sameAs wiki:Q12554 ; #Medieval history
    ludeme:Modern "0"^^xsd:boolean ;
        schema:sameAs wiki:Q3281534 ; #Modern history
    ludeme:VeryEarlyMedieval "0"^^xsd:boolean ;
    ludeme:EarlyMedieval "0"^^xsd:boolean ;
        schema:sameAs wiki:Q202763 ; #Early Medieval
    ludeme:LateMedieval "0"^^xsd:boolean ;
        schema:sameAs wiki:Q212976 ; #Late Medieveal
    ludeme:1500s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q44140 ;
    ludeme:1600s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q42995 ;
    ludeme:1700s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q43370 ;
    ludeme:1800s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q39577 ;
    ludeme:1900s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q36574 ; 
    ludeme:2000s "0"^^xsd:boolean ;
        schema:sameAs wiki:Q35024 ; 
         
```