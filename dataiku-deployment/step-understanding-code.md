----

In this tutorial you will be developing a Seldon model server for a Dataiku saved PMML model. Not only that, but your final Seldon server will also be totally resuable- allowing you to apply it to any other Dataiku PMML models!

In this step of the tutorial you will gain an understanding of the structure of the Seldon Python code required to download, load and generate predictions from the Dataiku model.

## Understanding the Code

In the Katacoda editor open up the `RandomForest.py` file. The `RandomForest.py` file contains all of the logic required for the Seldon model server.

The structure of `RandomForest.py` can be broken down into the following pieces:

1. **IMPORTS**: Standard Python imports, the only piece to note here is that you are downloading from a Google storage bucket, hence the inclusion of the `google.cloud` import. This could be readily swapped out to support your chosen storage system.

2. **INIT METHOD**: The `__init__` method connects you to the storage bucket and sets the path to the model artefact within the bucket. You'll notice that the `__init__` method expects a `model_path` parameter which is an adjustable variable fed to the model at runtime. This tweak is one of the main reasons as to why this Seldon server you're building can be considered reusable- `model_path` can be updated at runtime to a different model artefact each time.

3. **LOAD MODEL METHOD**: The `__init__` method calls the `load_model` method which downloads the model artefact from storage and loads it using `PyPMML`.

4. **PREDICT METHOD**: Your `predict` method is straightforward. Any exceptions are caught and logged in the try/except block. The inbound request is transformed into the format which the model expects by using the `zip` function to roll up the inference data with the feature names (you'll see the request format which Seldon expects in a little bit). Once the request has been created correctly the model is called with `self.model.predict(request)`. The prediction is then transformed into a response which is returned to the user.

The final thing which you should note is that the name of the model class (`RandomForest`) is the same as the Python script which houses it.

## Taking Stock

Phew! You have now added all of the Python code which is needed to create your Dataiku deployment. The remainder of this tutorial is focused on testing your work, and creating the final Docker image!
