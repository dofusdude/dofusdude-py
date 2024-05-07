# WeaponRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.weapon_range import WeaponRange

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponRange from a JSON string
weapon_range_instance = WeaponRange.from_json(json)
# print the JSON string representation of the object
print(WeaponRange.to_json())

# convert the object into a dict
weapon_range_dict = weapon_range_instance.to_dict()
# create an instance of WeaponRange from a dict
weapon_range_from_dict = WeaponRange.from_dict(weapon_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


