# SpellLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**grade** | **int** |  | [optional] 
**ap_cost** | **int** |  | [optional] 
**min_range** | **int** |  | [optional] 
**max_range** | **int** |  | [optional] 
**max_cast_per_turn** | **int** |  | [optional] 
**max_cast_per_target** | **int** |  | [optional] 
**max_global_cast_per_turn** | **int** |  | [optional] 
**max_global_cast_per_target** | **int** |  | [optional] 
**min_cast_interval** | **int** |  | [optional] 
**initial_cooldown** | **int** |  | [optional] 
**global_cooldown** | **int** |  | [optional] 
**ignore_prison_glyph** | **bool** |  | [optional] 
**spell_breed** | **int** |  | [optional] 
**effects** | [**List[SpellEffect]**](SpellEffect.md) |  | [optional] 
**critical_effects** | [**List[SpellEffect]**](SpellEffect.md) |  | [optional] 

## Example

```python
from dofusdude.models.spell_level import SpellLevel

# TODO update the JSON string below
json = "{}"
# create an instance of SpellLevel from a JSON string
spell_level_instance = SpellLevel.from_json(json)
# print the JSON string representation of the object
print(SpellLevel.to_json())

# convert the object into a dict
spell_level_dict = spell_level_instance.to_dict()
# create an instance of SpellLevel from a dict
spell_level_from_dict = SpellLevel.from_dict(spell_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


