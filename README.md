
# ♟️ FAIR Data for Traditional Games

A RDF Knowledge graph for traditional games:

* This is a repo for [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021)

* [Proposal Accepted](files/CLARIAH-F-2021_paper.pdf)

* [DARIAH2022 Conference Paper-In prep](files/play_fair_dariah.pdf)

* More info [E-Data & Research Article](https://edata.nl/2022/01/31/historische-spelletjesdatabase-in-de-maak/)

---

## 🎯 Objective

> To make traditional games data Interoperable (the I in FAIR)

## 🧑‍💻 PLAY-FAIR Data Model

<p align="center"> 
	<img src="images/data-model.svg"> 
</p>


Concepts and properties are annotated with general (e.g. Schema.org, Dublin Core or wikipedia) and dedicated digital humanities (e.g. getty) ontologies:

+ [Data Model Game table](model/data-model.md) - describes a Game
+ [Data Model Ruleset Regions](model/data-model-regions.md) - describes the rulesets of a Game given geographical regions
+ [Data Model Ruleset Periods](model/data-model-periods.md) - describes the rulesets of a Game given historical periods



## 🎲 Data Identification & Argumentation

We link Ludeme dataset to data descriptors from the **Digital Collection of the British Museum** as following:

+ keyword: *game-board*
+ Query database: https://www.britishmuseum.org/collection/search?object=game-board
+ Download dataset: [collections-22-01-26-10 28 18.csv](data/collections-britishM.csv)    

Other sources from digital collection of international museums are *currently* being incorporated:

- **Louvre Museum**:
  + keyword: *plateau de jeu*
  + Query database: https://collections.louvre.fr/search/export?q=%22plateau%20de%20jeu%22
  + Download dataset csv format: [Link](https://collections.louvre.fr/recherche?q=%22plateau+de+jeu%22) 



See the ongoing [scripts](etl) and [notebooks](notebooks) using python.


## ♠️ Install locally

Install dependencies:

```bash
yarn global add @rmlio/yarrrml-parser
wget https://github.com/RMLio/rmlmapper-java/releases/download/v4.12.0/rmlmapper.jar
pip install cow-csvw
```

## 🐮 Run CoW for `Game` level:

- The **Input CSV file** is in `./data`:
  + [data/tableGames.csv](data/tableGames.csv)

- Generate the **metadata file** with CSVw mappings:

```powershell
cow_tool build data/tableGames.csv
```

- Change the json file generated:

  * Change the base URI to w3id.org/ludeme
  * Add `propertyUrl` to map to our predicates (cf. https://www.w3.org/TR/tabular-data-primer/#property-names)
- You can check our **JSON** Skeleton Schema in `./data`:
  + [tableGames.csv-metadata.json](data/tableGames.csv-metadata.json)

- Run the CSVw mappings to generate RDF:


```powershell
cow_tool convert data/tableGames.csv
```

- The **Output RDF file** is in `./data`:

  + [data/tableGames.csv.nq](data/tableGames.csv.nq)


## 🪄 **Convert spreadsheets to Linked Data for `Ruleset` level**

- The **Inputs CSV files** are in `./data`:
  + [data/rulesetRegions.csv](data/rulesetRegions.csv)
  + [data/rulesetPeriods.csv](data/rulesetPeriods.csv)

- Follow the instructions given here:
  + [https://humanities.wizard.semanticscience.org/](https://humanities.wizard.semanticscience.org/)

- The **Outputs RDF file** are in `./data`:

  + [data/rulesetRegions.csv.nq](data/rulesetRegions.csv.nq)
  + [data/rulesetPeriods.csv.nq](data/rulesetPeriods.csv.nq)


## 🪄 RDF files to Druid

- **Graphs**:

  + Datasets publicly available here: [https://druid.datalegend.net/UtrillaGuerreroC/playfair](https://druid.datalegend.net/UtrillaGuerreroC/playfair)


- **Services**:

  + The SPARQL endpoint is accessible at [https://druid.datalegend.net/UtrillaGuerreroC/playfair/sparql/playfairKG](https://druid.datalegend.net/UtrillaGuerreroC/playfair/sparql/playfairKG)


- **Check the SPARQL queries**

Queries from the grlc API can be checked and changed in the .rq files.
    
* Examples:
- [Get Games](queries/get-games.rq)
- [Get images](queries/get-games-images.rq)
- [Get network](queries/get-network.rq)

### Website

Want to learn more? Check out [PLAYFAIR Website!](https://www.clariah.nl/projects?page=2/)

---

### Acknowledgement
PLAYFAIR is funded by [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021):

<a href="https://www.maastrichtuniversity.nl/research/institute-data-science"><img src="images/Logo_IDS.jpg" width="150px" height="70px" alt="Institute of Data Science" /></a>&emsp;&emsp;&emsp;&emsp;<a href="https://www.clariah.nl//"><img src="images/Logo_Clariah.png" alt="Clariah Logo" width="150px" height="50px"/></a>

---


<a href="http://www.ludeme.eu/"><img src="images/LOGO_ERC-FLAG_EU_.jpg" width="150px" height="150px" alt="Ludeme Project Logo" /></a>

This research received funding from the CLARIAH Infrastructure (Grant Agreement No. CP-21-F-I 5) under the WP-3.
## License

**Copyright (C) 2021, CLARIAH-PLUS WP1: CP-21-F-I 5**

MIT License 

---

