from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

X = pd.DataFrame(projected_df) # Principal component scores as DataFrame

# convert classes into binary array
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(df['class'].values)

# Reshape to a 2D array for OneHotEncoder
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoder = OneHotEncoder(sparse=False)
y_binarized = onehot_encoder.fit_transform(integer_encoded)

# Convert y_binarized back to single labels for all classes
y_single = np.argmax(y_binarized, axis=1)

