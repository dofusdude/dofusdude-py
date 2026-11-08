# MonsterGradeSpellsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**grade** | **int** | The spell grade assigned to this monster grade. | 
**url** | **str** | Grade-specific spell URL; already includes the &#x60;grade&#x60; query parameter. | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**description** | **str** |  | [optional] 
**icon_id** | **int** |  | [optional] 
**admin_name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**type** | [**CombatReference**](CombatReference.md) |  | [optional] 
**classes** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**monsters** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**levels** | [**List[SpellLevel]**](SpellLevel.md) |  | 
**scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 
**critical_scripts** | [**List[SpellScriptUsage]**](SpellScriptUsage.md) |  | [optional] 

## Example

```python
from dofusdude.models.monster_grade_spells_inner import MonsterGradeSpellsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterGradeSpellsInner from a JSON string
monster_grade_spells_inner_instance = MonsterGradeSpellsInner.from_json(json)
# print the JSON string representation of the object
print(MonsterGradeSpellsInner.to_json())

# convert the object into a dict
monster_grade_spells_inner_dict = monster_grade_spells_inner_instance.to_dict()
# create an instance of MonsterGradeSpellsInner from a dict
monster_grade_spells_inner_from_dict = MonsterGradeSpellsInner.from_dict(monster_grade_spells_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


