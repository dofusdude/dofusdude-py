# Weapon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**TranslatedId**](TranslatedId.md) |  | [optional] 
**is_weapon** | **bool** | always true when the item is a weapon. Many fields are now available. Always check for this flag first when getting single equipment items. | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**effects** | [**List[Effect]**](Effect.md) |  | [optional] 
**conditions** | [**ConditionNode**](ConditionNode.md) |  | [optional] 
**critical_hit_probability** | **int** |  | [optional] 
**critical_hit_bonus** | **int** |  | [optional] 
**max_cast_per_turn** | **int** |  | [optional] 
**ap_cost** | **int** |  | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 
**recipe** | [**List[Recipe]**](Recipe.md) |  | [optional] 
**parent_set** | [**TranslatedId**](TranslatedId.md) |  | [optional] 

## Example

```python
from dofusdude.models.weapon import Weapon

# TODO update the JSON string below
json = "{}"
# create an instance of Weapon from a JSON string
weapon_instance = Weapon.from_json(json)
# print the JSON string representation of the object
print(Weapon.to_json())

# convert the object into a dict
weapon_dict = weapon_instance.to_dict()
# create an instance of Weapon from a dict
weapon_from_dict = Weapon.from_dict(weapon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


