# astator
Python Intelligent Aide for Humans

#### History

Although there has been several attempts in making the machines intelligent, the early prototypes were still dumb. Until 2015. Then came 
the astator.

#### Introduction

Astator, aims to help humans by trying to understand them and answer their questions. They do not aim harm, they are here to help. But 
who knows, they might one day overthrow humans and rule the world, that I do not know.

#### Overview

The engine is written in Python. There is also a [Django interface](https://github.com/semihyagcioglu/advocatus) in the making, but you can 
use astator standalone as a Python package.

The first prototype of astator will be simple. They will parse the query, gather information, evaluate findings and answer the question.

#### Goal

The goal is have some fun, and see what this prototype can do.

#### Installation

I am planning to make a setup, but for the time being you can install astator via VCS.

```pip install git+git://github.com/astator/astator.git

or

pip install git+https://github.com/astator/astator.git

or without git

pip install —upgrade https://github.com/astator/astator/tarball/master```


#### Ideas

- Use google as source? We might need to rewrite the question. But when and how?
- Add wikipedia as knowledge base. Maybe simple english?
- Cosine similarity. gensim might be a good idea.
- Use synonyms. There are some online APIs out there.
- Planning to add CI and deployment to a production server, so that I can play with it anytime I want.
- How to score multiple sources, and rank them?
- Will probably need a database and an instantaneous search. Elasticsearch?
- Replace constant messages via redis?

# Roadmap

There are several ways to improve astator. Please let me know, if you have suggestions. Or better, you can contribute by just sending a pull request.