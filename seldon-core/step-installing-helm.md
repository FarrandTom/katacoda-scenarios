It's time to get your hands dirty! 

Prior to installing Seldon you will install [Helm](https://docs.helm.sh/) ⛴. Helm is a Kubernetes package manager which makes it dead easy to install other Kubernetes software with- including Seldon.

Helm is straightforward to install. You will first grab the install script:
`curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3`{{execute}}

Changing the permissions, to allow the script to be executed:
`chmod 700 get_helm.sh`{{execute}}

Running the installer:
`./get_helm.sh`{{execute}}

If you are successful, you will see the following message:
`helm installed into /usr/local/bin/helm`

👍