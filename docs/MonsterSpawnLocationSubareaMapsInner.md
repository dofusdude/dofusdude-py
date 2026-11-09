# MonsterSpawnLocationSubareaMapsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**position_x** | **int** |  | 
**position_y** | **int** |  | 
**world_map_id** | **int** | World-map context for these coordinates. Coordinates alone are not a globally unique map identifier. | 

## Example

```python
from dofusdude.models.monster_spawn_location_subarea_maps_inner import MonsterSpawnLocationSubareaMapsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterSpawnLocationSubareaMapsInner from a JSON string
monster_spawn_location_subarea_maps_inner_instance = MonsterSpawnLocationSubareaMapsInner.from_json(json)
# print the JSON string representation of the object
print(MonsterSpawnLocationSubareaMapsInner.to_json())

# convert the object into a dict
monster_spawn_location_subarea_maps_inner_dict = monster_spawn_location_subarea_maps_inner_instance.to_dict()
# create an instance of MonsterSpawnLocationSubareaMapsInner from a dict
monster_spawn_location_subarea_maps_inner_from_dict = MonsterSpawnLocationSubareaMapsInner.from_dict(monster_spawn_location_subarea_maps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


