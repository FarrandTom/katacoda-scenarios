# Introduction

In this tutorial you will learn how to wrap a Dataiku generated model artefact into a high performance Seldon inference server.

## Description

Seldon provides [reusable pre-built servers](https://docs.seldon.io/projects/seldon-core/en/stable/nav/config/servers.html) for popular machine learning frameworks (Scikit-learn, XGBoost, Tensorflow, MLFlow, Triton) which only need a saved model artefact to get going with.

On top of this Seldon provides the tools to create your own custom reusable container images for high performance machine learning serving.

This tutorial walks you through this process, focusing on a pre-trained Dataiku model artefact. Developing your own reusable model servers reduces engineering effort drastically, by allowing you to skip the container build stage in the future and simply supply the saved model artefact!

## Workflow

This tutorial will follow the below workflow:

1. **Understanding the Python Code:** You will get to grips with the Python code which will be used to load the model and handle requests when deployed.
2. **Adding Requirements:** Defining the Python dependencies needed to run the model.
3. **Testing Locally:** Ensuring that the code of your deployment so far is correct before building the Docker image.
4. **Creating Your Dockerfile:** Specifying how you would like the Docker image to be built.
5. **Building Your Model Image:** Creating the Docker image.
6. **Deploying Onto Seldon:** Pushing your model server onto the Seldon platform to serve requests.

Time to get cracking!
