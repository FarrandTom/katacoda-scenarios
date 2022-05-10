----

Now that you have tested your deployment locally it is time to being preparing to wrap it as a Docker container- ready for production!

Seldon exposes two avenues for creating Docker images, the first is to use `source-2-image` tooling which removes the need for model builders to write a Dockerfile, and creates a new image directly from the Seldon provided base images. You can find more information about that process [here](https://docs.seldon.io/projects/seldon-core/en/stable/python/python_wrapping_s2i.html).

In this case, you will add the Dockerfile directly. This is because `PyPMML` has a Java dependency and thus the fine grained control provided by the Dockerfile approach means that you can specifiy the inclusion of Java.

## Adding the Dockfile

First, create an empty Dockerfile.

```(bash)
touch Dockerfile
```{{execute}}

Then fill in the following details to outline how you would like your Seldon model server built. 

```(docker)
FROM openjdk:11
COPY --from=python:3.8-slim / /
WORKDIR /app

# Install python packages
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

# Seldon runs as user 8888 thus change file permissions as such
RUN chown -R 8888 /app

# Define environment variables
ENV MODEL_NAME RandomForest
ENV SERVICE_TYPE MODEL

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
```

## Understanding Your Dockerfile

The Dockerfile necessary to build the Seldon server is simple and straightforward. Stepping through it:

1. The `openjdk` toolkit is used to satisfy the requirement for Java. Meanwhile Python 3.7 is also added to the environment.
2. Next, the Python packages defined in `requirements.txt` are installed.
3. Both port 5000 and 9000 are exposed. Seldon automatically configures both REST and gRPC endpoints for all deployments.
4. Seldon by default runs all containers as user 8888, not as root. This is for security purposes, but to ensure all of your files are accessible at deployment time, including any which we download, `chown` is used to change the userid of the `/app` directory.
5. Finally, a very similar `seldon-core-microservice` command is built out using the model name, and the service type. Seldon allows you to build different custom services, models being one of them, but other examples include transformers, routers and combiners. More details can be found [here](https://docs.seldon.io/projects/seldon-core/en/stable/python/python_component.html#transformers).

Now that your Dockerfile is in place, it is time to build your container image!
