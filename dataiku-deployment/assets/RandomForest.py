# IMPORTS
import logging
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
        self.load_model()

    # LOAD MODEL METHOD
    def load_model(self):
        logger.info("Loading model")
        blob = self.bucket.blob(f'{self.model_path}')
        blob.download_to_filename('model.pmml')
        self.model = Model.fromFile('model.pmml')

    # PREDICT METHOD
    def predict(self, X: np.ndarray, names: Iterable[str], meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:
        try:
            request = {"features": dict(zip(names,X))}
            
            logger.info("Calling predict")
            prediction = self.model.predict(request)
            
            response = {"data": {"names": ["proba_True", "proba_False"], "ndarray": [prediction["proba_True"], prediction["proba_False"]]}}
            return response
        
        except Exception as ex:
            logging.exception("Exception during predict!")
            logging.exception(f"{ex}")