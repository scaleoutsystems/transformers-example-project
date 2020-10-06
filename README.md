# Transformer example project

This STACKn example project demonstrates how to deploy the Swedish BERT model developed by the Swedish Unemployment Agency: https://github.com/af-ai-center/SweBERT.git and publish live prediction endpoints to a STACKn model portal.

***

## BERT and the Swedish BERT models


The realease of the BERT architecture is seen as one of the major breakthroughs in NLP (natural language processing) in the last few years. BERT has presented state of the art results across a number of different use cases, such as document classification, sentiment analysis, natural language inference, questions answering, sentence similarity and more.

Arbetsförmedlingen (The Swedish Public Employment Service) has developed Swedish BERT models which were trained on Swedish Wikipedia with approximately 2 million articles and 300 million words.

## Getting started

On STACKn, create a new project (Projects -> Create project), spin up a new lab session (Labs, choose Image/Default and Flavor/Default -> Submit), open the lab sessionby clicking the link under Ingress. Open a terminal window (+ button, select Terminal). 

Download this repository:

    $ git pull https://github.com/scaleoutsystems/transformers-example-project.git

and then install requirements and Jupyter notebook extension:
    
    $ pip install -r requirements.txt
    $ jupyter nbextension enable --py widgetsnbextension
    
Now you should be ready to open the **getting_started_with_swebert.ipynb** in the **notebooks** folder follow the instructions in there.

## Deploying the model

When the getting started noteb

