# ItemListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**recipe** | [**List[RecipeEntry]**](RecipeEntry.md) |  | [optional] 
**description** | **str** |  | [optional] 
**conditions** | [**List[ConditionEntry]**](ConditionEntry.md) |  | [optional] 
**condition_tree** | [**ConditionTreeNode**](ConditionTreeNode.md) |  | [optional] 
**effects** | [**List[EffectsEntry]**](EffectsEntry.md) |  | [optional] 
**is_weapon** | **bool** |  | [optional] 
**pods** | **int** |  | [optional] 
**parent_set** | [**ItemListEntryParentSet**](ItemListEntryParentSet.md) |  | [optional] 
**critical_hit_probability** | **int** |  | [optional] 
**critical_hit_bonus** | **int** |  | [optional] 
**is_two_handed** | **bool** |  | [optional] 
**max_cast_per_turn** | **int** |  | [optional] 
**ap_cost** | **int** |  | [optional] 
**range** | [**ItemListEntryRange**](ItemListEntryRange.md) |  | [optional] 

## Example

```python
from dofusdude.models.item_list_entry import ItemListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ItemListEntry from a JSON string
item_list_entry_instance = ItemListEntry.from_json(json)
# print the JSON string representation of the object
print(ItemListEntry.to_json())

# convert the object into a dict
item_list_entry_dict = item_list_entry_instance.to_dict()
# create an instance of ItemListEntry from a dict
item_list_entry_from_dict = ItemListEntry.from_dict(item_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


