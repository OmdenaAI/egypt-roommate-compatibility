# Concepts

MLflow is organized into four components: Tracking, Projects, Models, and Model Registry. You can use each of these components on their own—for example, maybe you want to export models in MLflow’s model format without using Tracking or Projects—but they are also designed to work well together.

MLflow’s core philosophy is to put as few constraints as possible on your workflow: it is designed to work with any machine learning library, determine most things about your code by convention, and require minimal changes to integrate into an existing codebase. At the same time, MLflow aims to take any codebase written in its format and make it reproducible and reusable by multiple data scientists. On this page, we describe a typical ML workflow and where MLflow fits in.
The Machine Learning Workflow

# Machine Learning Workflow

Machine learning requires experimenting with a wide range of datasets, data preparation steps, and algorithms to build a model that maximizes some target metric. Once you have built a model, you also need to deploy it to a production system, monitor its performance, and continuously retrain it on new data and compare with alternative models.

Main challenges of Machine Learning Workflow:

    It’s difficult to keep track of experiments. 

    It’s difficult to reproduce code. 

    There’s no standard way to package and deploy models. 

    There’s no central store to manage models (their versions and stage transitions). 


MLflow provides four components to help manage the ML workflow:

MLflow Tracking is an API and UI for logging parameters, code versions, metrics, and artifacts when running your machine learning code and for later visualizing the results. 

MLflow Projects are a standard format for packaging reusable data science code. Each project is simply a directory with code or a Git repository, and uses a descriptor file or simply convention to specify its dependencies and how to run the code. For example, projects can contain a conda.yaml file for specifying a Python Conda environment. 

MLflow Models offer a convention for packaging machine learning models in multiple flavors, and a variety of tools to help you deploy them. Each Model is saved as a directory containing arbitrary files and a descriptor file that lists several “flavors” the model can be used in. 

MLflow Registry offers a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production or archiving), and annotations.

#MLflow tracking 

Here's the fluxogram for working with MLflow:

![MLflow Tracking](https://mlflow.org/docs/latest/_images/quickstart_tracking_overview.png)

# How to use

## Installing 

    pip install mlflow

## Tracking a model

Below here we have a simple code for tracking a simple model:

    import mlflow

    from sklearn.model_selection import train_test_split
    from sklearn.datasets import load_diabetes
    from sklearn.ensemble import RandomForestRegressor

    mlflow.autolog()

    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

    # Create and train models.
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # Use the model to make predictions on the test dataset.
    predictions = rf.predict(X_test)

## Using MLflow dashboard

### Run the dashboard

Run on your terminal the following command:

    mlflow ui

### Navigate

Now you can navigate to the dashboard with http://localhost:500.

### Use all the funtions MLflow has

Now you're able to use all the funtionalities MLflow has. You can check the [tutorials](https://mlflow.org/docs/latest/tutorials-and-examples/index.html) from the Official site.



