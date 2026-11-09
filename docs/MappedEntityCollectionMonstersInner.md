# MappedEntityCollectionMonstersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**race** | [**MonsterRace**](MonsterRace.md) |  | 
**grades** | [**List[MonsterGrade]**](MonsterGrade.md) | Variants of this monster. Each has its own combat level, statistics and assigned spells. The monster grade number is not a spell grade number or combat level. | 
**spawn_locations** | [**List[MonsterSpawnLocation]**](MonsterSpawnLocation.md) | Known spawn subareas and their geographic parents. This is not live population data or a per-map spawn probability. Maps listed within a subarea are not guaranteed individual spawn points. | 
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
from dofusdude.models.mapped_entity_collection_monsters_inner import MappedEntityCollectionMonstersInner

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityCollectionMonstersInner from a JSON string
mapped_entity_collection_monsters_inner_instance = MappedEntityCollectionMonstersInner.from_json(json)
# print the JSON string representation of the object
print(MappedEntityCollectionMonstersInner.to_json())

# convert the object into a dict
mapped_entity_collection_monsters_inner_dict = mapped_entity_collection_monsters_inner_instance.to_dict()
# create an instance of MappedEntityCollectionMonstersInner from a dict
mapped_entity_collection_monsters_inner_from_dict = MappedEntityCollectionMonstersInner.from_dict(mapped_entity_collection_monsters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


