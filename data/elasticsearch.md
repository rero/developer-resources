# elasticsearch

## Introduction

Elasticsearch is a distributed, RESTful search and analytics engine capable of solving a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data so you can discover the expected and uncover the unexpected.

## Main Concepts

- __cluster__: set of Elasticsearch instances that share the data of the same application
- __node__: one Elasticsearch instance of a cluster, in a cluster a master node is choosen by majority vote
- __shard__: Elasticsearch provides the ability to subdivide your index into multiple pieces called shards
  - __primary__: original indexes data
  - __replicat__: indexes data replication
- __index__: collection of documents that have somewhat similar characteristics; similar to a database in SQL
- __type__: or document type, logical category/partition of your index whose semantics is completely up to you; similar to a SQL database
- __document__: basic unit of information that can be indexed; similar to a row in a SQL table
- __field__: one entry of the document, can store `string`, `integer` `list`, `object`, etc.; similar to a table SQL cell

## Concepts

- __mapping__: the process of defining how a document, and the fields it contains, are stored and indexed
- __query__: search query with ranking results
- __filter__: boolean query without ranking
- __aggregator__: facets
- __analzyer__: transform a document value in a set of tokens; index entities
  - __char_filter__: are used to preprocess the stream of characters before it is passed to the tokenizer
  - __tokenizer__: receives a stream of characters, breaks it up into individual tokens
  - __token filter__: accept a stream of tokens from a tokenizer and can modify tokens; for example: `Lowercase Token Filter` or language stemmers

A complete Elasticsearch glossary is available in [2](#references).

## Installation

### Docker

```bash
docker run --name es --rm -ti -p 9200:9200 -p 9300:9300 elasticsearch
```

Open `http://localhost:9200` in a browser.

## References

1. [Official Documentations](https://www.elastic.co/guide/index.html)
2. [Elasticsearch Glossary](https://www.elastic.co/guide/en/elasticsearch/reference/current/glossary.html)
