# WorldArea

Geographic data from a super-area, area or subarea endpoint. The hierarchy is super-area to area to subarea to map. Field availability depends on the selected geographic resource. Unrelated to combat-cell effect zones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**world_map_id** | **int** | World-map context supplied on super-area records. | [optional] 
**areas** | [**List[CombatReference]**](CombatReference.md) | Child area references supplied on super-area records. | [optional] 
**level** | **int** | Suggested geographic difficulty level supplied on subarea records. Not a monster grade or the level of every monster there. | [optional] 
**dungeon_id** | **int** | Dungeon association when supplied by the subarea data. | [optional] 
**maps** | [**List[WorldMapReference]**](WorldMapReference.md) | Map membership supplied on subarea records. Does not imply a spawn on every map. | [optional] 
**super_area** | [**CombatReference**](CombatReference.md) |  | [optional] 
**area** | [**CombatReference**](CombatReference.md) |  | [optional] 
**subareas** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 
**monsters** | [**List[CombatReference]**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.world_area import WorldArea

# TODO update the JSON string below
json = "{}"
# create an instance of WorldArea from a JSON string
world_area_instance = WorldArea.from_json(json)
# print the JSON string representation of the object
print(WorldArea.to_json())

# convert the object into a dict
world_area_dict = world_area_instance.to_dict()
# create an instance of WorldArea from a dict
world_area_from_dict = WorldArea.from_dict(world_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


