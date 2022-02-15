----

The penultimate stage in the process is to build and push your container image.

All of the component pieces are now in place to ensure this is a smooth process. You simply have to run:

```(bash)
docker build . -t random-forest:0.1
```{{execute}}

This will build and tag a Docker image with the `random-forest:0.1` tag. The next stage is to then push this freshly build Seldon server to your Dockerhub, ready for deployment: 

```(bash)
docker push \<YOUR DOCKER HUB NAME>/random-forest:0.1
```

Once the server is built and pushed it can be deployed to Seldon!
