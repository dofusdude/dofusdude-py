# Resource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**effects** | [**List[Effect]**](Effect.md) |  | [optional] 
**conditions** | [**ConditionNode**](ConditionNode.md) |  | [optional] 
**recipe** | [**List[Recipe]**](Recipe.md) |  | [optional] 

## Example

```python
from dofusdude.models.resource import Resource

# TODO update the JSON string below
json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print(Resource.to_json())

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


