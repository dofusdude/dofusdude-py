# SetListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**items** | **int** | amount | [optional] 
**level** | **int** |  | [optional] 
**effects** | **List[List[SetEffectsEntry]]** |  | [optional] 
**equipment_ids** | **List[int]** |  | [optional] 

## Example

```python
from dofusdude.models.set_list_entry import SetListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SetListEntry from a JSON string
set_list_entry_instance = SetListEntry.from_json(json)
# print the JSON string representation of the object
print(SetListEntry.to_json())

# convert the object into a dict
set_list_entry_dict = set_list_entry_instance.to_dict()
# create an instance of SetListEntry from a dict
set_list_entry_from_dict = SetListEntry.from_dict(set_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


