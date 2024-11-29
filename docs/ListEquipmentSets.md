# ListEquipmentSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PagedLinks**](PagedLinks.md) |  | [optional] 
**sets** | [**List[ListEquipmentSet]**](ListEquipmentSet.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_equipment_sets import ListEquipmentSets

# TODO update the JSON string below
json = "{}"
# create an instance of ListEquipmentSets from a JSON string
list_equipment_sets_instance = ListEquipmentSets.from_json(json)
# print the JSON string representation of the object
print(ListEquipmentSets.to_json())

# convert the object into a dict
list_equipment_sets_dict = list_equipment_sets_instance.to_dict()
# create an instance of ListEquipmentSets from a dict
list_equipment_sets_from_dict = ListEquipmentSets.from_dict(list_equipment_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


