----

The penultimate stage in the process is to build and push your container image.

All of the component pieces are now in place to ensure this is a smooth process. You simply have to run:

```(bash)
apt-get update
docker build . -t dataiku-example:0.1
```{{execute}}

This will build and tag a Docker image with the `dataiku-example:0.1` tag. Prior to pushing your image to Seldon you will need to login to Docker using your own credentials. 

```(bash)
docker login
```{{execute}}

Re-tag your image to match your Docker username:

```(bash)
docker tag dataiku-example:0.1 <YOUR DOCKER HUB NAME>/dataiku-example:0.1
```

You can now push to your Docker repository:

```(bash)
docker push <YOUR DOCKER HUB NAME>/dataiku-example:0.1
```

Once the server is built and pushed it can be deployed to Seldon!
