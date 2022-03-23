### RDF for description of a game: senet and object details
This module describes the data element of a game (e.g "Senet"). These elements, defined by the Ludeme project, can be found on the [Structure of Game Table](https://ludii.games/downloads/DLP_Database_Guide.pdf) and the dataset in [this link](data/tableGames.csv).

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
@prefix wiki: <http://www.wikidata.org/entity/>


# rdf syntax generated manually:
# <https://w3id.org/ludeme/game/3> a schema:Game;
#   dc:description "Senet is one of the oldest board games known in the world, documented from about 3000 BCE until the first millennium BCE in Egypt. It was also played In Cyprus for most of that time, and played at different times in the Levant. Though a full ruleset has never been found, hints from texts and tomb paintings in Egypt give us clues about the manner in which it was likely played. The game was also heavily imbued with religious significance, as the board itself represented the journey through the afterlife.";
#   rdfs:label "Senet" .



<https://ludii.games/identifier.php?Id=DLP.Games.3> a schema:Game ; # https://ludii.games/details.php?keyword=Senet
    schema:additionalType schema:DiscoverAction ;
    dcterms:object "http://vocab.getty.edu/aat/300222752" ; #related vocabularies for game object or wiki: https://www.wikidata.org/wiki/Q131436
    dcterms:title "Entry in Table Games for ID number 3" ;
    dcterms:identifier "3" ; #id
    dc:description "Senet is one of the oldest board games known in the world, documented from about 3000 BCE until the first millennium BCE in Egypt. It was also played In Cyprus for most of that time, and played at different times in the Levant. Though a full ruleset has never been found, hints from texts and tomb paintings in Egypt give us clues about the manner in which it was likely played. The game was also heavily imbued with religious significance, as the board itself represented the journey through the afterlife."; #Description
    rdfs:label "Senet" ; #Name or NativeName
    schema:countryOfOrigin "Egipt" ; #Origin, RegionId
    schema:project "1"^^xsd:boolean ; #DLPGame
    ludeme:publicGame "1"^^xsd:boolean ; #PublicGame
    schema:alternativeName "XXX" ; #knownalias
    schema:author "ZZ" ; #Author
    schema:publisher "ddd" ; # publisher
    schema:startTime "-0031"^^xsd:gYear ; #Date, PeriodId wiki:P580 31. century BCE
    schema:isProprietary "0"^^xsd:boolean ; #ProprietaryGame
    schema:credit "XXX" ; ## ????
    schema:isRelatedTo "" ; #SeeAlso
    ludeme:EvidenceRange "5504, 5504" ; ## ???
    ## FROM DATA ARGUMENTATION
    schema:image "https://media.britishmuseum.org/media/Repository/Documents/2014_10/9_11/b1268a6e_e324_4afe_9ab9_a3bf00b6214d/preview_00505785_001.jpg" ; #imagefromBritishMuseum
    schema:latitude "444"xsd:float ; #OriginPoint
    schema:longitude "44.3"^^xsd:float ; #OriginPoint
    schema:category "board, Race, Escape" ; #category
    schema:additionalProperty :_MainRuleset ; #MainRuleset
    schema:additionalProperty :_Concepts ; #all related concepts for a game
    schema:author "Original author or designer of the game, where applciable" ; #author
    schema:publisher "Original publisher or designer of the game, where applciable" ;
    schema:provenance "Museum excavations" ;
    schema:seeAlso "https://www.metmuseum.org/art/collection/search/553268" #met
    schema:seeAlso "https://collections.louvre.fr/ark:/53355/cl010007877" #louvre

:_MainRuleset a schema:additionalPropery ;
    dcterms:title "this is the name of the ruleset" #Name
    schema:identifier "528" ; #id
    dc:description " Played on a 3x10 board. Pieces can be five or seven in number. Two players. Four casting sticks used as dice. Boustrophedon track from top left to bottom right. " ; #summary #description
    rdfs:label "Senet" ; #Name or NativeName
    ludii:type "Primary identifier of the RulesetTypes table value associated with this ruleset" ; #type
    ludii:ruleset "-unique id- and name- and can be one or more three periods- These are the rules of this ruleset, described with reference to the main ruleset for this game" ; #Ruleset
    schema:gameItem "An item is an object within the game world that can be collected by a player or, occasionally, a non-player character." ; #Ruleset`
    schema:numberOfPlayers "Indicate how many people can play this game (minimum, maximum, or range)" ;
    schema:quest "The task that a player-controlled character, or group of characters may complete in order to gain a reward." ;
    wiki:P580 "31. century BCE" ; #Date, PeriodId
    schema:citation "" ; #SeeAlso
    schema:latitude "444" ; #OriginPoint
    schema:longitude "44.3" ; #OriginPoint

:_Concepts a schema:additionalPropery ; #select the ones for the network analysis
    <https://ludii.games/concepts.php?gameId=3> a schema:additionalPropery ;
    sio:statistics "XX" ; 


```