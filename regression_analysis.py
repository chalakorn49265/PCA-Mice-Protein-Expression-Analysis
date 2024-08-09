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

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_single, test_size=0.3, random_state=42)

# We will use Lasso with l1 regularization
model = LogisticRegression(penalty='l1', solver='liblinear', multi_class='ovr')

# Fit the model with training data
model.fit(X_train, y_train)

# Compute the predicted data
y_pred = model.predict(X_test)

# Compare predicted data with actual data
print(classification_report(y_test, y_pred))

# Print the coefficients
print("Coefficients of the model:")
print(model.coef_)

def main():
    # Define coefficients for each class
    coefficients = {
        'c-CS-s': [0.05697969, 0.20509097, 0.20710991, 0.11754858, 0.0297423, 0.31858742, -0.79201464, -0.2850825, -0.44987017],
        'c-CS-m': [-0.0026826, 0.6448493, 0.49195695, -0.03053657, 0.62553842, 0.02633092, -1.08748998, -0.50683028, 0.37458434],
        'c-SC-s': [-0.49476283, -1.40850497, -0.29881774, 0.39769263, -1.3629923, -0.57528856, -0.57986001, 0, 1.23452592],
        'c-SC-m': [-0.07224931, -0.53524878, -0.68946469, 0.42892331, -0.2020770, 0, 0.21532781, -0.64269204, -1.11534066],
        't-CS-s': [-0.23462099, 0.34857209, 0.12947203, -0.21767423, -0.39473808, 0.00224123, -0.1361875, 0.15847362, 0.35486583],
        't-CS-m': [-0.21109091, 1.02289601, 0.08827354, -0.8991831, 0.73025996, 0, 0.55904586, -1.15378426, -0.64323752],
        't-SC-s': [0.37350931, -0.70226272, -0.23808578, 0.30074136, -0.24444927, 0.19017583, 0.95576603, 0.65065805, 0.08605293],
        't-SC-m': [-0.05665128, -0.57119043, -0.26731696, -0.68917772, -0.029377, -1.61011674, -0.27762764, -0.41775609, -0.38541348],
    }

# Define variable names corresponding to the coefficients
variables = ['MEK_N', 'EGR1_N', 'PSD95_N', 'pPKCG_N', 'GFAP_N', 'pP70S6_N', 'Tau_N', 'DYRK1A_N', 'GluR4_N']

# Create scatter plot for each class
plt.figure(figsize=(15, 10))

for i, (class_name, coeffs) in enumerate(coefficients.items()):
    plt.subplot(3, 3, i+1)
    x_positions = np.arange(len(variables))
    plt.scatter(x_positions, coeffs, label=class_name)
    plt.plot(x_positions, coeffs)
    plt.title(f'{class_name}')
    plt.xticks(x_positions, variables, rotation=45)
    plt.xlabel('Variables')
    plt.ylabel('Coefficient Value')
    plt.grid(True)
    plt.tight_layout()
plt.show()
