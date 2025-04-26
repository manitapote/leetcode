### PCA
PCA tries to find new axes (directions) in the data such that each dimension in the compressed data preserves the
maximum variance.

#### Steps of PCA calculation
1) Standardize the data
- Center the data by subtracting the mean of each feature
- Sometimes also scale to unit variance (z-score) but centering is always necessry.
- $$X_{centered} = X - mean(X)$$

2) Compute the Covariance Matrix
- Covariance tells us how feature vary with each other.
$$Cov(X) = \frac{1}_{n - 1} X^{T}_{centered} X_{centered}$$
- If two features are highly correlated => large covariance

3) Compute Eigenvectors and Eigenvalues
- solve the eigenvectors and eigenvalues of the covariance matrix
$$Cov(X)v = \lambda v$$
where v = eigenvector (direction) <br />
$$\lambda =$$ eigenvalue (amount of  variance explained in that direction)

4) Sort the eigenvectors
- Sort eigenvectors by their corresponding eigenvalues, from largest to smalles.
- The top $$k$$ eigenvectors form your principal components.

#### Assumption of PCA
- Linearity: Relationship between variables are linear.
- Large Variance = important: Direction with the highest variance are the most important/informative.
- Mean-centered data: Data is centered around 0 (zero mean).
- No strong outliers: Outliers can heavily distort PCA directions.
- Features are continuous: PCA assumes numerical, continuous variables (not categorical).
- Independent principal components: The new axes (principal components) are orthogonal (uncorrelated).

#### Myths and Reality
- PCA does not assume normality
- PCA is unsupervised.

#### Where does PCA fails?
- When data is non-linear, noisy with high variance, or strongly non-Gaussian.

#### Where does visualization with PCA could lead to misreadings?
- Outlier could disort PCA so the cluster spread out could be because of noise.
- Two clusters are far apart but they could be close in other dimensions.
- High-dimensional spaces have alot more 'room' than 2D or 3D. PCA forces all points into a small flat space. Dense
areas in 2D may not be dense in high dimensions.
- Principal components are just directions maximizing variance. They often don't have easy human interpretation.

#### Ml Research Questions related PCA
1) Concept/Theory Questions
- What is PCA? Explain in simple terms: Unsupervised dimension reduction method 
- **Why does PCA require centering the data?**:
  - PCA finds directions of maximum variance from the origin (zero point).
  - If data is not centered, the mean acts like a bias- PCA may point to the mean, not the true spread of the data.
  - Mathemactically, covariance matrix assumes mean=0
  - Without centering, eigenvectors and variance directions become wrong.

- What assumptions does PCA makes about the data?
  - Linearity, high variance = important structure, mean-centered data, continuous numerical features
  
- What are principal components orthogonal?
  - PCA solves for eigenvectors of the covariance matrix.
  - In linear algebra, eigenvectors of a symmetric matrix (like variance) are always orthogonal.
  - Orthogonality ensures that principal components are uncorrelated and independent directions of variation.
  - It prevents redundancy between components -- each captures unique variance.

- What does high variance mean in PCA?
  - High variance along a direction mean data points are more spread out in that direction.
  - PCA assumes that more spread = more information (not noise).
  - So principal components with high variance capture the essential structure of the data.
  - Low variance directions are likely noise or less important features, and can be discarded during dimensionality
  reduction.

- How do you choose the number of principal components?
  - Plot explained variance ratio using scree plot (elbow curve).
    - Choose the number of components where:
      - Cumulative explained variance >= 90-95%
      - Elbow point: After which adding more components gives diminishing returns
  - Sometimes, use cross-validation on a downstream model to tune dimension.

- What happens if you apply PCA to non-linear data?
  - PCA flattens the data linearly -- so it cannot capture nonlinear structures (eg. swiss roll).
  - Important relationships in data get lost or distorted.
  - Use nonlinear dimensionality reduction methods (t-SNE, UMAP, Kernel PCA).


2) Practical/Application Questions
- When would you not use PCA before applying a machine learning model?
  - When the model is non-linear (eg.decision trees, random forests, XGBoost) - PCA might destroy important feature
  splits.
  - When interpretability is important -- after PCA, features lose real-world meaning.
  - When data is already low-dimensional and clean.
  - When variance does not equal importance (eg. in sparse feature data).
  
- Can PCA be used before logistic regression? Why or Why not?
  - Yes, PCA can reduce dimensionality before logistic regression to prevent overfitting.
  - But, PCA mixes features, so you lose feature interpretability (no direct feature-to-class link).
  - If the goal is pure prediction and variance retention -- PCA+logistic works fine.

- How does PCA impact clustering algorithms like k-means?
  - PCA can help clustering by removing noisy dimensions.
  - Makes clustering faster and often better when high-dimensional noise exists.
  - However, if important cluster structure lies in small-variance directions, PCA may hurt clustering.

- How can PCA help in reducing overfitting?
  - PCA reduces the number of features (dimensions), keeping only the directions that explain most variance.
  - By discarding low-variance (likely noise) dimensions, PCA removes irrelevant patterns that could cause model to
  overfit.
  - Lower-dimensional models are less likely to memorize noise, improving generalization.
  - Particularly useful when the number of features is large compared to the number of samples (curse of dimensionality).

- Why might PCA fail when the features are not continuous or numerical?
  - PCA assumes that features are numeric and continuous because it computes variance and covariance.
  - Categorical variables (eg. red, green, blue) don't have a natural ordering or distance -- covariance doesn't make
  sense.
  - Directly applying PCA to categorical features can produce misleading results.
  - Proper handling: encode categories first (eg. one-hot encoding) or use methods like MCA (Multiple Correspondence
  Analysis) designed for categorical data.
  
- How would you visualize the results of PCA when working with very large feature spaces? 
  - First, reduce dimensions to 2D or 3D by selecting top principal components (PC1, PC2, optionally PC3).
  - Use scatter plots (2D or 3D) colored by labels if available (eg, classes, clusters).
  - Plot explained variance ratio ('scree plot') to show how much information each PC captures.
  - Optionally, biplots: show PCs and how original features load onto them.
  - For very large datasets, sample points for clarity or use density plots (eg. hexbin, contour).
  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
- How does PCA interact with regularization (eg. L1/L2 penalties)?
  - PCA acts as unsupervised feature compression -- it reduces the number of dimensions before modeling. 
  - L1/L2 penalties (used in supervised models like ridge/lasso) apply after model training, penalizing coefficients to
  control complexity.
  - PCA reduces the input complexity first, regularization penalizes model weights afterward.
  - Important: PCA removes feature interpretability, so applying L1 (lasso feature selection) after PCA has no clear
  original feature meaning.
  - Both PCA and regularization reduce overfitting, but in different ways:
    - PCA reduces input dimensions.
    - L1/L2 control model flexibility.

3) Deep/Research-Level Questions
- How would you modify PCA to work for categorical data?
- What are alternative to PCA when data lies on a non-linear manifold?
- How does Kernel PCA differ from standard PCA?

- What are the differences between PCA and Autoencoders for dimensionality reduction?
  - Model type: PCA is a linear algebra-based method (eigen decomposition of covariance matrix). Autoencoder is neural
  network based model that models non-linear relationships.
  - Linearity vs. Non-linearity: PCA finds linear principal components. Autoencoder can capture nonlinear patterns
  through nonlinear activation functions (ReLU, Tanh).
  - Interpretability: Components are linear combinations of original features -- somewhat interpretable. Autoencoder
  latent features are less interpretable (they are learned abstract representations).
  - Training approach: Autoencoder require training and backpropagation.
  - Data Requirements: PCA works well on small-to-medium datasets. Autoencoder needs more data and careful tuning.
  - Reconstruction Quality: PCA is good if underlying structure is linear. Autoencoder is better reconstruction quality
  on nonlinear data because of its flexibility.

4) Advanced PCA Questions
- What are limitations of PCA in supervised learning?
  - PCA is unsupervised -- it does not use label information when finding components.
  - So, PCA does not necessarily preserve class separability -- it maximizes variance, not label information.
  - Applying PCA before supervised model (classification) can sometimes hurt performance, because useful features for
  classification might be low-variance and discarded.
  - Better options: supervised dimensionality reduction methods like linear discriminant analysis (LDA) if preserving
  class separability is important.

- How would you modify PCA to preserve class separability?
   - Use Supervised PCA: modify objective to also consider correlation with labels.
   - Use Linear Discriminant Analysis (LDA):
     - Maximizes between-class variance
     - Minimizes within-class variance
   - Alternatively, use PCA + feature selection: Apply PCA for compression, then supervised feature selection afterward
   keep discriminative components.
   - Newer methods like Deep CCA, Supervised Manifold Learning also exist for complex tasks.

- When should you prefer kernel PCA over standard PCA?
  - Standard PCA finds linear principal components.
  - If data lies on a non-linear manifold (eg. curved, spiraled structure like swiss roll), linear PCA fails.
  - Kernel PCA maps data into a higher-dimensional feature space using a kernel (eg. RBF), then applies PCA there.
  - Kernel PCA captures nonlinear patterns -- suitable for complex datasets where linear spread isn't enough.

- What are alternatives to PCA for non-linear dimensionality reduction?
  - t-SNE, UMAP, Isomap, Autoencoders