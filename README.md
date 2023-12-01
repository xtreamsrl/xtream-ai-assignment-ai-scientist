# xtream AI Challenge

## Ready Player 1? 🚀

Hey there! If you're reading this, you've already aced our first screening. Awesome job! 👏👏👏

Welcome to the next level of your journey towards the [xtream](https://xtreamers.io) AI squad. Here's your cool new assignment.

Among the datasets described below, pick **just one** that catches your eye. Each dataset comes with its own set of challenges. Don't stress about doing them all. Just dive into the ones that spark your interest or that you feel confident about. Let your talents shine bright! ✨

Take your time – you've got **10 days** to show us your magic, starting from when you get this. No rush, work at your pace. If you need more time, just let us know. We're here to help you succeed. 🤝

🚨 **Heads Up**: You might think the tasks are a bit open-ended or the instructions aren't super detailed. That’s intentional! We want to see how you creatively make the most out of the data and craft your own effective solutions.

### What You Need to Do

Think of this as a real-world project. Fork this repo and treat it as if you're working on something big! When the deadline hits, we'll be excited to check out your work. No need to tell us you're done – we'll know. 😎

🚨 **Remember**: At the end of this doc, there's a "How to run" section left blank just for you. Please fill it in with instructions on how to run your code – it's important!

### How We'll Evaluate Your Work

We'll be looking at a bunch of things to see how awesome your work is, like:

* Your approach and method
* How well you get the business problem
* Your understanding of the data
* The clarity and completeness of your findings
* How you use your tools (like git and Python packages)
* The neatness of your code
* The clarity of your documentation

🚨 **Keep This in Mind**: This isn't about building the fanciest model: we're more interested in your process and thinking.

## Special Note for Interns

If you're aiming for an internship, focus **only on Challenges 1 and 2** for the dataset you choose.

We'll mainly look at:

* Your workflow
* How well you understand the problem and data
* The approach to the analysis and clarity of your conclusions
* How neat your code is (relative to your experience level)

This is your chance to showcase your unique approach and thought process. Don't worry if your code isn't perfect or your model isn't top-notch yet. We've been in your shoes and are here to help you grow. 🌟

---

### Diamonds

**Problem type**: regression

**Dataset description**: [Diamonds readme](./datasets/diamonds/README.md)

Don Francesco runs a jewelry. He is a very rich fellow, but his past is shady: be sure not to make him angry.
Over the years, he collected data from 5000 diamonds.
The dataset provides physical features of the stones, as well as their value, as estimated by a respected expert.

#### Challenge 1

**Francesco wants to know which factors influence the value of a diamond**: he is not an AI expert, 
he wants simple and clear messages.
However, he trusts no one - and, for sure, he does not trust you: so, he hired another data scientist 
to get a second opinion on your work.
Create a Jupyter notebook to explain what Francesco should look at and why.
Your code should be understandable by a data scientist, but your text should be clear for a layman.

#### Challenge 2

Then, Francesco tells you that the expert providing him with the stone valuations disappeared.
**He wants you to develop a model to predict the value of a new diamond given its characteristics**.
He insists on a point: his customer are not easy-going, so he wants to know why a stone is given a certain value.
Create a Jupyter notebook to meet Francesco's request.

#### Challenge 3

Francesco likes your model! Now he wants to use it. To improve the model, Francesco is open to hire a new expert and 
let him value more stones.
**Create an automatic pipeline capable of training a new instance of your model from the raw dataset**. 

#### Challenge 4

Finally, Francesco wants to embed your model in a web application, to allow for easy use by his employees.
**Develop a REST API to expose the model predictions**.

---

### Italian Power Load

**Problem type**: time series forecasting

**Dataset description**: [Power Load readme](./datasets/italian-power-load/README.md)

It is your first day in the office and your first project is about time series forecasting.
Your customer is Zap Inc, an imaginary Italian utility: they will provide you with the daily Italian Power Load from 2006 to 2022.
Marta, a colleague of yours, provides you with a wise piece of advice: be careful about 2020, it was a very strange year...

#### Challenge 1

Zap Inc asks you for a complete report about the main feature of the power load series.
The report should be understandable by a layman, but it should also provide enough details to be useful for a data scientist.
**Create a Jupyter notebook to answer their query.**

#### Challenge 2

Then, your first forecasting model.
**You are asked to develop a long-term model to predict the power load 1 year ahead.**
Disregard 2020, 2021, and 2022: use 2019 as test.
Another piece of advice from your colleague Marta.
The managers at Zap Inc are not AI experts, so they want to know how accurate your model is and why they should trust it.
Be sure to answer their concerns in your notebook.

#### Challenge 3

Long-term was great, but what about short term?
**Your next task is to create a short-term model to predict the power load 1 day ahead.**
Disregard 2020, 2021, and 2022: use 2019 as test.
Keep im mind Marta's advice from the previous challenge! 

#### Challenge 4

Finally, production trial.
**Pick one of your models and develop and end-to-end pipeline to train and evaluate it on 2020 and 2021.**
Again, your good friend Marta has some suggestion for you. It looks like Luca, the new CTO at Zap, is a bit of a nerd.
And he wants all the production code to be clean, well-structured, and easily maintanable.
You'd better not to disappoint him!

#### Challenge 5

Zap Inc is not impressed by the performance of your model in 2020. You should defend your results.
**Create a notebook to comment and explain the performance of your model in 2020.**

---

### Employee Churn

**Problem type**: classification

**Dataset description**: [Employee churn readme](./datasets/employee-churn/README.md)

You have just been contracted by Pear Inc, a multinational company worried about its poor talent retention.
In the past few months, they collected data about their new employees. All of them come from classes 
the company is sponsoring, yet many enter Pear just to leave a few months later.
This is a huge waste of time and money.

The HR department of the company wants you to understand what is going on and to prevent further bleeding.

The main sponsor of the project is Gabriele, Head of Talent at Pear.

#### Challenge 1

Pear Inc wants you to understand what are the main traits separating the loyal employees from the others.
**Create a Jupyter notebook to answer their query.**
Gabriele is not an AI expert, so be sure to explain your results in a clear and simple way.
However, you are also told that Fabio, an ML Engineer, will review your work: be sure to provide enough details to be useful for him.

#### Challenge 2

Then, a predicting model.
**You are asked to create a model to predict whether a new employee would churn**.
Gabriele tells you that he would like to know the probability of churn for each employee, so that he could take 
corrective actions.
Fabio has now joined Pear, and has some advice for you: Gabriele does not believe in black-box models, so
be sure to provide him with compelling evidence that your model works.

#### Challenge 3

Wow, the model works great, but why does it? 
**Try and make the model interpretable**, by highlighting the most important features and how each prediction is made.
You'll need to explain your work to both Gabriele and Fabio, so be sure to include clear and simple text, 
but feel free to use advanced techniques, if you feel that it is necessary.

#### Challenge 4

Now, production trial. 
**Develop and end-to-end pipeline to train a model given a new dataset.**
You can assume that the new dataset has exactly the same structure as the provided one: 
possible structural changes will be managed by your fellow data engineers.
Fabio is a clean code lover: make sure not to disappoint him!

#### Challenge 5

Finally, Pear Inc is happy with your results!
Now they want to embed your model in a web application. 
**Develop a REST API to expose the model predictions**.
Again, this is no longer about Gabriele, but Fabio will review and evolve your work.
Be sure to provide him with clean and well-structured code.

---

## How to run
Please fill this section as part of the assignment.