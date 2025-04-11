# User Identity Graph

Let's build an Identity graph


## Sample Data
![map](./docs/graph.png)


## Setup Gcloud 

```bash
gcloud auth application-default login
make instancecreate
make loadschema
```


## Get Python setup and load the Data

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./load_data.py
```

## Start Querying

[Queries](./SampleQueries.md)

## Benchmarking

There is a sample Benchmarking script that runs a few hop queries to give a basic idea of end to end latency

```bash
cd ./snippets
./parameterize.py
```


