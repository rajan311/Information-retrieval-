import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the CSV file
df = pd.read_csv(r"C:\IR TYCS\dataset.csv")

# Combine the 'covid' and 'fever' columns to create input data
data = df["covid"] + "" + df["fever"]
X = data.astype(str)  # Test data
y = df['flu']  # Labels

# Splitting the data into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Converting data into bag-of-words format to train the model
vectorizer = CountVectorizer()

# Initializing the converter
X_train_counts = vectorizer.fit_transform(X_train)

# Converting the training data
X_test_counts = vectorizer.transform(X_test)

# Using and training the multinomial model of naive Bayes algorithm
classifier = MultinomialNB()  # Initializing the classifier
classifier.fit(X_train_counts, y_train)  # Training the classifier

# Loading another dataset to test if the model is working properly
data1 = pd.read_csv(r"C:\IR TYCS\test.csv")

# Combine the 'covid' and 'fever' columns for new data
new_data = data1["covid"] + "" + data1["fever"]
new_data_counts = vectorizer.transform(new_data.astype(str))  # Converting the new data

# Making the model predict the results for the new dataset
predictions = classifier.predict(new_data_counts)

# Output the results
print(predictions)

# Retrieving the accuracy and classification report
accuracy = accuracy_score(y_test, classifier.predict(X_test_counts))
print(f"\nAccuracy: {accuracy:.2f}")
print("Classification Report: ")
print(classification_report(y_test, classifier.predict(X_test_counts)))

# Convert the predictions to a DataFrame
predictions_df = pd.DataFrame(predictions, columns=['flu_prediction'])

# Concatenate the original DataFrame with the predictions DataFrame
data1 = pd.concat([data1, predictions_df], axis=1)

# Write the DataFrame back to CSV
data1.to_csv(r"C:\IR TYCS\test1.csv", index=False)
