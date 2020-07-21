## Introduction 👩‍💻
In this scenario, you will deploy [Seldon Core](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/) to a Kubernetes environment. 

You will then use Seldon Core to deploy and test a machine learning classifier- pre-trained on the Scikit-Learn [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

## Pre-requisites ☁
An understanding of [Kubernetes](https://kubernetes.io/) terminology and concepts will be helpful! 

## What is Seldon Core? 🤖

Seldon Core is an open source platform to deploy your machine learning models at scale on Kubernetes.  

Seldon Core makes it simple to convert machine learning models into production-grade microservices following three steps:
1. **Containerise**: Model binaries from popular frameworks (Scikit-Learn, Tensorflow, XGBoost) are readily containerised thanks to pre-built model servers. 
Custom models are supported using language wrappers (Python, Java) allowing you to take any model in these languages and containerise them. 
2. **Deploy**: Seldon Core extends Kubernetes by adding the custom `SeldonDeployment` resource. Seldon deployments support a range of complex inference patterns, such as canary rollouts and multi-armed bandits. Seldon deployments are built out of a number of core components e.g. Transformers, Predictors, Explainers, Routers, etc.
3. **Monitor**: Logging can easily be configured to support [tracing of network traffic to deployments](https://docs.seldon.io/projects/seldon-core/en/latest/graph/distributed-tracing.html), [monitoring of request/response payloads](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/logging.html), [visualisation of real time model health](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/analytics.html). Alerting for [outlier detection](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/outlier_detection.html) and [concept drift](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/drift_detection.html) can be setup. 

![](seldon-core/assets/seldon_core_overview.png)

✍️ Tutorial authored by Tom Farrand. Source [here](https://github.com/FarrandTom/katacoda-scenarios/tree/master/seldon-core).