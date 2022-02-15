----

The final step is to deploy this onto the Seldon platform!

The simplest way to achieve this is to visit the workshop cluster's [user interface](http://35.204.150.218/seldon-deploy/).

You can login in using:

* Username: admin@seldon.io
* Password: 12341234

Next, select the "+ CREATE" button, this will bring up the deployment creation wizard. Add a deployment name which is unique and contains no capital letters or underscores, then select "Next".

On the "Default Predictor" screen select the "Custom" runtime, and pass in the link to your Docker image i.e. `seldonexamples/dataiku-example:0.1`. Click "Next".

Next, fill in the "Predictor Parameters" screen. This is where the `model_path` variable which your server expects is to be added. Click the green + to add a new key-value pair: `model_path: katacoda-scenarios/dataiku-model/high-revenue-prediction.pmml`.

You can move through the remaining screens using their default values and finally click "Launch" to create your deployment.

The final step is to test your new deployment. Once it has become available, click "Make a new prediction" and paste in the below request:

```(json)
{
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
}
```

You will see a successful 200 status code and the model's response.