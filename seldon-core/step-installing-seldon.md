Next, you will install Seldon Core Operator. The Seldon Core Operator is responsible for taking the machine learning deployment you will specify and managing the underlying Kubernetes resources. 😎

Create a couple of namespaces.
1. `kubectl create namespace seldon`{{execute}}
2. `kubectl create namespace seldon-system`{{execute}}

The `seldon` namespace will hold your machine learning deployment and networking pods used for traffic ingress. `seldon-system` will contain the adminstration and management pods used by Seldon Core. Next you will update the `kubeconfig` for the `seldon` namespace:
`kubectl config set-context $(kubectl config current-context) --namespace=seldon`{{execute}}

You can now use Helm to install Seldon Core: 
`helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --set ambassador.enabled=true --set usageMetrics.enabled=true --namespace seldon-system`{{execute}}

This command grabs the Seldon Core Helm chart from the specified repository `--repo https://storage.googleapis.com/seldon-charts`, and enables Seldon for use with Ambassador `--set ambassador.enabled=true` (more on that later!).

You can watch the status of the deployment by running: 
`kubectl rollout status deploy/seldon-controller-manager -n seldon-system`{{execute}}

Once the Seldon Core pods are up and running your prompt will return, and you will see:
`deployment "seldon-controller-manager" successfully rolled out` 

👌