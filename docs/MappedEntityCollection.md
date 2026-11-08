# MappedEntityCollection

The populated array property matches the selected resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classes** | [**List[MappedEntityCollectionClassesInner]**](MappedEntityCollectionClassesInner.md) |  | [optional] 
**spells** | [**List[MappedEntityCollectionSpellsInner]**](MappedEntityCollectionSpellsInner.md) |  | [optional] 
**monsters** | [**List[MappedEntityCollectionMonstersInner]**](MappedEntityCollectionMonstersInner.md) |  | [optional] 
**super_areas** | [**List[MappedEntityCollectionSuperAreasInner]**](MappedEntityCollectionSuperAreasInner.md) |  | [optional] 
**areas** | [**List[MappedEntityCollectionSuperAreasInner]**](MappedEntityCollectionSuperAreasInner.md) |  | [optional] 
**subareas** | [**List[MappedEntityCollectionSuperAreasInner]**](MappedEntityCollectionSuperAreasInner.md) |  | [optional] 
**links** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dofusdude.models.mapped_entity_collection import MappedEntityCollection

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityCollection from a JSON string
mapped_entity_collection_instance = MappedEntityCollection.from_json(json)
# print the JSON string representation of the object
print(MappedEntityCollection.to_json())

# convert the object into a dict
mapped_entity_collection_dict = mapped_entity_collection_instance.to_dict()
# create an instance of MappedEntityCollection from a dict
mapped_entity_collection_from_dict = MappedEntityCollection.from_dict(mapped_entity_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


