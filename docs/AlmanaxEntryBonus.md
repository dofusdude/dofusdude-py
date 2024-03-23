# AlmanaxEntryBonus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**type** | [**GetMetaAlmanaxBonuses200ResponseInner**](GetMetaAlmanaxBonuses200ResponseInner.md) |  | [optional] 

## Example

```python
from dofusdude.models.almanax_entry_bonus import AlmanaxEntryBonus

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxEntryBonus from a JSON string
almanax_entry_bonus_instance = AlmanaxEntryBonus.from_json(json)
# print the JSON string representation of the object
print(AlmanaxEntryBonus.to_json())

# convert the object into a dict
almanax_entry_bonus_dict = almanax_entry_bonus_instance.to_dict()
# create an instance of AlmanaxEntryBonus from a dict
almanax_entry_bonus_form_dict = almanax_entry_bonus.from_dict(almanax_entry_bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


