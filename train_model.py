import pandas as pd
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump
from sklearn import datasets, linear_model
from celery_app import celery

nltk.download('punkt')
nltk.download('stopwords')

# Define a function to preprocess text
def preprocess_text(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

@celery.task
def train_model(model_path='sentiment_model.joblib', training_file='social_media_comments.csv'):
    # Load the Sentiment140 dataset
    df = pd.read_csv("data/"+training_file, encoding='latin-1', header=None, names=['sentiment', 'id', 'date', 'query', 'user', 'text'])

    # Map sentiment values to positive and negative labels
    df['sentiment'] = pd.to_numeric(df['sentiment'], errors='coerce')

    # Apply preprocessing to each comment
    df['processed_text'] = df['text'].apply(preprocess_text)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['processed_text'], df['sentiment'], test_size=0.2, random_state=42)

    # Create a pipeline with CountVectorizer and MultinomialNB
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # fit a linear regression model
    model.fit(X_train, y_train)

    # Save the trained model to disk
    dump(model, model_path)

    print("Model trained and saved to {model_path}")
