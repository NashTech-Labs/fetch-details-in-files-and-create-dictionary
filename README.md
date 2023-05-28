# Fetch the details form two yamls and create the dictionary to perform operation on that dictionary

### This template will help us to fetch the details of the perticular resource type from the one yaml and from the second yaml, fetch the pipeline id with respect to that resource type. Suppose that we are working on the ADO pipeline and I have many ADO pipline and I want to run the perticular pipeline. So I can fetch the details from the both yaml [in my case, I am fetching only the resource type so that i can trigger the perticular resource pipeline].

-------
### You just need to follow the below steps to run the code:-

#### 1. Define the required details for the code and you can change the file name also as your need.

````
compute_yaml_file = 'compute.yaml'
resources_yaml_file = 'pipeline_id.yaml'

````

#### 2. Install the required packages in your system.

````
pip3 install -r requirements.txt
````

#### 3. Its time to run the main python code.

````
python3 fetch.py
````