# Resource



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ResourceType**](ResourceType.md) |  | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**effects** | [**List[EffectsEntry]**](EffectsEntry.md) |  | [optional] 
**conditions** | [**List[ConditionEntry]**](ConditionEntry.md) |  | [optional] 
**condition_tree** | [**ConditionTreeNode**](ConditionTreeNode.md) |  | [optional] 
**recipe** | [**List[RecipeEntry]**](RecipeEntry.md) |  | [optional] 

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


