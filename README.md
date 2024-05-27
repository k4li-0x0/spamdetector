# Spam detector
## How to install project
 - install pipenv: `pip3 install pipenv`
 - install dependencies: `pipenv install`
 - run virtual environment shell `pipenv shell`
## How to use scrapper
 - Copy .env.example and name it .env
 - Enter your API credentials
 - `python spamdetector/scrapper.py`
 - Profit!
## How to label dataset
 - `python spamdetector/datasetweb.py`
## How to train model
 - `python spamdetector/model/bayes.py`
 - `python spamdetector/model/svc.py`
## How to run model on local machine:
 - `python spamdetector/model/util.py`