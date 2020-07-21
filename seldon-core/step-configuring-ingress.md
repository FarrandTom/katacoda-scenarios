At this point, you have Seldon Core up and running. There is now only one more step prior to deploying your first machine learning model onto Seldon. 🤓

You now need to ensure that any models deployed to Seldon will be accessible to users. You will set up a simple API gateway to control ingress to your cluster. To do this you will use the [Ambassador stack](https://www.getambassador.io/). 

Once more you will make use of Helm to grab and install Ambassador. First, add the Ambassador repository to Helm:
`helm repo add datawire https://www.getambassador.io`{{execute}}

Make sure everything is up-to-date:
`helm repo update`{{execute}}

You can now install Ambassador in the `seldon` namespace you created earlier: 
`helm install ambassador datawire/ambassador --set image.repository=quay.io/datawire/ambassador --set enableAES=false --set crds.keep=false --namespace seldon`{{execute}}

As before, you can use Kubernetes to watch the rollout of your deployment (this can take a couple of minutes to get up and running): 
`kubectl rollout status deployment.apps/ambassador -n seldon`{{execute}}

Once the Ambassador pods have been deployed and are running, you will run the following command:
`kubectl port-forward $(kubectl get pods -n seldon -l app.kubernetes.io/name=ambassador -o jsonpath='{.items[0].metadata.name}') -n seldon 8003:8080`{{execute}}

This will forward traffic from the local `8003` port to port `8080` of the Ambassador ingress gateway pod within Kubernetes. Ambassador will then route this traffic to your Seldon deployments.

The ouput of this command should look similar to the below:
```
Forwarding from 127.0.0.1:8003 -> 8080
Forwarding from [::1]:8003 -> 8080
```
This listener will wait for ingress traffic to forward on from port `8003` to the pod port of `8080`. For the rest of the tutorial you will now work in **Terminal 2**. It should already be open and ready to use as a separate tab at the top of your terminal environment. 

🤟