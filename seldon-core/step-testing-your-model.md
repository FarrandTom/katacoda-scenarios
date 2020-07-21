You can now test our model deployment. 

The model you have deployed is a simple classifier based upon the Scikit-Learn Iris flower dataset. Based upon various measurements of everyone's favourite flower your classifier will distinguish between 3 different types of iris (Setosa, Versicolour, and Virginica). 

Therefore, your classifier expects an array of the form `[Sepal Length, Sepal Width, Petal Length, Petal Width]`. You can implement this simply using curl by running the following command:
`curl -s http://localhost:8003/seldon/seldon/seldon-deployment-example/api/v0.1/predictions -H "Content-Type: application/json" -d '{"data":{"ndarray":[[5.964,4.006,2.081,1.031]]}}'`{{execute}}

This should return a response which confirms the classification of your iris alongside a confidence scoring:
``

If you switch back to your original Terminal you should see the request traffic being picked up by your port-forwarding listener. 