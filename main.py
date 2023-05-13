import json
import os

from dotenv import load_dotenv
from flask import Flask, request
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import CohereEmbeddings
from langchain.vectorstores import Qdrant

from flask_cors import CORS

load_dotenv()
openai_api_key = os.environ.get('openai_api_key')
cohere_api_key = os.environ.get('cohere_api_key')
qdrant_url = os.environ.get('qdrant_url')
qdrant_api_key = os.environ.get('qdrant_api_key')

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return {"Hello": "World"}


@app.route('/embed', methods=['POST'])
def embed_pdf():
    collection_name = request.json.get("collection_name")
    file_url = request.json.get("file_url")

    loader = PyPDFLoader(file_url)
    docs = loader.load_and_split()
    embeddings = CohereEmbeddings(model="multilingual-22-12", cohere_api_key=cohere_api_key)
    qdrant = Qdrant.from_documents(docs, embeddings, url=qdrant_url, collection_name=collection_name, prefer_grpc=True, api_key=qdrant_api_key)

    return {"collection_name": qdrant.collection_name}
