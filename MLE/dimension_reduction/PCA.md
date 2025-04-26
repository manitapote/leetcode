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
- What are principal components orthogonal?
- What does high variance mean in PCA?

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
- Why might PCA fail when the features are not continuous or numerical?
- How would you visualize the results of PCA when working with very large feature spaces?
- How does PCA interact with regularization (eg. L1/L2 penalties)?

3) Deep/Research-Level Questions
- How would you modify PCA to work for categorical data?
- What are alternative to PCA when data lies on a non-linear manifold?
- How does Kernel PCA differ from standard PCA?
- What are the differences between PCA and Autoencoders for dimensionality reduction?