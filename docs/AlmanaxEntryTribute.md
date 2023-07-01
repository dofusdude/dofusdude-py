# AlmanaxEntryTribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**AlmanaxEntryTributeItem**](AlmanaxEntryTributeItem.md) |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.almanax_entry_tribute import AlmanaxEntryTribute

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxEntryTribute from a JSON string
almanax_entry_tribute_instance = AlmanaxEntryTribute.from_json(json)
# print the JSON string representation of the object
print AlmanaxEntryTribute.to_json()

# convert the object into a dict
almanax_entry_tribute_dict = almanax_entry_tribute_instance.to_dict()
# create an instance of AlmanaxEntryTribute from a dict
almanax_entry_tribute_form_dict = almanax_entry_tribute.from_dict(almanax_entry_tribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


