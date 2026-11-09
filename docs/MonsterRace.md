# MonsterRace

Monster taxonomy. Race is the monster's family and super_race is the broader grouping. Neither is a playable class or a monster grade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**super_race** | [**CombatReference**](CombatReference.md) |  | 

## Example

```python
from dofusdude.models.monster_race import MonsterRace

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterRace from a JSON string
monster_race_instance = MonsterRace.from_json(json)
# print the JSON string representation of the object
print(MonsterRace.to_json())

# convert the object into a dict
monster_race_dict = monster_race_instance.to_dict()
# create an instance of MonsterRace from a dict
monster_race_from_dict = MonsterRace.from_dict(monster_race_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


