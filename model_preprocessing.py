import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load the character data from the CSV file
data = pd.read_csv('train/train_characters.csv')

# Separate the features and target variable
X = data[['Strength', 'Agility', 'Magic', 'Vitality']]
y = data['Class']

# Encode the target variable
#label_encoder = LabelEncoder()
# y_encoded = label_encoder.fit_transform(y)

# Perform feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Save the preprocessed data
preprocessed_data = {
    'X_train': X_train,
    'X_val': X_val,
    'y_train': y_train,
    'y_val': y_val,
    # 'label_encoder': label_encoder,
    'scaler': scaler
}

# Save the preprocessed data to a file
filename = 'preprocessed_data.pkl'
pd.to_pickle(preprocessed_data, filename)

print(f"Preprocessed data saved to {filename}")
