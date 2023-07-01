# EffectsEntryType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_meta** | **bool** | true if a type is generated from the Api instead of Ankama. In that case, always prefer showing the templated string and omit everything else. The \&quot;name\&quot; field will have an english description of the meta type. An example for such effects are class sets effects. | [optional] 
**is_active** | **bool** | Affects target or source actively. | [optional] 

## Example

```python
from dofusdude.models.effects_entry_type import EffectsEntryType

# TODO update the JSON string below
json = "{}"
# create an instance of EffectsEntryType from a JSON string
effects_entry_type_instance = EffectsEntryType.from_json(json)
# print the JSON string representation of the object
print EffectsEntryType.to_json()

# convert the object into a dict
effects_entry_type_dict = effects_entry_type_instance.to_dict()
# create an instance of EffectsEntryType from a dict
effects_entry_type_form_dict = effects_entry_type.from_dict(effects_entry_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


