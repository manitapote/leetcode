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
[Source](https://www.scribbr.com/methodology/sampling-methods/) <br />
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

3) **Stratified sampling**: Stratified sampling divides the population into subpopulation that differ in important ways.
It makes sure that every subgroup is properly represented in the sample. To use this sampling method, we divide the
population into subgroups (called strata) based on the relevant characteristics (e.g. gender identity, age, range,
income bracket, job role). Based on the proportions, we calculate how many people should be sampled from each subgroup.
<br />
For example: If there are 800 female and 200 male employees, a sample of 100 people would include 80 women and 20 men. 


4) **Cluster sampling**: It divides the population into subgroups, but each subgroup should have similar characteristics
to the whole sample. Instead of sampling individuals from each subgroup, we randomly select entire subgroups. If
practical, all the individual from each sampled cluster are included. If clusters are large, we can sample individuals
from within each cluster using one of the techniques above. This is also called multi-stage sampling.

This method is good for dealing with large and dispersed populations. <br />
Example: The company has offices in 10 cities across the country. If it is not possible to travel to each office to
collect data, so you randomly sample 3 offices and these offices are the clusters.

<br />
**Note**: This sounds more like a tree structure. We want to decide which level we want to consider for aggregation.
<br />

B) **Non-probability sampling methods**: Individuals are selected based on non-random criteria, and not every individual
has a chance of being included.
This type of sampling is easier and cheaper to access but have higher risk of sampling bias. The inferences we make
about the population are weaker than with probability samples, and conclusions may be more limited.
<br />
Non-probability sampling techniques are often used in exploratory and quantitative research. In these types of research,
the aim is not to test a hypothesis about a broad population but to develop an initial understanding of small or
under-researched population.

1) **Convenience sampling**: Easy and inexpensive way to gather initial data. The individuals can be anyone available to
the researcher. The sample might not be representative of the population so the results might not be generalizable.
This sampling process is at risk for both **sampling bias** and **selection bias**.
<br />
2) **Snowball sampling**:
4) **Reservoir sampling**:
5) **Importance sampling**:

#### Splitting the data

#### Address any class imbalances