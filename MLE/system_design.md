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
- Normalization (min-max scaling): This process scales the values so that values are within the range (0,1).
$$z = \frac{x - x_{min}}{x_{max} - x_{min}}$$

- Standardization (Z-score normalization): This process changes the distribution of a feature to have a mean 0 and
standard deviation of 1.
$$z = \frac{x - \mu}{\delta}$$

- Log scaling: This mitigates the skewness of a feature.
$$z = log(x)$$

#### Discretization (Bucketing)
- It is the process of converting a continuous feature into categorical features. For example: instead of representing 
height as a continous feature, we can divide heights into discrete buckets and represent each height by the bucket to 
which it belongs. This allows the model to focus on learning only a few categories instead of attempting to learn an
infinite number of possibilities.

#### Encoding Categorical Features
There are three common methods for converting categorical features into numeric representations:
- **Integer encoding**: An integer value is assigned to each unique category value. For example: Excellent is 1, Good is 2 and
Bad is 3. This is useful if the integer values have a natural relationship with each other. If there is no ordial
relationship between categorical features, integer encoding is not a good choice.  

- **One-hot encoding**: In this technique, a new binary feature is created for each unique value. For example, we replace
the original feature (color) with three new binary features (red, green and blue). Each is replaced with binary 
representation.

- **Embedding learning**: Embedding is a mapping of a categorical feature into an N-dimensional vector. Embedding learning is
the process of learning an N-dimensional vector for each unique value that the categorical feature may take. This approach
is useful when the number of unique values the feature takes is very large. This approach is useful when the number of
unique values the feature takes is very large. In this case one-hot encoding is not a good option because it leads to very
large vector sizes.

#### Things to take into consideration
- **Data availability and data collection**: What are the data sources? What data is available to us and how do we collect it?
How large is the data size? How often do new data come in?
- **Data storage**: Where is the data currently stored? Is it on the cloud or on user devices?  What data format is appropriate
for storing the data? How do we store multimodal dta, eg: a data point that might contain both images and texts?
- **Feature engineering**: All of the above feature related things.
- **Privacy**: How sensitive are the available data? Are users concerned about the privacy of their data? Is anonymization of
user data necessary? Is it possible to store user's data on our servers, or is it only possible to access their data on
their device?
- **Biases**: Are there any biases in the data? If yes, what kinds of biases are present and how do we correct them?

