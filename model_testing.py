import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

# Load the trained model
model = pickle.load(open('trained_model.pkl', 'rb'))

# Load the test data
test_data = pd.read_csv('test/test_characters.csv')

# Extract the features and labels from the test data
X_test = test_data[['Strength', 'Agility', 'Magic', 'Vitality']]
y_test = test_data['Class']

# Preprocess the features using the saved scaler from the preprocessing step
scaler = pickle.load(open('preprocessed_data.pkl', 'rb'))['scaler']
X_test_scaled = scaler.transform(X_test)

# Predict the labels for the test data
y_pred = model.predict(X_test_scaled)

# Calculate the accuracy of the model on the test data
test_accuracy = accuracy_score(y_test, y_pred)

print(f"Test Accuracy: {test_accuracy}")
