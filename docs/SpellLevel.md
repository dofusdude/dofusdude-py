# SpellLevel

One grade of a spell. The levels array contains these spell variants, not player levels. Grade numbers are local to the containing spell and are independent of monster grades.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** | ID of the spell-level definition. Different from the parent spell ID and from the grade number. Used by explicit spell-level references such as script spell_level_ids. | [optional] 
**grade** | **int** | Number identifying this variant within its spell. Select by this value, not by the array position. Used by the spell detail endpoint&#39;s grade parameter. | [optional] 
**ap_cost** | **int** | Action points required to cast this spell grade. | [optional] 
**critical_hit_probability** | **int** | Base critical-hit percentage recorded for this spell grade, before fighter-specific modifiers. | [optional] 
**min_player_level** | **int** | Player-level requirement recorded for this spell grade. This is not its grade number or a monster combat level. | [optional] 
**min_range** | **int** | Minimum casting range in combat cells. | [optional] 
**max_range** | **int** | Maximum casting range in combat cells as defined by this grade. | [optional] 
**max_cast_per_turn** | **int** | Per-caster cast limit within a turn as recorded by the source. | [optional] 
**max_cast_per_target** | **int** |  | [optional] 
**max_global_cast_per_turn** | **int** |  | [optional] 
**max_global_cast_per_target** | **int** |  | [optional] 
**min_cast_interval** | **int** | Minimum interval between casts, measured in fight turns. | [optional] 
**initial_cooldown** | **int** | Initial wait before casting, measured in fight turns. | [optional] 
**global_cooldown** | **int** |  | [optional] 
**ignore_prison_glyph** | **bool** |  | [optional] 
**spell_breed** | **int** |  | [optional] 
**states_criterion** | [**EligibilityNode**](EligibilityNode.md) | Available client-side state requirements for this spell grade. Null does not assert that the server imposes no restriction. | [optional] 
**preview_zones** | [**List[SpellPreviewZone]**](SpellPreviewZone.md) | Client preview and activation geometry for this grade. Use each effect&#39;s zone for its actual effect-area definition. | [optional] 
**effects** | [**List[SpellEffect]**](SpellEffect.md) | Normal-cast effects for this grade. Each entry has independent targeting and area geometry. | [optional] 
**critical_effects** | [**List[SpellEffect]**](SpellEffect.md) | Critical-cast effects for this grade. Keep separate from normal effects rather than applying both arrays to every cast. | [optional] 

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


