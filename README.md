# xtream AI Challenge

## Ready Player 1? 🚀

Hey there! If you're reading this, you've already aced our first screening. Awesome job! 👏👏👏

Welcome to the next level of your journey towards the [xtream](https://xtreamers.io) AI squad. Here's your cool new assignment.

Among the datasets described below, pick **just one** that catches your eye. Each dataset comes with its own set of challenges. Don't stress about doing them all. Just dive into the ones that spark your interest or that you feel confident about. Let your talents shine bright! ✨

Take your time – you've got **10 days** to show us your magic, starting from when you get this. No rush, work at your pace. If you need more time, just let us know. We're here to help you succeed. 🤝

### What You Need to Do

Think of this as a real-world project. Fork this repo and treat it as if you're working on something big! When the deadline hits, we'll be excited to check out your work. No need to tell us you're done – we'll know. 😎

🚨 **Heads Up**: You might think the tasks are a bit open-ended or the instructions aren't super detailed. That’s intentional! We want to see how you creatively make the most out of the data and craft your own effective solutions.

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

---

### Diamonds

**Problem type**: Regression

**Dataset description**: [Diamonds Readme](./datasets/diamonds/README.md)

Meet Don Francesco, the mystery-shrouded, fabulously wealthy owner of a jewelry empire. 

He's got an impressive collection of 5000 diamonds and a temperament to match - so let's keep him smiling, shall we? 
In our dataset, you'll find all the glittery details of these gems, from size to sparkle, along with their values 
appraised by an expert. You can assume that the expert's valuations are in line with the real market value of the stones.

#### Challenge 1

Francesco wonders: **what makes a diamond valuable?** You should provide him with an answer.

Don Francesco has been very clear with you: he is not a fan of tech jargon, so keep your message plain and simple. 
However, he trusts no one - certainly not you. He's hired Luca, another data scientist, to double-check your findings (no pressure!). 
Your mission is simple. 

Create a Jupyter notebook to explain what Francesco should look at and why.
Your code should be understandable by a data scientist like Luca, but your text and visualizations should be clear for a layman like Francesco.

#### Challenge 2

Plot twist! The expert who priced these gems has now vanished. 
Francesco needs you to be the new diamond evaluator. 
He's looking for a **model that predicts a gem's worth based on its characteristics**. 
And, because Francesco's clientele is as demanding as he is, he wants the why behind every price tag. 

Create another Jupyter notebook where you develop and evaluate your model.

#### Challenge 3

Good news! Francesco is impressed with the performance of your model. 
Now, he's ready to hire a new expert and expand his diamond database. 

**Develop an automated pipeline** that trains your model with fresh data, 
keeping it as sharp as the diamonds it assesses.

#### Challenge 4

Finally, Francesco wants to bring your brilliance to his business's fingertips. 

**Build a REST API** to integrate your model into a web app, 
making it a cinch for his team to use. 
Keep it developer-friendly – after all, not everyone speaks 'data scientist'!

So, ready to add some sparkle to this challenge? Let's make these diamonds shine! 🌟💎✨

---

### Italian Power Load

**Problem type**: time series forecasting

**Dataset description**: [Power Load readme](./datasets/italian-power-load/README.md)

Welcome to your first day at the office, and what a charged-up project you have! 
Your client is Zap Inc, a fictional power player in Italy. 
They're handing you data on Italy's power load from 2006 to 2022. 
Marta, your wise colleague, has a piece of advice for you: be careful with 2020, it was a very peculiar year.

#### Challenge 1

Zap Inc asks you for a complete report about the main feature of the power load series.
The report should be understandable by a layman, but it should also provide enough details to be useful for a data scientist.
**Create a Jupyter Notebook that sheds light on the main characteristics of the power load data.** 
Make it clear, make it insightful!

#### Challenge 2

Now, it's time to **predict the future**, well, at least a year into it. 
Develop a long-term forecasting model for the power load with a forecasting horizon of one year ahead, but let's skip 2020-2022 and use 2019 as your testing ground. 
Marta's advice: Zap's bosses aren't AI gurus, so your model's accuracy and explainability need to be crystal clear. 
Illuminate these points with a second notebook.

#### Challenge 3

After mastering the long-term, it's time to zoom in. 
Your next challenge is to **predict the power load one day ahead**. 
Again, sideline 2020-2022 and focus on 2019 for testing. 
Keep Marta's wisdom in mind – clarity is key!

#### Challenge 4

Choose one of your sparkling models and get it ready for the big leagues. 
Develop an **end-to-end pipeline for training and evaluating your model** on 2020 and 2021 data. 
Luca, the new CTO at Zap and a self-confessed nerd, demands code that's as clean and structured as it is maintainable. 
Impress him!

#### Challenge 5

2020 was a tough year for everyone, including your model. 
Zap Inc isn't thrilled with its performance. 
**Justify your model's performance in 2020** with a detailed notebook. 
Explain the unexpected, defend your approach, and remember, every challenge is a learning curve!

Ready to electrify your career with this project? Let's power through! ⚡🔌📈

---

### Employee Churn

**Problem type**: classification

**Dataset description**: [Employee churn readme](./datasets/employee-churn/README.md)

Your first client is Pear Inc, a multinational company worried about its poor talent retention.
Pear has a peculiar hiring strategy. They offer free classes and hire the best students.
The strategy is working, but many new hires leave the company after a few months. This is a huge waste of time and money.

In the past few months, they collected a dataset with information about their employees and recorded whether they 
churned or not. Due to the churning period being so short, they are confident that the history of each candidate
is enough to predict the churn and the experience is Pear is not relevant.

Gabriele, the Head of Talent, is counting on you to put a plug in this problem. 
And Fabio, an ML Engineer and new colleague of yours, will be eyeing your work too!

#### Challenge 1

Pear Inc needs your help to figure out **what makes an employee stick versus split**. 
Craft a Jupyter notebook to answer their question. 
Keep it simple enough for Gabriele but detailed enough to dazzle Fabio.

#### Challenge 2

Next up, Pear Inc needs a crystal ball to foresee who will staty with them. 
**Develop a model that predicts employee churn**, complete with churn probabilities to help Gabriele take timely action.
Remember, Gabriele's no fan of black-box machines, and Fabio's looking for proof that your model's magic works.

#### Challenge 3

Your model's a hit, but why does it work wonders? 
Time to add some transparency to your tech.
**Make your model interpretable**, showcasing the key features and how each prediction is made. 
Your audience: both Gabriele and Fabio, so balance simplicity with sophistication.

#### Challenge 4

Now, let's get your model production-ready. 
**Build an end-to-end pipeline for training your model with new data sets.** 
Assume the data structure stays the same, and keep your code clean and classy to impress Fabio, a clean code lover.

#### Challenge 5

Bravo! Pear Inc loves your work, and now it's showtime for your model in their web app. 
**Develop a REST API** to expose your model's predictions. 
This time, it's all about Fabio - ensure your code is clean, structured, and ready for evolution.

So, ready to tackle Pear Inc's perplexing problem and turn the tide on talent turnover? 
Let's get cracking! 🍐💼🔍

---

## How to run
Please fill this section as part of the assignment.