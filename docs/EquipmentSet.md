# EquipmentSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**equipment_ids** | **List[int]** |  | [optional] 
**effects** | **List[List[SetEffectsEntry]]** |  | [optional] 
**highest_equipment_level** | **int** |  | [optional] 
**is_cosmetic** | **bool** |  | [optional] 

## Example

```python
from dofusdude.models.equipment_set import EquipmentSet

# TODO update the JSON string below
json = "{}"
# create an instance of EquipmentSet from a JSON string
equipment_set_instance = EquipmentSet.from_json(json)
# print the JSON string representation of the object
print(EquipmentSet.to_json())

# convert the object into a dict
equipment_set_dict = equipment_set_instance.to_dict()
# create an instance of EquipmentSet from a dict
equipment_set_from_dict = EquipmentSet.from_dict(equipment_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


