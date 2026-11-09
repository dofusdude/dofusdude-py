# SpellScriptUsage

Resolved client-side spell script binding, including target selection and areas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**script_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**random** | **int** |  | [optional] 
**random_group** | **int** |  | [optional] 
**sequence_group** | **int** |  | [optional] 
**activation_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**caster_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**target_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**activation_zone** | [**EffectZone**](EffectZone.md) |  | [optional] 
**target_zone** | [**EffectZone**](EffectZone.md) |  | [optional] 
**condition** | **Dict[str, object]** |  | [optional] 
**targets_affected_concurrently** | **bool** |  | [optional] 
**target_treated_as_caster** | **bool** |  | [optional] 
**spell_level_ids** | **List[int]** | Spell-level definition IDs to which this script binding applies. Match SpellLevel.ankama_id, not Spell.ankama_id or SpellLevel.grade. | [optional] 

## Example

```python
from dofusdude.models.spell_script_usage import SpellScriptUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SpellScriptUsage from a JSON string
spell_script_usage_instance = SpellScriptUsage.from_json(json)
# print the JSON string representation of the object
print(SpellScriptUsage.to_json())

# convert the object into a dict
spell_script_usage_dict = spell_script_usage_instance.to_dict()
# create an instance of SpellScriptUsage from a dict
spell_script_usage_from_dict = SpellScriptUsage.from_dict(spell_script_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


