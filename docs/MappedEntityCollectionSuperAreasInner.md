# MappedEntityCollectionSuperAreasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
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
from dofusdude.models.mapped_entity_collection_super_areas_inner import MappedEntityCollectionSuperAreasInner

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityCollectionSuperAreasInner from a JSON string
mapped_entity_collection_super_areas_inner_instance = MappedEntityCollectionSuperAreasInner.from_json(json)
# print the JSON string representation of the object
print(MappedEntityCollectionSuperAreasInner.to_json())

# convert the object into a dict
mapped_entity_collection_super_areas_inner_dict = mapped_entity_collection_super_areas_inner_instance.to_dict()
# create an instance of MappedEntityCollectionSuperAreasInner from a dict
mapped_entity_collection_super_areas_inner_from_dict = MappedEntityCollectionSuperAreasInner.from_dict(mapped_entity_collection_super_areas_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


