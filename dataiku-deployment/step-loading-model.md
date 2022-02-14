# Downloading the Dataiku artefact

In this tutorial you will be developing a Seldon model server for a Dataiku saved PMML model. Not only that, but your final Seldon server will also be totally resuable- allowing you to apply it to any other Dataiku PMML models!

In this step of the tutorial you will work on developing the Python code to download the model from a storage bucket and load it into memory.

## Setting up the Code

Start by creating a new Python file titled `RandomForest.py`:

```(bash)
touch RandomForest.py
```{{execute}}

Next, open this blank Python file in the editor and fill in the below code, either by copy pasting or typing it in manually.

```(python)
# IMPORTS
import logging

from io import BytesIO
from google.cloud import storage

import numpy as np
from pypmml import Model

from typing import Dict, List, Union, Iterable

logger = logging.getLogger(__name__)


class RandomForest(object):

    # INIT METHOD
    def __init__(self, model_path):
        logger.info(f"Connecting to storage bucket")
        self.client = storage.Client.create_anonymous_client()
        self.bucket = self.client.bucket('tom-seldon-examples')

        logger.info(f"Model name: {model_path}")
        self.model_path = model_path

        logger.info("Loading model.")
        self.load_model()
        self.ready = False

    # LOAD MODEL METHOD
    def load_model(self):
        logger.info("Loading model")
        model_file = BytesIO()
        model_blob = self.bucket.get_blob(f'{self.model_path}')
        model_blob.download_to_file(model_file)
        self.model = Model.fromFile('high-revenue-prediction.pmml')

        self.ready = True
```

## Understanding the Code

The structure of `RandomForest.py` thus far can be broken down into the following pieces:

1. **IMPORTS**: Standard Python imports, the only piece to note here is that you are downloading from a Google storage bucket, hence the inclusion of the `google.cloud` import. This could be readily swapped out to support your chosen storage system.
2. **INIT METHOD**: The `__init__` method connects you to the storage bucket and sets the path to the model artefact within the bucket. You'll notice that the `__init__` method expects a `model_path` parameter which is an adjustable variable fed to the model at runtime. This tweak is one of the main reasons as to why this Seldon server you're building can be considered reusable- `model_path` can be updated at runtime to a different model artefact each time.
3. **LOAD MODEL METHOD**: The `__init__` method calls the `load_model` method which downloads the model artefact from storage and loads it using `PyPMML`. 

The only other thing which you should note is that the name of the model class is the same as the Python script which houses it.

Now that you have the code to load your model, you can focus on the code to perform inference!
