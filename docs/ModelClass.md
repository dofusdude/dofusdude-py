# ModelClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**gameplay_description** | **str** |  | [optional] 
**complexity** | **int** |  | [optional] 
**sort_index** | **int** |  | [optional] 
**creature_bones_id** | **int** |  | [optional] 
**roles** | **List[Dict[str, object]]** |  | [optional] 
**characteristic_costs** | **Dict[str, List[ClassCharacteristicCostsValueInner]]** | Characteristic point-cost tiers keyed by characteristic name. | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**looks** | [**ClassLooks**](ClassLooks.md) |  | 
**spells** | [**List[Spell]**](Spell.md) | Fully mapped class spells, including levels, effects, targeting, and zones. | 

## Example

```python
from dofusdude.models.model_class import ModelClass

# TODO update the JSON string below
json = "{}"
# create an instance of ModelClass from a JSON string
model_class_instance = ModelClass.from_json(json)
# print the JSON string representation of the object
print(ModelClass.to_json())

# convert the object into a dict
model_class_dict = model_class_instance.to_dict()
# create an instance of ModelClass from a dict
model_class_from_dict = ModelClass.from_dict(model_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


