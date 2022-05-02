# Data Science Interview Assignment

## Introduction

:clap: If you read this file, you were successful in the behavioural interview. Well done!

The next step to join the Data Science team of [xtream](https://xtreamers.io) is this assignment. 

You will find several datasets: please choose only one of them.
For each dataset, we propose several challenges. You **do not need to
complete all of them**, but rather only the ones you feel comfortable about or that interest you.

:sparkles: Choose what really makes you shine!

:watch: We estimate it should take around 8 hours to solve the challenges for a dataset, and we give you **1 week** to submit a
solution, so that you can do it at your own pace.

:heavy_exclamation_mark:**Important**: you might feel like the tasks are somehow too broad, or the requirements are not
fully elicited. **This is done on purpose**: we wish to let you take your own way in extracting value from data and in developing
your own solutions.

### Deliverables

Please fork this repository and work on it as if you were working on a real-world project assigned to you. A week from
now, we will check out your work and evaluate it.

:heavy_exclamation_mark:**Important**: At the end of this README, you will find a "How to run" section that is not
filled out. Please, write there instructions on how to run your code.

### Evaluation

Your work will be assessed according to several criteria. As an example, these include:

* Method
* Closeness to the data
* Ability to report the results
* Code quality
* Work quality (use of git, dataset management, workflow, tests, ...)
* Documentation

:heavy_exclamation_mark:**Important**: this is not a Kaggle competition, we do not care about model performance.
Do not feel pushed to get the best possible model, focus on showing your method and why you would be able to get there,
given enough time and support.

---   

### Diamonds

**Problem type**: regression

John Doe, a rich but somehow suspect fellow runs a jewelry. Over the years, he has collected data from 5000 diamonds.
The dataset provides physical features of the stones, as well as the value, as estimated by a famous and respected expert.

#### Challenge #1

John wants to know what are the main factors influencing the value of a diamond.
Create a Jupyter notebook to explain what he should look at and why.

#### Challenge #2

Then, John tells you that the expert providing him with the stone valuations disappeared.
He wants you to develop a model to predict the value of a new diamond given its characteristics.
He insists on a point: he wants to know why a stone is given a certain value.
Create a Jupyter notebook to meet John's request.

#### Challenge #3

John likes your model! Now he wants to use it. To improve the model, John is open to hire a new expert and 
let him value more stones.
Create an automatic pipeline capable of training a new instance of your model from the raw dataset. 

#### Challenge #4

Now, John wants to embed your model in a web application, to allow for easy use by his employees.
Develop a REST API to expose the model predictions.

---

### Italian Power Load

**Problem type**: time series forecasting

It is your first day in the office and your first project is about time series forecasting.
You will be given the data for the daily Italian Power Load from 2006 to 2022.
Be careful: 2020 is a very strange year...

#### Challenge #1

Your client asks you for a complete report about the main feature of the power load series.
Create a Jupyter notebook to answer his query.

#### Challenge #2

Then, your first forecasting model.
You are asked to develop a long-term model to predict the power load 1 year ahead.
Disregard 2020, 2021, and 2022: use 2019 as test.

#### Challenge #3

Long-term was great, but what about short term?
Your next task is to create a short-term model to predict the power load 1 day ahead.
Disregard 2020, 2021, and 2022: use 2019 as test.

#### Challenge #4

Finally, production trial.
Pick one of your models and develop and end-to-end pipeline to train and evaluate your models on 2020 and 2021.
Optionally, create a Jupyter notebook to show and comment the results.

---

## How to run
Please fill this section as part of the assignment.