# Spell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**icon_id** | **int** |  | [optional] 
**admin_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**type** | [**CombatReference**](CombatReference.md) |  | [optional] 
**classes** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**monsters** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**levels** | [**List[SpellLevel]**](SpellLevel.md) |  | 
**scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 
**critical_scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 

## Example

```python
from dofusdude.models.spell import Spell

# TODO update the JSON string below
json = "{}"
# create an instance of Spell from a JSON string
spell_instance = Spell.from_json(json)
# print the JSON string representation of the object
print(Spell.to_json())

# convert the object into a dict
spell_dict = spell_instance.to_dict()
# create an instance of Spell from a dict
spell_from_dict = Spell.from_dict(spell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


