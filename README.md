![Flask](https://raw.githubusercontent.com/pallets/flask-website/master/flask_website/static/badges/flask-project-s.png)
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/anfederico/flaskex/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/35ba0b8c1364449baf1ed01331dac874)](https://www.codacy.com/app/charlesxdeng/Relex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=charlesxdeng/Relex&amp;utm_campaign=Badge_Grade)
![Relex](https://img.shields.io/badge/Relex-NLP-red.svg)
# Relex
------
A simple user-friendly NLP tool leveraging a powerful natural language processing library, regex, and intuitive pipelines to analyze text and extract entities, relations, and other syntactic features such as parsed syntactic trees.
## Why you should care
Perhaps:
1. You want a mental model or an example of what an NLP tool entails.
2. You need an intuitive tool that takes an object oriented approach to extracting information from text.
3. You are operating a web application that contains information you would like to analyze simply by sending a web request to an API endpoint.
4. You aim to define a quick solution easier to use than a text mining agent(TMA) and more scalable than regex.

## Documentation 📖
### Installing
spaCy is a library for advanced Natural Language Processing in Python and Cython. It's built on the very latest research, and was designed from day one to be used in real products. spaCy comes with pre-trained statistical models and word vectors, and currently supports tokenization for 30+ languages. It features the fastest syntactic parser in the world, convolutional neural network models for tagging, parsing and named entity recognition and easy deep learning integration. It's commercial open-source software, released under the MIT license.

Install the NLP library, Spacy IO, by following the instructions in the link: https://spacy.io/usage/

When using pip it is generally recommended to install packages in a virtual
environment to avoid modifying system state:
```
    python -m venv .env
    source .env/bin/activate
    pip install spacy
```
Install the language model "en_core_web_sm" needed to assign word vectors, context-specific token vectors, POS tags, dependency parse and named entities
```
python -m spacy download en_core_web_sm
```
https://devcenter.heroku.com/articles/heroku-cli
### Deploying to Heroku
**Tutorial:** https://www.youtube.com/watch?v=skc-ZEU9kO8&t=300s
```
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
#### Note:
Add the spacy model's github link instead of its python library name to the requirements.txt as shown below.

```
...
cymem==2.0.2
cytoolz==0.9.0.1
dill==0.2.9
spacy>=2.0.0,<3.0.0
https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz#en_core_web_sm
Flask==1.0.2
Flask-Cors==3.0.7
Flask-HTTPAuth==3.2.4
gunicorn==19.9.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
msgpack==0.5.6
msgpack-numpy==0.4.3.2
murmurhash==1.0.1
numpy==1.16.0
...
```




## Usage:
The entity and relation values can either be in a list or in a string separated by semicolons.
* Return relations from two different sets of entities:
    * POST https://secure-spire-37812.herokuapp.com/api/entity_entity
```
    {
      "entity_1_values": "Emmanuel Macron;Macron",
      "entity_2_values": ["France","United States","U.S", "US"],
      "entity_1_name": "PRESIDENTS",
      "entity_2_name": "COUNTRIES",
      "text": "Did France  President Emmanuel Macron sum up Brexit better than the British? Emmanuel Macron launches 'grand debate' tour in response to France's yellow vest protests. French President       Emmanuel Macron delivers a speech to mayors from rural Normandy during the 'grand debate' in Grand Bourgtheroulde on Tuesday. Macron encouraged people to express their grievances and propose changes, a strategy aimed to quell weeks of anti-government protests. (Philippe Wojazer/Pool Photo via AP) Macron was appointed Deputy Secretary General to the President by François Hollande in May 2012.
      "scope": 1,
    }
```

* Return entities given two unique sets of relations and entities:
    * POST https://secure-spire-37812.herokuapp.com/api/relation_entity
```
    {
        "entity_values": "Calcium channel blockers",
	      "relation_values": ["treat","relax","increase"],
    	  "entity_name": "drugs",
	      "relation_name": "cures",
	      "text": "Calcium channel blockers help treat chest pain (your doctor may say “angina”) and high blood pressure. They relax blood vessels and increase blood and oxygen to your heart. That eases its workload. They treat heart failure caused by hypertension. But they’re used only when other medicines to lower blood pressure don’t work. Ask your doctor if one is right for you.",
	      "scope": 3,
}
```
* Return sentences containing entities and relations given both :
    * POST https://secure-spire-37812.herokuapp.com/api/all_entities_relations
```
{
    "entity_1_values": "Emmanuel Macron;Macron",
    "entity_2_values": ["France", "United States", "U.S", "US"],
    "entity_1_name": "PRESIDENTS",
    "entity_2_name": "COUNTRIES",
    "relation_values":["launches"],
    "relation_name":"actions",
	  "text":
	    "Did French President Emmanuel Macron sum up Brexit better than the British? Emmanuel Macron launches 'grand debate' tour in response to France's yellow vest protests. French President Emmanuel Macron delivers a speech to mayors from rural Normandy during the 'grand debate' in Grand Bourgtheroulde on Tuesday. Macron encouraged people to express their grievances and propose changes, a strategy aimed to quell weeks of anti-government protests. (Philippe Wojazer/Pool Photo via AP) Macron was appointed Deputy Secretary General to the President by François Hollande in May 2012. He was appointed Minister of Economy, Industry and Digital Affairs in August 2014 under the Second Valls government, where he pushed through business-friendly reforms. He resigned in August 2016 to launch a bid in the 2017 presidential election. After being a member of the Socialist Party from 2006 to 2009, Macron ran in the election under the banner of a centrist political movement he founded in April 2016, En Marche!. He won the election on 7 May 2017 with 66.1% of the vote in the second round.",
	  "scope": 1,
   	"pipeline":0

}

```
### API Resources
  - [POST /api/entity_entity](#post-api/entity_entity)
  - [POST /api/relation_entity](#post-api/relation_entity)
  - [POST /api/all_entities_relations](#post-api/all_entities_relations)
### POST /api/entity_entity
Example: https://secure-spire-37812.herokuapp.com/api/relation_entity

Response body:
```
{
"data": [
    {
        "children": {
            "text": [
                [
                    "France"
                ],
                [
                    "President",
                    "Emmanuel"
                ],
                [
                    "Did",
                    "Macron",
                    "up",
                    "Brexit",
                    "better",
                    "?"
                ]
            ]
        },
        "countries": {
            "index": 1,
            "length": 0,
            "position": 0,
            "type": "countries",
            "value": ""
        },
        "entities": [
            "presidents",
            "countries"
        ],
        "phrase": {
            "text": "Did France  President Emmanuel Macron sum up Brexit better than the British?"
        },
        "presidents": {
            "length": 15,
            "position": 22,
            "type": "presidents",
            "value": "Emmanuel Macron"
        },
        "relation": {
            "POS": [
                "PROPN",
                "PROPN",
                "VERB"
            ],
            "text": [
                "sum"
            ]
        },
        "relation1": {
            "text": [
                "sum"
            ]
        },
        "sentence1": {
            "index": 0,
            "text": "Did France  President Emmanuel Macron sum up Brexit better than the British?"
        },
        "sentence2": {
            "index": 0,
            "text": "Did France  President Emmanuel Macron sum up Brexit better than the British?"
        }
    },
    {
        "children": {
            "text": [
                [
                    "France",
                    "yellow",
                    "vest"
                ],
                [
                    "protests"
                ],
                [
                    "to"
                ],
                [
                    "response"
                ],
                [
                    "debate",
                    "in",
                    "."
                ]
            ]
        },
        "countries": {
            "index": 25,
            "length": 0,
            "position": 0,
            "type": "countries",
            "value": ""
        },
        "entities": [
            "presidents",
            "countries"
        ],
        "phrase": {
            "text": "Emmanuel Macron launches 'grand debate' tour in response to France's yellow vest protests."
        },
        "presidents": {
            "length": 15,
            "position": 0,
            "type": "presidents",
            "value": "Emmanuel Macron"
        },
        "relation": {
            "POS": [
                "NOUN",
                "ADP",
                "NOUN",
                "ADP",
                "NOUN"
            ],
            "text": [
                "protests",
                "response",
                "tour"
            ]
        },
        "relation1": {
            "text": [
                "launches",
                "debate",
                "tour"
            ]
        },
        "sentence1": {
            "index": 1,
            "text": "Emmanuel Macron launches 'grand debate' tour in response to France's yellow vest protests."
        },
        "sentence2": {
            "index": 1,
            "text": "Emmanuel Macron launches 'grand debate' tour in response to France's yellow vest protests."
        }
    }
]
}
```
### POST /api/relation_entity
Example: https://secure-spire-37812.herokuapp.com/api/relation_entity

Response body:
```
    {
    "data": [
        {
            "children": {
                "text": [
                    [
                        "While",
                        "smoking",
                        "still",
                        "by",
                        "cause"
                    ],
                    [
                        "is",
                        "number",
                        "."
                    ]
                ]
            },
            "cures": {
                "index": 8,
                "length": 5,
                "position": 42,
                "type": "cures",
                "value": "cause"
            },
            "drugs": {
                "length": 0,
                "position": 0,
                "type": "drugs",
                "value": ""
            },
            "entities": [
                "drugs",
                "cures"
            ],
            "entity": {
                "index": 1,
                "length": 7,
                "position": 6,
                "sentence": "While smoking is still by far the biggest cause of cancer and cancer deaths, obesity, poor diet and drinking too much alcohol cause an increasing number of cancer cases and deaths.",
                "value": "smoking"
            },
            "phrase": {
                "text": "While smoking is still by far the biggest cause of cancer and cancer deaths, obesity, poor diet and drinking too much alcohol cause an increasing number of cancer cases and deaths."
            },
            "relation": {
                "POS": [
                    "VERB",
                    "VERB"
                ],
                "text": [
                    "is",
                    "cause"
                ]
            },
            "relation1": {
                "text": [
                    "deaths",
                    "of",
                    "cause",
                    "is",
                    "cause"
                ]
            },
            "sentence1": {
                "index": 0,
                "text": "While smoking is still by far the biggest cause of cancer and cancer deaths, obesity, poor diet and drinking too much alcohol cause an increasing number of cancer cases and deaths."
            },
            "sentence2": {
                "index": 0,
                "text": "While smoking is still by far the biggest cause of cancer and cancer deaths, obesity, poor diet and drinking too much alcohol cause an increasing number of cancer cases and deaths."
            }
        },

    ]
}
```
### POST /api/all_entities_relations
Example: https://secure-spire-37812.herokuapp.com/api/all_entities_relations

Request body:
```
[    
    {
    "data": [
        {
            "countries": {
                "index": 1,
                "length": 0,
                "position": 0,
                "type": "countries",
                "value": ""
            },
            "entities": [
                "presidents",
                "countries"
            ],
            "phrase": {
                "text": "Did French President Emmanuel Macron sum up Brexit better than the British?"
            },
            "presidents": {
                "length": 15,
                "position": 21,
                "type": "presidents",
                "value": "Emmanuel Macron"
            },
            "sentence1": {
                "index": 0,
                "text": "Did French President Emmanuel Macron sum up Brexit better than the British?"
            },
            "sentence2": {
                "index": 0,
                "text": "Did French President Emmanuel Macron sum up Brexit better than the British?"
            }
        },
        {
            "actions": {
                "index": 15,
                "length": 8,
                "position": 16,
                "sentence": "Emmanuel Macron launches 'grand debate' tour in response to yellow vest protests.  ",
                "type": "actions",
                "value": "launches"
            },
            "countries": {
                "index": 1,
                "length": 0,
                "position": 0,
                "type": "countries",
                "value": ""
            },
            "entities": [
                "presidents",
                "countries"
            ],
            "phrase": {
                "text": "Did French President Emmanuel Macron sum up Brexit better than the British?Emmanuel Macron launches 'grand debate' tour in response to yellow vest protests.  "
            },
            "presidents": {
                "length": 15,
                "position": 0,
                "type": "presidents",
                "value": "Emmanuel Macron"
            },
            "relation": {
                "value": "actions"
            },
            "sentence1": {
                "index": 1,
                "text": "Emmanuel Macron launches 'grand debate' tour in response to yellow vest protests.  "
            },
            "sentence2": {
                "index": 0,
                "text": "Did French President Emmanuel Macron sum up Brexit better than the British?"
            }
        }
    ]
}
```
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Contributions
Contributions are always welcome!
## Acknowledgments
* Sinequa: https://www.sinequa.com/

<p align="center"><a href="http://heroku.com/"><img
 src="https://miro.medium.com/max/768/1*w2RAR48UbSAYv-6y_V-cdA.png"
border="0"
alt="Heroku powered"
title="Heroku powered"></a></p>

<p align="center"><a href="http://flask.pocoo.org/"><img
    src="https://raw.githubusercontent.com/pallets/flask-website/master/flask_website/static/badges/flask-powered.png"
   border="0"
   alt="Flask powered"
   title="Flask powered"></a></p>
