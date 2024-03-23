# Cosmetic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**CosmeticType**](CosmeticType.md) |  | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**effects** | [**List[EffectsEntry]**](EffectsEntry.md) |  | [optional] 
**conditions** | [**List[ConditionEntry]**](ConditionEntry.md) |  | [optional] 
**condition_tree** | [**ConditionTreeNode**](ConditionTreeNode.md) |  | [optional] 
**recipe** | [**List[RecipeEntry]**](RecipeEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.cosmetic import Cosmetic

# TODO update the JSON string below
json = "{}"
# create an instance of Cosmetic from a JSON string
cosmetic_instance = Cosmetic.from_json(json)
# print the JSON string representation of the object
print(Cosmetic.to_json())

# convert the object into a dict
cosmetic_dict = cosmetic_instance.to_dict()
# create an instance of Cosmetic from a dict
cosmetic_form_dict = cosmetic.from_dict(cosmetic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


