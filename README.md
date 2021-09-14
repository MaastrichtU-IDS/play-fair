# FAIR Data for Historical Games

This is a repo for [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021)

[Proposal Accepted](files/CLARIAH-F-2021_paper.pdf)

---

## Abstract

The ERC-Digital Ludeme Project (DLP) is constructing a database of historical evidence for Ancient games, aiming at modeling the evolution of games throughout history. This database is unique in its scale, and its development is constrained by the unreliable nature of the data, lacking standards with other historical datasets. PLAYFAIR will apply FAIR principles to our dataset to maximise its usefulness and longevity, and explore the use of Semantic Web and Linked Data (LD) approaches for this purpose.
We will connect our dataset — that is the world’s most comprehensive dataset on Ancient games — with others, to make a universally FAIR to everyone, and find sources for additional data to complete our own set.
PLAYFAIR will tackle the challenge of developing an LD workflow using CLARIAH, show the power of the Semantic Web to answering a research question, and enhance data published on the Web in any applications of digital humanities.

## Data 

Ancient game in Louvre: https://collections.louvre.fr/ark:/53355/cl010006455

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
cd data
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

MariaDB on DSRI (5.5.68-MariaDB.

```bash
oc new-app mariadb-persistent -p DATABASE_SERVICE_NAME=mariadb \
  -p MYSQL_USER=mariadb \
  -p MYSQL_PASSWORD=ludiluda \
  -p MYSQL_ROOT_PASSWORD=ludiluda \
  -p MYSQL_DATABASE=ludiiGames \
  -p MARIADB_VERSION=10.3-el8 \
  -p VOLUME_CAPACITY=10Gi \
  -p MEMORY_LIMIT=2Gi
```

Delete the database on DSRI:

```bash
oc delete all,secret,pvc,configmaps,serviceaccount,rolebinding --selector template=mariadb-persistent-template
```

Try starting [MariaDB 5.5 with Helm](https://github.com/bitnami/charts/blob/master/bitnami/mariadb/values.yaml):

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Start MariaDB 5.5:

```bash
helm install mariadb bitnami/mariadb \
    --set image.tag="5.5.48-0-r01" \
    --set serviceAccount.name=anyuid,serviceAccount.create=false \
    --set rbac.create=true,volumePermissions.enabled=true \
    --set auth.rootPassword=ludiluda,auth.database=ludiiGames \
    --set auth.username=mariadb,auth.password=ludiluda
```

Uninstall MariaDB 5.5:

```bash
helm uninstall mariadb
```

## License

**Copyright (C) 2021, CLARIAH-PLUS WP1: CP-21-F-I 5**

MIT License 

---

