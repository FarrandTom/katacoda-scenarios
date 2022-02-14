# Preparing for Predictions

In the previous step you added the code required to pull in the model artefact. In this step you will create the predictive logic to perform inference on the freshly loaded model!

When wrapping custom models Seldon exposes the inference logic under the `predict` method. This is the method which you will now populate in your existing `RandomForest.py` file.

## Adding Your Predict Method

Thus, re-open the `RandomForest.py` file and beneath the `load_model` method add the following `predict` method.

```(python)
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
```

## Understanding Your Predict Method

Your `predict` method is straightforward. Any exceptions are caught and logged in the try/except block. The inbound request is transformed into the format which the model expects by using the `zip` function to roll up the inference data with the feature names (you'll see the request format which Seldon expects in a little bit).

Once the request has been created correctly the model is called with `self.model.predict(request)`. The prediction is then transformed into a response which is returned to the user.

You now have added all of the Python which is needed to create your Dataiku deployment. The remainder of this tutorial is focused on testing your work, and creating the final Docker image!
