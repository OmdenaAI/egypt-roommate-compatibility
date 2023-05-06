Our goal is to create a personality-detecting model that could understand the personalities of people and based on their personalities, help us compare them with other individuals looking for roommates.
There are multiple personality tests available online but we would specifically be working with two personality tests. The first one is our primary dataset.

**OCEAN(Big 5 Personality test)**: This test basically attempts to describe people based on 5 broad factors. The factors are:

**Openness to experience**: High scores reflect the creativity, imagination, and open-mindedness of individuals. Ones with low scores in openness on the other hand are more practical and logical.
**Conscientiousness**: High scores reflect organization, goal-orientedness, disciplined and responsible behaviour of an individual. Lower scores mean that the individual is spontaneous but lower in orderliness.
**Extraversion**: High scores reflect the Individual's inclination towards extraversion, and lower scores signify traits of introversion.
**Agreeableness**: This trait reflects a person's tendency to be compassionate, cooperative, and trusting towards others. Highly agreeable individuals are generally kind, empathetic, and considerate, whereas those low in agreeableness may be more skeptical and competitive.
**Neuroticism**: This trait is associated with emotional stability and the tendency to experience negative emotions such as anxiety, depression, and mood swings. People high in neuroticism may be more prone to stress and exhibit emotional reactivity, while those low in neuroticism tend to be more emotionally resilient and stable.

Based on a questionnaire, the scores for each of these categories are calculated and a final output is given. For this purpose, a public dataset published by open psychometrics, who collected data from more than  1 million people between 2016-2018 by asking them 50 questions. The dataset containing answers of 1,015,342 people can be accessed [here](https://www.kaggle.com/datasets/tunguz/big-five-personality-test). 
This is the primary dataset that we plan to use.

**MBTI (Myers Briggs Type Indicator)**: This is another personality test that is used to check if people are compatible or not. This test classifies people into 16 personality types based on the way they react to the environment. The MBTI gives an individual four letters based on their Introversion/Extroversion, Intuitive decision making/Sensing based on past experiences, Logical/Emotional, and Perceptive (Adaptive) /Judgmental(Rigid) behavior to situations.
We found a [dataset](https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset) where 500-word essays of each of MBTI types are given by 106k people. 

This is our secondary dataset and we would work on this parallelly with the Big Five personality dataset.
