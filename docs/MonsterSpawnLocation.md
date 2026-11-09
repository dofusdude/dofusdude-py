# MonsterSpawnLocation

Known spawn subarea with its parent area, super-area and map membership. Does not assert a spawn on each listed map and does not include spawn probabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subarea** | [**CombatReference**](CombatReference.md) |  | 
**area** | [**CombatReference**](CombatReference.md) |  | 
**super_area** | [**CombatReference**](CombatReference.md) |  | 
**subarea_maps** | [**List[MonsterSpawnLocationSubareaMapsInner]**](MonsterSpawnLocationSubareaMapsInner.md) | Maps belonging to the referenced subarea. Map membership alone is not proof that the monster spawns on a particular map. | 
**preferred** | **bool** | Whether the source marks this as a preferred subarea. A preference flag, not a spawn percentage or guarantee of presence. | 

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


