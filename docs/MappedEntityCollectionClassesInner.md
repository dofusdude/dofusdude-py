# MappedEntityCollectionClassesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**description** | **str** |  | [optional] 
**gameplay_description** | **str** |  | [optional] 
**complexity** | **int** |  | [optional] 
**sort_index** | **int** |  | [optional] 
**creature_bones_id** | **int** |  | [optional] 
**roles** | **List[Dict[str, object]]** |  | [optional] 
**characteristic_costs** | **Dict[str, List[ClassCharacteristicCostsValueInner]]** | Characteristic point-cost tiers keyed by characteristic name. | [optional] 
**looks** | [**ClassLooks**](ClassLooks.md) |  | 
**spells** | [**List[Spell]**](Spell.md) | Fully mapped class spells, including levels, effects, targeting, and zones. | 

## Example

```python
from dofusdude.models.mapped_entity_collection_classes_inner import MappedEntityCollectionClassesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MappedEntityCollectionClassesInner from a JSON string
mapped_entity_collection_classes_inner_instance = MappedEntityCollectionClassesInner.from_json(json)
# print the JSON string representation of the object
print(MappedEntityCollectionClassesInner.to_json())

# convert the object into a dict
mapped_entity_collection_classes_inner_dict = mapped_entity_collection_classes_inner_instance.to_dict()
# create an instance of MappedEntityCollectionClassesInner from a dict
mapped_entity_collection_classes_inner_from_dict = MappedEntityCollectionClassesInner.from_dict(mapped_entity_collection_classes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


