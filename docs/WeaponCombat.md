# WeaponCombat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | [**EffectZone**](EffectZone.md) |  | 
**cast_in_line** | **bool** |  | 
**cast_in_diagonal** | **bool** |  | 
**requires_line_of_sight** | **bool** |  | 

## Example

```python
from dofusdude.models.weapon_combat import WeaponCombat

# TODO update the JSON string below
json = "{}"
# create an instance of WeaponCombat from a JSON string
weapon_combat_instance = WeaponCombat.from_json(json)
# print the JSON string representation of the object
print(WeaponCombat.to_json())

# convert the object into a dict
weapon_combat_dict = weapon_combat_instance.to_dict()
# create an instance of WeaponCombat from a dict
weapon_combat_from_dict = WeaponCombat.from_dict(weapon_combat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


