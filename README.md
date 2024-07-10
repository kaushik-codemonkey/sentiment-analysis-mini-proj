# Social Media Sentiment Analysis System

A Mini project that can analyse the sentiment of whatever string that is passed in

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started
Install Redis in your system and start the redis service
from the root of the project do - pip install
Open up a terminal and run - celery -A celery_app.celery worker --loglevel=info 
Open up another terminal and run - python app.py
The app runs on 5001 port
### Routes
```POST /train-model```: Hit this api first to train a model and the system will store the trained model
sample: 
```
curl --location 'http://127.0.0.1:5001/train-model' \
--header 'Content-Type: application/json' \
--data '{
    "modelPath": "sentiment_model.joblib",
    "trainingFile": "social_media_comments.csv"
}'
```

```POST /predict```: Hit this api to get the sentiment of a single stretch of string
sample:
```
curl --location 'http://127.0.0.1:5001/predict' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Bad Clean Air Day"
}'
```
### Dependencies
All project Dependencies are mentioned in requirements.txt
Apart from that Redis has to be installed (System specific steps required)

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

Open up a terminal and run - ```celery -A celery_app.celery worker --loglevel=info ```
Open up another terminal and run - ```python app.py```
The app runs on 5001 port

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
