# pdf-search

Search PDF files in 100+ languages using Qdrant and Cohere.

### Installation guide

Install the dependencies using pip

```
pip install -r requirements.txt
```

Setup Qdrant

1. Create a [Qdrant](https://qdrant.tech/) account
2. Create a new cluster to get your `dqrant_url` and `qdrant_api_key`

Env variables

Assign all of these env variables:

```
cohere_api_key="***"
openai_api_key="***"
qdrant_url="***"
qdrant_api_key="***"
```

### Run the app

Use the command below to run the app and it should be available with these API routes `/embed` and `/retrieve`.

```
gunicorn app:app
```
