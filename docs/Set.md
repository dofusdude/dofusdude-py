# Set


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**equipment_ids** | **List[int]** |  | [optional] 
**effects** | **Dict[str, List[Effect]]** |  | [optional] 
**highest_equipment_level** | **int** |  | [optional] 
**is_cosmetic** | **bool** |  | [optional] 

## Example

```python
from dofusdude.models.set import Set

# TODO update the JSON string below
json = "{}"
# create an instance of Set from a JSON string
set_instance = Set.from_json(json)
# print the JSON string representation of the object
print(Set.to_json())

# convert the object into a dict
set_dict = set_instance.to_dict()
# create an instance of Set from a dict
set_from_dict = Set.from_dict(set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


