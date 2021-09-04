# FAIR Data for Historical Games

This is a repo for [CLARIAH Fellowship Call 2021](https://www.clariah.nl/news/clariah-fellowship-call-2021)

[Proposal Accepted](files/CLARIAH-F-2021_paper.pdf)

---

## Abstract

The ERC-Digital Ludeme Project (DLP) is constructing a database of historical evidence for Ancient games, aiming at modeling the evolution of games throughout history. This database is unique in its scale, and its development is constrained by the unreliable nature of the data, lacking standards with other historical datasets. PLAYFAIR will apply FAIR principles to our dataset to maximise its usefulness and longevity, and explore the use of Semantic Web and Linked Data (LD) approaches for this purpose.
We will connect our dataset — that is the world’s most comprehensive dataset on Ancient games — with others, to make a universally FAIR to everyone, and find sources for additional data to complete our own set.
PLAYFAIR will tackle the challenge of developing an LD workflow using CLARIAH, show the power of the Semantic Web to answering a research question, and enhance data published on the Web in any applications of digital humanities.

## Documentation



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

MariaDB on DSRI.

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

## License

**Copyright (C) 2021, CLARIAH-PLUS WP1: CP-21-F-I 5**

MIT License 

---

