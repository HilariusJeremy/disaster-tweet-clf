# Disaster-tweet-classifier
Predicts if a tweet is about a real disaster using fine-tuned DistilBERT. Prediction can be done with either streamlit or HTML.

## Description
Data is taken from: https://www.kaggle.com/competitions/nlp-getting-started

My model can be found on: https://huggingface.co/HilariusJeremy/disaster_tweet_distilbert

## Getting Started
**Installing**

- Install the dependencies using pip: `pip install -r requirements.txt`
- Download both `train.csv` and `test.csv` from the kaggle link above 
- Extract them to `data`

**Executing program**

Using streamlit:

- run `python app.py`
- open another terminal and run `streamlit run streamlit_app.py`

Using HTML:

- run `python app.py`
- open `index.HTML` file





