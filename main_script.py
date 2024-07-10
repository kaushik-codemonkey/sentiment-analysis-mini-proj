# main_script.py

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load your dataset
df = pd.read_csv('data/social_media_comments.csv', encoding='latin-1', header=None, names=['sentiment', 'id', 'date', 'query', 'user', 'text'])
# df['sentiment'] = df['sentiment'].map({'0': 'negative', '4': 'positive'})
df['sentiment'] = df['sentiment']


# Display the first few rows of the dataset
print(df.head())

# Define a function to preprocess text
def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# Apply preprocessing to each comment
df['processed_text'] = df['text'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['processed_text'], df['sentiment'], test_size=0.2, random_state=42)

# Create a pipeline with CountVectorizer and MultinomialNB
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Predict the sentiment of the test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print classification report
print(classification_report(y_test, y_pred))

# Function to predict sentiment of a given text
def predict_sentiment(text):
    processed_text = preprocess_text(text)
    return model.predict([processed_text])[0]

# Example usage
new_comment = "I absolutely love this product! It's amazing."
print(f"Predicted Sentiment: {predict_sentiment(new_comment)}")
