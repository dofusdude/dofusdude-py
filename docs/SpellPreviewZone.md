# SpellPreviewZone

Client preview binding. Activation criteria and display geometry serve a different purpose from an effect's zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**activation_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**caster_mask** | [**TargetMask**](TargetMask.md) |  | [optional] 
**hidden** | **bool** |  | [optional] 
**activation_zone** | [**EffectZone**](EffectZone.md) |  | [optional] 
**display_zone** | [**EffectZone**](EffectZone.md) |  | [optional] 

## Example

```python
from dofusdude.models.spell_preview_zone import SpellPreviewZone

# TODO update the JSON string below
json = "{}"
# create an instance of SpellPreviewZone from a JSON string
spell_preview_zone_instance = SpellPreviewZone.from_json(json)
# print the JSON string representation of the object
print(SpellPreviewZone.to_json())

# convert the object into a dict
spell_preview_zone_dict = spell_preview_zone_instance.to_dict()
# create an instance of SpellPreviewZone from a dict
spell_preview_zone_from_dict = SpellPreviewZone.from_dict(spell_preview_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


