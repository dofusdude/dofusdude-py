# Equipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 
**is_weapon** | **bool** |  | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**effects** | [**List[EffectsEntry]**](EffectsEntry.md) |  | [optional] 
**conditions** | [**List[ConditionEntry]**](ConditionEntry.md) |  | [optional] 
**condition_tree** | [**ConditionTreeNode**](ConditionTreeNode.md) |  | [optional] 
**recipe** | [**List[RecipeEntry]**](RecipeEntry.md) |  | [optional] 
**parent_set** | [**EquipmentParentSet**](EquipmentParentSet.md) |  | [optional] 

## Example

```python
from dofusdude.models.equipment import Equipment

# TODO update the JSON string below
json = "{}"
# create an instance of Equipment from a JSON string
equipment_instance = Equipment.from_json(json)
# print the JSON string representation of the object
print Equipment.to_json()

# convert the object into a dict
equipment_dict = equipment_instance.to_dict()
# create an instance of Equipment from a dict
equipment_form_dict = equipment.from_dict(equipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


