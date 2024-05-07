# AlmanaxEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus** | [**AlmanaxEntryBonus**](AlmanaxEntryBonus.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**tribute** | [**AlmanaxEntryTribute**](AlmanaxEntryTribute.md) |  | [optional] 
**reward_kamas** | **int** | Amount of Kamas you get as reward for finishing this Almanax quest. | [optional] 

## Example

```python
from dofusdude.models.almanax_entry import AlmanaxEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxEntry from a JSON string
almanax_entry_instance = AlmanaxEntry.from_json(json)
# print the JSON string representation of the object
print(AlmanaxEntry.to_json())

# convert the object into a dict
almanax_entry_dict = almanax_entry_instance.to_dict()
# create an instance of AlmanaxEntry from a dict
almanax_entry_from_dict = AlmanaxEntry.from_dict(almanax_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


