# ConditionEntry



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**int_value** | **int** |  | [optional] 
**element** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_entry import ConditionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionEntry from a JSON string
condition_entry_instance = ConditionEntry.from_json(json)
# print the JSON string representation of the object
print(ConditionEntry.to_json())

# convert the object into a dict
condition_entry_dict = condition_entry_instance.to_dict()
# create an instance of ConditionEntry from a dict
condition_entry_form_dict = condition_entry.from_dict(condition_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


