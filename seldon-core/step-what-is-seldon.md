# What is Seldon Core?

Seldon Core is an open source platform to deploy your machine learning models at scale on Kubernetes. 

Seldon Core makes it simple to convert machine learning models into production-grade microservices following three steps:
1. *Containerise*: Model binaries from popular frameworks (Scikit-Learn, Tensorflow, XGBoost) are readily containerised thanks to pre-built model servers. 
Custom models are supported using language wrappers (Python, Java) allowing you to take any model in these languages and containerise them. 
2. *Deploy*: Seldon Core extends Kubernetes by adding the custom `SeldonDeployment` resource. SeldonDeployments support a range of complex inference patterns, such as canary rollouts and multi-armed bandits. 
![](seldon-core/assets/seldon_core_overview.png)
SeldonDeployments are built out of a number of core components:
- Transformers: Pre-processors to ensure raw data is correctly wrangled before handing off to the predictor and post-processors to return user-friendly results.
- Predictors: The pod which will contain the machine learning models that you are deploying. 
- Explainers: Use [Seldon Alibi](https://docs.seldon.io/projects/alibi/en/stable/index.html) to provide explainations of algorithmic decisions. 
- Routers: Define how network traffic will be routed within your SeldonDeployment.
- etc... 
3. *Monitor*: Logging can easily be configured to support [tracing of network traffic to deployments](https://docs.seldon.io/projects/seldon-core/en/latest/graph/distributed-tracing.html), [monitoring of request/response payloads](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/logging.html), [visualisation of real time model health](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/analytics.html). Alerting for [outlier detection](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/outlier_detection.html) and [concept drift](https://docs.seldon.io/projects/seldon-core/en/latest/analytics/drift_detection.html) can be setup. 

Now, it's time to get hands on!