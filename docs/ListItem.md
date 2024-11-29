# ListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**recipe** | [**List[Recipe]**](Recipe.md) |  | [optional] 
**description** | **str** |  | [optional] 
**conditions** | [**ConditionNode**](ConditionNode.md) |  | [optional] 
**effects** | [**List[Effect]**](Effect.md) |  | [optional] 
**is_weapon** | **bool** |  | [optional] 
**pods** | **int** |  | [optional] 
**parent_set** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**critical_hit_probability** | **int** |  | [optional] 
**critical_hit_bonus** | **int** |  | [optional] 
**max_cast_per_turn** | **int** |  | [optional] 
**ap_cost** | **int** |  | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_item import ListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ListItem from a JSON string
list_item_instance = ListItem.from_json(json)
# print the JSON string representation of the object
print(ListItem.to_json())

# convert the object into a dict
list_item_dict = list_item_instance.to_dict()
# create an instance of ListItem from a dict
list_item_from_dict = ListItem.from_dict(list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


