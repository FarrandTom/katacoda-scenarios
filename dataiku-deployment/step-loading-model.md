# Time to get your hands dirty with Python

In this tutorial you will be developing a Seldon model server for a Dataiku saved PMML model. Not only that, but you will your final Seldon model will also be totally resuable- allowing you to apply it to any other Dataiku PMML models!

In this step of the tutorial you will work on developing the Python code to download the model from a storage bucket and load it into memory.

Start by creating a new Python file titled `RandomForest.py`:

```(bash)
touch RandomForest.py
```{{execute}}

Next, open this blank Python file in the editor and fill in the below code, either by copy pasting or typing it in manually.

```(python)
import logging

from io import BytesIO
from google.cloud import storage

import numpy as np
from pypmml import Model

logger = logging.getLogger(__name__)

class RandomForest(object):

    def __init__(self, model_path):
        logger.info(f"Connecting to storage bucket")
        self.client = storage.Client.create_anonymous_client()
        self.bucket = self.client.bucket('tom-seldon-examples')

        logger.info(f"Model name: {model_path}")
        self.model_path = model_path

        logger.info("Loading model.")
        self.load_model()
        self.ready = False

    def load_model(self):
        logger.info("Loading model")
        model_file = BytesIO()
        model_blob = self.bucket.get_blob(f'{self.model_path}')
        model_blob.download_to_file(model_file)
        self.model = Model.fromFile('high-revenue-prediction.pmml')

        self.ready = True
```
