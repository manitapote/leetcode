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
