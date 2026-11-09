# SpellEffect

One normal or critical effect of a particular spell grade. Its zone defines where it applies, target_mask defines eligible targets and triggers defines activation events. Templated text is for display, not a formula to parse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Localized effect category, such as Air damage. This is not a spell ID or a structured game reference. | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**duration** | **int** | Effect duration in fight turns as represented by the source. Not a real-time duration in seconds. | [optional] 
**delay** | **int** | Delay before the effect in fight turns as represented by the source. | [optional] 
**random** | **float** | Source random-selection value. Do not interpret it as a percentage without the effect&#39;s selection rules. | [optional] 
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
**templated** | **str** | Localized effect text suitable for display. Numeric effect properties remain available separately. | [optional] 

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


