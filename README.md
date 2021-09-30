
# FAIR Data for Historical Games

This is a repo for [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021)

[Proposal Accepted](files/CLARIAH-F-2021_paper.pdf)

---

## Abstract

The ERC-Digital Ludeme Project (DLP) is constructing a database of historical evidence for Ancient games, aiming at modeling the evolution of games throughout history. This database is unique in its scale, and its development is constrained by the unreliable nature of the data, lacking standards with other historical datasets. PLAYFAIR will apply FAIR principles to our dataset to maximise its usefulness and longevity, and explore the use of Semantic Web and Linked Data (LD) approaches for this purpose.
We will connect our dataset — that is the world’s most comprehensive dataset on Ancient games — with others, to make a universally FAIR to everyone, and find sources for additional data to complete our own set.
PLAYFAIR will tackle the challenge of developing an LD workflow using CLARIAH, show the power of the Semantic Web to answering a research question, and enhance data published on the Web in any applications of digital humanities.

## Data Identification

- This are examples of games in different museums:
    + Ancient game in Louvre: https://collections.louvre.fr/ark:/53355/cl010006455
    + Ancient game in British Museum: https://www.britishmuseum.org/collection/object/Y_EA22323 (game-board keyword search: https://www.britishmuseum.org/collection/term/x6970) 
    + Ancient game in Metropolitan Museum of Art: https://www.metmuseum.org/art/collection/search/55326

- This is the list of API/database links to integrate:
    + Metropolitan Art Museum: https://github.com/metmuseum/openaccess/blob/master/MetObjects.csv
    + The British Museum:no active sparql endpoint https://old.datahub.io/dataset/british-museum-collection or collection.britishmuseum.org/sparql          


## Documentation

### Install locally

Install dependencies:

```bash
yarn global add @rmlio/yarrrml-parser
wget https://github.com/RMLio/rmlmapper-java/releases/download/v4.12.0/rmlmapper.jar
pip install cow-csvw
```

### Run RML mapper

```powershell
cd etl
.\run.ps1
```

### Run CoW

Export the games table to a `games.csv` file

Generate the metadata file with CSVw mappings:

```powershell
cow_tool build data/tableGames.csv
```

Run the CSVw mappings to generate RDF:

```powershell
cow_tool convert data/tableGames.csv
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

## License

**Copyright (C) 2021, CLARIAH-PLUS WP1: CP-21-F-I 5**

MIT License 

---

