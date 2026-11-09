# MappedEntityCollectionSpellsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**description** | **str** |  | [optional] 
**icon_id** | **int** |  | [optional] 
**admin_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**type** | [**SpellType**](SpellType.md) |  | [optional] 
**base_preview_zone** | [**EffectZone**](EffectZone.md) |  | [optional] 
**classes** | [**List[CombatReference]**](CombatReference.md) | Reverse references to playable classes associated with this spell. These are compact references, not complete class documents. | [optional] 
**monsters** | [**List[CombatReference]**](CombatReference.md) | Reverse references to monsters associated with this spell. Use a monster&#39;s grade-specific assignments to determine which spell grade it uses. | [optional] 
**levels** | [**List[SpellLevel]**](SpellLevel.md) | Available spell grades. Despite the field name, entries are not player levels. A grade-filtered detail response contains only the requested entry while retaining the parent spell object. | 
**scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 
**critical_scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 

## Example

```python
from dofusdude.models.mapped_entity_collection_spells_inner import MappedEntityCollectionSpellsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityCollectionSpellsInner from a JSON string
mapped_entity_collection_spells_inner_instance = MappedEntityCollectionSpellsInner.from_json(json)
# print the JSON string representation of the object
print(MappedEntityCollectionSpellsInner.to_json())

# convert the object into a dict
mapped_entity_collection_spells_inner_dict = mapped_entity_collection_spells_inner_instance.to_dict()
# create an instance of MappedEntityCollectionSpellsInner from a dict
mapped_entity_collection_spells_inner_from_dict = MappedEntityCollectionSpellsInner.from_dict(mapped_entity_collection_spells_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


