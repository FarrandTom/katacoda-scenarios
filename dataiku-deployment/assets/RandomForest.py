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

    # PREDICT METHOD
    def predict(self, X: np.ndarray, names: Iterable[str], meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:
        try:
            if not self.ready:
                self.load()
            
            request = {"features": dict(zip(names,X))}
            
            logger.info("Calling predict_proba...")
            prediction = self.model.predict(request)
            
            response = {"data": {"names": ["proba_True", "proba_False"], "ndarray": [prediction["proba_True"], prediction["proba_False"]]}}
            return response
        
        except Exception as ex:
            logging.exception("Exception during predict!")
            logging.exception(f"{ex}")