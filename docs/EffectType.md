# EffectType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** | Affects target or source actively. | [optional] 
**is_meta** | **bool** | true if a type is generated from the Api instead of Ankama. In that case, always prefer showing the templated string and omit everything else. The \&quot;name\&quot; field will have an english description of the meta type. An example for such effects are class sets effects. | [optional] 

## Example

```python
from dofusdude.models.effect_type import EffectType

# TODO update the JSON string below
json = "{}"
# create an instance of EffectType from a JSON string
effect_type_instance = EffectType.from_json(json)
# print the JSON string representation of the object
print(EffectType.to_json())

# convert the object into a dict
effect_type_dict = effect_type_instance.to_dict()
# create an instance of EffectType from a dict
effect_type_from_dict = EffectType.from_dict(effect_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


