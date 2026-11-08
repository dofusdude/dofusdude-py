# SpellEffect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CombatReference**](CombatReference.md) |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**duration** | **int** |  | [optional] 
**delay** | **int** |  | [optional] 
**random** | **int** |  | [optional] 
**group** | **int** |  | [optional] 
**dispellable** | **int** |  | [optional] 
**effect_uid** | **int** | Stable identifier of this concrete effect instance. | [optional] 
**target_id** | **int** |  | [optional] 
**triggered_duration** | **int** |  | [optional] 
**display_zero** | **bool** |  | [optional] 
**modifier** | **int** |  | [optional] 
**zone** | [**EffectZone**](EffectZone.md) |  | [optional] 
**target_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**triggers** | [**SpellTriggers**](SpellTriggers.md) |  | [optional] 
**templated** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dofusdude.models.spell_effect import SpellEffect

# TODO update the JSON string below
json = "{}"
# create an instance of SpellEffect from a JSON string
spell_effect_instance = SpellEffect.from_json(json)
# print the JSON string representation of the object
print(SpellEffect.to_json())

# convert the object into a dict
spell_effect_dict = spell_effect_instance.to_dict()
# create an instance of SpellEffect from a dict
spell_effect_from_dict = SpellEffect.from_dict(spell_effect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


