# EquipmentParentSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.equipment_parent_set import EquipmentParentSet

# TODO update the JSON string below
json = "{}"
# create an instance of EquipmentParentSet from a JSON string
equipment_parent_set_instance = EquipmentParentSet.from_json(json)
# print the JSON string representation of the object
print EquipmentParentSet.to_json()

# convert the object into a dict
equipment_parent_set_dict = equipment_parent_set_instance.to_dict()
# create an instance of EquipmentParentSet from a dict
equipment_parent_set_form_dict = equipment_parent_set.from_dict(equipment_parent_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


