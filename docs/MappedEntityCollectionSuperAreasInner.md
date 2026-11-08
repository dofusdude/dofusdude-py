# MappedEntityCollectionSuperAreasInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
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


