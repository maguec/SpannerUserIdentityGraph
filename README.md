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

There are some sample Benchmarking scripts that give an idea of latency of various usage scenarios

```bash
cd ./snippets
```


### 2 Hop Parameterized Queries

Run through 1000 parameterized 2 hop queries to understand basic latency

```bash
./parameterize.py
```

### Get Order Shapes

Grab 1000 sample transactions and they run a query shape on each of those with the Email, Address and CC id's to see if we see similar transaction shapes

```bash
./get_order_shapes.py
```
