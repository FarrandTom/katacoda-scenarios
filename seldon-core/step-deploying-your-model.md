You will now deploy a machine learning classifier to your freshly setup Seldon environment! 🤩

At this point you should be working in **Terminal 2**, with your port forwarding listener running in the original terminal. 

To begin with, you need to define the configuration of the SeldonDeployment which will orchestrate the serving of your model. In this example you will use this simple config: 
```
apiVersion: machinelearning.seldon.io/v1alpha2
kind: SeldonDeployment
metadata:
  name: seldon-deployment-example
spec:
  name: sklearn-iris-deployment
  predictors:
  - componentSpecs:
    - spec:
        containers:
        - image: seldonio/sklearn-iris:0.1
          imagePullPolicy: IfNotPresent
          name: sklearn-iris-classifier
    graph:
      children: []
      endpoint:
        type: REST
      name: sklearn-iris-classifier
      type: MODEL
    name: sklearn-iris-predictor
    replicas: 1
```

In the config file above you are creating a custom resource of `kind: SeldonDeployment`. You are making use of a `predictor` component which will pull and run the `seldonio/sklearn-iris:0.1` model. Finally, under the `graph` section you are creating a REST model endpoint called `sklearn-iris-predictor`. 

This config has been pre-uploaded to your environment (you can view and edit it with `nano sklearn_iris_deployment.yaml`). ✅

To create the specified Seldon deployment run:
`kubectl create -f sklearn_iris_deployment.yaml`{{execute}}

Again, you can watch the rollout of the model deployment:
`kubectl rollout status deploy/$(kubectl get deploy -l seldon-deployment-id=seldon-deployment-example -o jsonpath='{.items[0].metadata.name}')`{{execute}}

When the deployment is ready you should see a similar message: `deployment "seldon-92a927e5e90d7602e08ba9b9304f70e8" successfully rolled out`

You can view your new deployment pods with: `kubectl get pods -n seldon`{{execute}}

Congratulations you have deployed your first Seldon model! 🥳

Next, you'll try testing it...

