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
A) **Probability sampling methods**: In this method every member of the population has a chance of being selected. It
is mainly used in quantitative research. If we want to produce results that are representative of the whole population,
probability sampling techniques are the most valid choice.

1) **Simple random sampling**: Every member of the population has an equal chance of being selected. It is conducted by
random number generators or other techniques that are based entirely on chance.

2) **Systematic sampling**: Similar to simple random sampling but it is usually slightly easier to conduct. Every member
of the population is listed with a number and instead of randomly generating numbers, individuals are chosen at regular
intervals. For example: All employees of the company are listed in alphabetical order. From the first 10 numbers, you
randomly select a starting point: number 6. From number 6 onwards, every 10th person on the list is selected (6, 16, 26,
36, and so on), and you end up with a sample of 100 people.
If this technique is used, it is important to make sure that there is no hidden pattern in the list that might skew the
sample.

3) **Stratified sampling**: 

4) **Cluster sampling**

B) Non-probability sampling methods:
1) **Convenience sampling**:
2) **Snowball sampling**:
3) **Stratified sampling**:
4) **Reservoir sampling**:
5) **Importance sampling**:

#### Splitting the data

#### Address any class imbalances