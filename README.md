
# FAIR Data for Historical Games

This is a repo for [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021)

[Proposal Accepted](files/CLARIAH-F-2021_paper.pdf)

[E-Data & Research Article](https://edata.nl/2022/01/31/historische-spelletjesdatabase-in-de-maak/)

---

## Objective

The aim of PLAY-FAIR project is to make a substantial contribution to enable realisation of the ambitions within CLARIAH Community to make collections FAIR for research and public engagement purposes.

> To make Historical games data Interoperable (the I in FAIR)

PLAYFAIR will tackle the challenge of developing an LD workflow using CLARIAH, show the power of the Semantic Web to answering a research question, and enhance data published on the Web in any applications of digital humanities.

## Documentation

### Data Identification & Argumentation

We link Ludeme dataset to data descriptors from British Museum as following:

- British Museum:
  + keyword: game-board
  + Query database: https://www.britishmuseum.org/collection/search?object=game-board
  + Download dataset: [collections-22-01-26-10 28 18.csv](data/collections-britishM.csv)    



Other sources from Museums to be integrated are currently investigated:

- Louvre Museum:
  + keyword: plateau de jeu
  + Query database: https://collections.louvre.fr/search/export?q=%22plateau%20de%20jeu%22
  + Download dataset csv format: [Link](https://collections.louvre.fr/recherche?q=%22plateau+de+jeu%22) 
  + Download dataset json format: [Link](https://collections.louvre.fr/search/export?q=%22plateau%20de%20jeu%22) 

- This is the list of API/database links to integrate:
    + Metropolitan Art Museum: https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv
    + The British Museum:no active sparql endpoint https://old.datahub.io/dataset/british-museum-collection or collection.britishmuseum.org/sparql


### PLAY-FAIR Data Model

Concepts and properties are annotated with general ontologies

+ [Data Model Game table](model/data-model.md)
+ [Data Model Ruleset Regions](model/data-model-regions.md)
+ [Data Model Ruleset Periods](model/data-model-periods.md)

### Install locally

Install dependencies:

```bash
yarn global add @rmlio/yarrrml-parser
wget https://github.com/RMLio/rmlmapper-java/releases/download/v4.12.0/rmlmapper.jar
pip install cow-csvw
```

### Run CoW

- Export the games table to a `tableGames.csv` file to `./data`:
  + [data/tableGames.csv](data/tableGames.csv)
  + [data/rulesetRegions.csv](data/rulesetRegions.csv)
  + [data/rulesetPeriods.csv](data/rulesetPeriods.csv)



Generate the metadata file with CSVw mappings:

```powershell
cow_tool build data/tableGames.csv
```

Change the json file generated:
* Change the base URI to w3id.org/ludeme
* Add `propertyUrl` to map to our predicates (cf. https://www.w3.org/TR/tabular-data-primer/#property-names)

- Generated Skeleton Schema in `./data`:
  + [tableGames.csv-metadata.json](data/tableGames.csv-metadata.json)
  + [rulesetRegions.csv-metadata.json](data/rulesetRegions.csv-metadata.json)
  + [rulesetPeriods.csv-metadata.json](data/rulesetPeriods.csv-metadata.json)



Run the CSVw mappings to generate RDF:

```powershell
cow_tool convert data/tableGames.csv
```


### Outputs




### Run RML mapper

```powershell
cd etl
.\run.ps1
```


### Start workspace

Start the workspace to run mappings to convert Ludeme data to RDF on DSRI:

```bash
oc new-app vscode-root -p APPLICATION_NAME=vscode \
  -p GIT_URL=https://github.com/MaastrichtU-IDS/play-fair \
  -p STORAGE_SIZE=10Gi \
  -p PASSWORD=CHANGEME
```

Delete the VSCode on DSRI:

```bash
oc delete all,secret,pvc,configmaps,serviceaccount,rolebinding --selector app=vscode
```

To run locally, you can use docker, run this command in the folder you want to see in the VSCode interface (the root of this repository):

```bash
docker run --rm -it -p 8080:8080 -e PASSWORD=password -e GIT_URL= -v $(pwd):/home/coder/project ghcr.io/maastrichtu-ids/code-server:latest
```

### Start database

Install MySQL with Helm:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Deploy MySQL in your DSRI project, this will automatically load the `ludiiGames` database, using the `values.yaml` file in this repository (feel free to adapt it for a different database):

```bash
helm install mysql bitnami/mysql -f mysql-helm-values.yaml
```

Forward the service to access it on your laptop at http://localhost:3306

```bash
oc port-forward svc/mysql 3306
```

You can now use your favorite tool to connect and explore the database, if you don't know which one to use we recommend to use the database administration tool [DBeaver](https://dbeaver.io/).

Delete MySQL deployment:

```bash
helm uninstall mysql
```


### Website

Want to learn more? Check out [PLAYFAIR Website!](https://www.clariah.nl/projects?page=2/)

_PLAYFAIR is a project of:_

<a href="https://www.maastrichtuniversity.nl/research/institute-data-science"><img src="images/Logo_IDS.jpg" width="50px" height="50px" alt="Institute of Data Science" /></a>&emsp;&emsp;&emsp;&emsp;<a href="https://www.clariah.nl//"><img src="images/Logo_Clariah.png" alt="Clariah Logo" width="80px" height="80px"/></a>

---


<a href="http://www.ludeme.eu/"><img src="images/LOGO_ERC-FLAG_EU_.jpg" width="150px" height="150px" alt="Ludeme Project Logo" /></a>

This research received funding from the CLARIAH Infrastructure (Grant Agreement No. CP-21-F-I 5) under the WP-3.
## License

**Copyright (C) 2021, CLARIAH-PLUS WP1: CP-21-F-I 5**

MIT License 

---

