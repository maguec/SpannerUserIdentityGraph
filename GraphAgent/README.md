# Let's build an agent that asks graph questions

This utilizes ADK and MCP Toolbox

## Setup Gcloud 

```bash
gcloud auth application-default login
```

## Create the ENV file

```bash
cp env.sample .env
# edit the file
cp .env graph_agent/.env
source .env
```

## Get Python setup and load the Data

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Download the Toolbox

```bash
# If on linux
make getmcplinux

# If on Mac
make getmcpmac
```

## Start the Toolbox

```bash
make runtoolbox
```
## Start the Agent Kit

```bash
adk web
```

## Run Some Sample queries

[Sample Queries](./SampleScript.md)

## Gemini-cli

This also contains a sample [setttings.json](./settings.json) file for configuring the MCP server for [Gemini cli tool](https://github.com/google-gemini/gemini-cli)
