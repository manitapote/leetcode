## Model Training
- Constructing the dataset
- Choosing the loss function
- Training from scratch vs. fine-tunning
- Distributed training

### Constructing the dataset
1) Collect the raw data
2) Identify features and labels
3) Select a sampling strategy
4) Split the data
5) Address class imbalance (if any)


#### Identify labels
1) **Hand labeling**: This means individual annotators labels the data by hand. For example:
an individual annotator labels whether the post contains misinforamtion or not. Hand labeling leads to
accurate labels since a human is involved in the process. However, it is expensive and slow, introduces bias,
requires domain knowledge, and is threat to data privacy.
2) **Natural labeling**: Ground truth labels are inferred automatically without human annotation.

#### Sampling Strategy
A) Probability sampling methods
1) **Simple random sampling**
2) **Sytematic sampling**
3) **Stratified sampling**
4) **Cluster sampling**

B) Non-probability sampling methods:
1) **Convenience sampling**:
2) **Snowball sampling**:
3) **Stratified sampling**:
4) **Reservoir sampling**:
5) **Importance sampling**:

#### Splitting the data

#### Address any class imbalances