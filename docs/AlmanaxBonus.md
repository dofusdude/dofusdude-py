# AlmanaxBonus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**type** | [**GetMetaAlmanaxBonuses200ResponseInner**](GetMetaAlmanaxBonuses200ResponseInner.md) |  | [optional] 

## Example

```python
from dofusdude.models.almanax_bonus import AlmanaxBonus

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxBonus from a JSON string
almanax_bonus_instance = AlmanaxBonus.from_json(json)
# print the JSON string representation of the object
print(AlmanaxBonus.to_json())

# convert the object into a dict
almanax_bonus_dict = almanax_bonus_instance.to_dict()
# create an instance of AlmanaxBonus from a dict
almanax_bonus_from_dict = AlmanaxBonus.from_dict(almanax_bonus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


