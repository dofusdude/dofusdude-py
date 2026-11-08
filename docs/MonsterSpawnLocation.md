# MonsterSpawnLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subarea** | [**CombatReference**](CombatReference.md) |  | 
**area** | [**CombatReference**](CombatReference.md) |  | 
**super_area** | [**CombatReference**](CombatReference.md) |  | 
**subarea_maps** | [**List[MonsterSpawnLocationSubareaMapsInner]**](MonsterSpawnLocationSubareaMapsInner.md) |  | 
**preferred** | **bool** | Whether the game marks this as the monster&#39;s preferred subarea. | 

## Example

```python
from dofusdude.models.monster_spawn_location import MonsterSpawnLocation

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterSpawnLocation from a JSON string
monster_spawn_location_instance = MonsterSpawnLocation.from_json(json)
# print the JSON string representation of the object
print(MonsterSpawnLocation.to_json())

# convert the object into a dict
monster_spawn_location_dict = monster_spawn_location_instance.to_dict()
# create an instance of MonsterSpawnLocation from a dict
monster_spawn_location_from_dict = MonsterSpawnLocation.from_dict(monster_spawn_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


