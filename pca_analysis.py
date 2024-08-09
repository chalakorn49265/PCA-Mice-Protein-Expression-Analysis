def compute_pca(standardized_df):
    # Sample covariance matrix from the cleaned dataset
    cov_matrix = np.cov(standardized_df.T)
    
    # Eigenvalues and eigenvectors of the sample covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # Plot a histogram of the eigenvalues
    plt.hist(eigenvalues, density=True, bins=100, label='Empirical eigenvalues')
    plt.title('Histogram of Eigenvalues of the Sample Covariance Matrix')
    plt.xlabel('Eigenvalue')
    plt.ylabel('Frequency')
    plt.show()
    
    return eigenvalues, eigenvectors

def find_noise_edge(eigenvalues, standardized_df):
    # Calculate the aspect ratio γ or gamma
    m = standardized_df.shape[1]
    N = standardized_df.shape[0]
    gamma = m / N
    
    # Calculate the upper bound of the Marchenko-Pastur distribution
    lambda_plus = (1 + np.sqrt(gamma))**2
    
    # Identify outlier eigenvalues
    outlier_eigenvalues = eigenvalues[eigenvalues > lambda_plus]
    num_outlier_eigenvalues = len(outlier_eigenvalues)
    
    print(f"Number of outlier eigenvalues: {num_outlier_eigenvalues}")
    print(f"Outlier eigenvalues: {outlier_eigenvalues}")
    
    return outlier_eigenvalues, lambda_plus

def perform_pca_and_plot(standardized_df, outlier_eigenvalues, noise_edge):
    pca = PCA(n_components=standardized_df.shape[1])
    pca.fit(standardized_df)
    
    eigenvalues = pca.explained_variance_
    outlier_indices = np.where(eigenvalues > noise_edge)[0]
    principal_components = pca.components_[outlier_indices, :]
    
    print(f"Number of significant principal components: {len(principal_components)}")
    
    # Project the data onto two principal components for visualization
    pc1, pc2 = principal_components[0:2]
    projected_data = np.dot(standardized_df, np.array([pc1, pc2]).T)
    
    projected_df = pd.DataFrame(projected_data, columns=['PC1', 'PC2'])
    
    return projected_df

def plot_principal_components(projected_df, labels):
    projected_df['class'] = labels.values
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PC1', y='PC2', hue='class', data=projected_df, palette='viridis')
    plt.title('Projection onto the first two principal components with class hue')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True)
    plt.legend(title='Class', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()
