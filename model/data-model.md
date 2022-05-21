### RDF for description of a game: senet and object details
This module describes the data element of a game (e.g "Senet"). These elements, defined by the Ludeme project, can be found on the [Structure of Game Table](https://ludii.games/downloads/DLP_Database_Guide.pdf) and the dataset in [this link](../data/tableGames.csv).

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


# rdf syntax generated manually:

<https://ludii.games/identifier.php?Id=DLP.Games.3> a schema:Game ;
    schema:isRelatedTo british:collection, louvre:collection;
    schema:additionalType schema:DiscoverAction ;
    schema:sameAs "http://vocab.getty.edu/aat/300217912" ;
    schema:identifier "3" ; #id
    dc:description "Senet is one of the oldest board games known in the world[...]The game was also heavily imbued with religious significance."; #Description
    rdfs:label "Senet" ; #Name or NativeName
    schema:countryOfOrigin "Egipt" ; #Origin
    schema:project "1"^^xsd:boolean ; #DLPGame
    schema:alternativeName "Znt" ; #knownalias
    schema:author "" ; #Author
    schema:publisher "" ; # publisher
    ludeme:creatorOfLud "XXX" ; ## credit
    schema:isRelatedTo "" ; #SeeAlso
    ludeme:EvidenceRange "530,3199"^^xsd:float . ## ???

## FROM LINK BRITISH & LOUVRE Digital collection

<https://www.britishmuseum.org/collection/object/Y_EA22323> a schema:game ;
    schema:isRelatedTo ludeme:collection, louvre:collection ;
    schema:image "https://media.britishmuseum.org/media/Repository/Documents/2014_10/9_11/b1268a6e_e324_4afe_9ab9_a3bf00b6214d/preview_00505785_001.jpg" ;
    schema:productionDate "1400BC-1200BC" ;
    wiki:Q11514315 "26th Dynasty" ;
   schema:identifier "No:EA22323" ;
   schema:material "copper pottery" .

<https://collections.louvre.fr/en/ark:/53355/cl010007877> a schema:game ;
    schema:isRelatedTo ludeme:collection, british:collection ;
    schema:material "copper pottery" .
```