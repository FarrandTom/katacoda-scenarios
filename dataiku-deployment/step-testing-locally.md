----

Now that you have your Python code and `requirements.txt` ready and waiting you can use the `seldon-core-microservice` to test your model locally.

The `seldon-core-microservice` allows us to test the model server logic locally without having to build the Docker image. This has the advantage of allowing you to quickly iterate in the development of your model server without having to build the Docker image each time.

## Spinning up the Seldon Server

Spin up the Seldon server by calling the `seldon-core-microservice` feeding in that you are creating a `MODEL` component, and the `model_path` parameter- where the artefact is stored in the storage bucket.

```(bash)
seldon-core-microservice RandomForest \
                         --service-type MODEL \
                         --parameters='[{ "name": "model_path", "value": "katacoda-scenarios/dataiku-model/high-revenue-prediction.pmml", "type": "STRING"}]'
```{{execute}}

You will now see a load of output related to the configuration of your Seldon model server. 

## Test Your Endpoint

Select the "+" next to "Terminal" and click on "Open New Terminal". This fresh terminal environment will allow you to use `curl` to send requests which will test your Seldon endpoint.

Custom model servers created using the Seldon tooling currently expect requests to use the Seldon protcol as the request and response schema- you can read more about that [here](https://docs.seldon.io/projects/seldon-core/en/stable/graph/protocols.html#rest-and-grpc-seldon-protocol). This is the reason as to why the request body is structured as a dictionary with a top level key of `data` and further entries for `names`, used to describe the feature names, and `ndarray` which contains the data features themselves.

The `curl` request will use the external `/predictions` endpoint which Seldon automatically exposes over both REST and gRPC to test the underlying `predict` method you created earlier. 

```(bash)
curl -H 'Content-Type: application/json' \
     -d '{
  "data": {
    "names": [
      "customer_id",
      "order_date_year_distinct",
      "order_date_month_distinct",
      "order_day_of_week_distinct",
      "pages_visited_avg",
      "total_sum",
      "gender",
      "age_first_order",
      "user_agent_brand",
      "user_agent_os",
      "user_agent_osversion",
      "ip_address_city",
      "ip_address_geopoint",
      "campaign",
      "count"
    ],
    "ndarray": [
      "000069",
      5,
      4,
      4,
      8.666666666666666,
      212,
      "F",
      1,
      "Chrome",
      "MacOS X",
      "10.12.3",
      "Changsha",
      "POINT(113.1136 50.1792)",
      "False",
      7
    ]
  }
}' \
     http://localhost:9000/api/v1.0/predictions

```{{execute}}

The sample model in this instance performing a binary classification between whether a website user is going to be a high revenue generator, or not. Therefore the output from your testing should look similar to the following. 

```(bash)
{"jsonData":{"data":{"names":["proba_True","proba_False"],"ndarray":[0.25793427065155805,0.742065729348442]}},"meta":{}}
```

Before you move on you should stop the model server running locally, return to the original terminal window and use CTRL+C to stop the server. Finally, deactivate your Python virtual environment:

```(bash)
deactivate
```{{exeucte}}

Time to focus on building the container image!
