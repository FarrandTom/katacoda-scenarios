
# Time to pull in the model artefact

Seldon picks up once a model has been trained providing best of breed deployment, monitoring, management and explainability capabilities. Therefore, before you get going, you will need a Dataiku model to deploy!

This tutorial makes use of a pre-trained Dataiku model saved in the Predictive Model Markup Language (PMML) format.

This model has been uploaded to a Google storage bucket where it can easily be pulled into your local Katacoda environment to begin working with. All you need to do is run the simple `wget` command below.

```(bash)
wget https://storage.googleapis.com/tom-seldon-examples/katacoda-scenarios/dataiku-model/high-revenue-prediction.pmml

```{{execute}}

----
Seldon supports the building of resuable model servers, 
----

You can validate that it has been successfully downloaded into your environment by running `ll` where you should be able to see the `high-revenue-prediction.pmml` file ready and waiting for deployment!* 

*Note: It seems as though the Katacoda editor does not display `.pmml` files, but it does exist- promise!
