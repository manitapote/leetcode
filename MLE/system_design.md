####  Unsupervised Algorithms
- Clustering
- Association
- Dimensionality reduction

#### Reinforcement learning
- A computer agent learns to perform a task through repeated trial-and-error interactions with the environment. 

#### Data Storage
- SQL: MySQL, PostgreSQL
- NoSQL: key/value (Redis, DynamoDB)
- Column-based: Cassandra, HBase
- Graph: Neo4J
- Document: MongoDB, CouchDB

#### Datat Types in ML
- Structured: Numerical (Discrete and Continuous), Categorical (Ordian, Nominal)
- Unstructured: Audio, Video, Image, Text

#### Structured
- Best with Decision trees, linear models, SVM, Naive Bayes and KNN

#### Unstructured
- Best with Deep Learning Models

#### Feature Engineering Operations
1) Handling missing values
This can be handled in two ways: deletion or imputation 
a) Deletion: This method removes any records with missing value in any of the features either row wise or colum nwise. 
In column deletion, we remove the whole column representing feature, if the feature has too many missing values. In 
row deletion, we remove a row representing a data point if the data point has many missing values. 
The drawback of deletion is that it decrease the data quantity. This case is not ideal.

2) Imputation: We can impute the missing values by filling them with certain values. Some common practices are:
- Filling in missing values with their defaults
- Filling in missing values with the mean, median or mode.
- The drawback of imputation is that it introduces noise to the data.

#### Feature Scaling
- Normalization (min-max scaling):
$$z = \frac{x - x_{min}}{x_{max} - x_{min}}$$

- Standardization (Z-score normalization): 
$$z = \frac{x - \mu}{\delta}$$