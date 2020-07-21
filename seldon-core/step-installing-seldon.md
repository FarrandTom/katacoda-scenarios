Next, you will install the Seldon Core Operator. The Seldon Core Operator is responsible for taking the machine learning deployment you will specify and 
managing the underlying Kubernetes resources.

Create a couple of namespaces.
1. `kubectl create namespace seldon`{{execute}}
2. `kubectl create namespace seldon-system`{{execute}}

The `seldon` namespace will hold your machine learning deployment and networking pods used for traffic ingress. `seldon-system` will contain the control and management pods used by Seldon Core. 

You can now use Helm to install Seldon Core: 
```
helm install seldon-core seldon-core-operator 
        --repo https://storage.googleapis.com/seldon-charts 
        --set ambassador.enabled=true 
        --set usageMetrics.enabled=true 
        --namespace seldon-system
```
{{execute}}

