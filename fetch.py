import yaml

# fetch the piepline id from the pipeline_id.yaml
def fetch_pipeline_ids(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    pipeline_ids = {resource['resourceType']: resource['pipelineId'] for resource in data['resources']}
    return pipeline_ids


#fetch the pipeline info and create the dictionary from those files as per the resource type matched

def fetch_pipeline_info(compute_yaml_file, resources_yaml_file):
    pipeline_ids = fetch_pipeline_ids(resources_yaml_file)
    pipeline_info = {}

    with open(compute_yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    resources = data['all-resource']# + data['product-resources']

    for resource in resources:
        resource_type = resource['type']
        if resource_type in pipeline_ids:
            pipeline_id = pipeline_ids[resource_type]
            pipeline_info[resource_type] = pipeline_id

    return pipeline_info


# define the file to pass into the python function

compute_yaml_file = 'compute.yaml'
resources_yaml_file = 'pipeline_id.yaml'

pipeline_info = fetch_pipeline_info(compute_yaml_file, resources_yaml_file)

print(pipeline_info)
