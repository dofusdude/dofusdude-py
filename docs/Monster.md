# Monster

A monster with its grades, family, spawn locations and drops. Spell expansion is optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**race** | [**MonsterRace**](MonsterRace.md) |  | 
**grades** | [**List[MonsterGrade]**](MonsterGrade.md) | Monster statistics and spells grouped by the monster grade that uses them. | 
**spawn_locations** | [**List[MonsterSpawnLocation]**](MonsterSpawnLocation.md) | Spawn subareas taken from the monster&#39;s authoritative subarea list. | 
**drops** | [**List[MonsterDrop]**](MonsterDrop.md) |  | 
**global_drops** | [**List[MonsterGlobalDrop]**](MonsterGlobalDrop.md) |  | [optional] 
**appearance** | [**ClassAppearance**](ClassAppearance.md) |  | [optional] 
**is_bounty** | **bool** |  | [optional] 
**corresponding_mini_boss** | [**CombatReference**](CombatReference.md) |  | [optional] 
**summon_cost** | **int** |  | [optional] 
**speed_adjust** | **int** |  | [optional] 
**scale_grade_reference** | **int** |  | [optional] 
**achievements** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**souls** | **List[Dict[str, object]]** |  | [optional] 
**characteristic_ratios** | **List[List[float]]** |  | [optional] 

## Example

```python
from dofusdude.models.monster import Monster

# TODO update the JSON string below
json = "{}"
# create an instance of Monster from a JSON string
monster_instance = Monster.from_json(json)
# print the JSON string representation of the object
print(Monster.to_json())

# convert the object into a dict
monster_dict = monster_instance.to_dict()
# create an instance of Monster from a dict
monster_from_dict = Monster.from_dict(monster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


