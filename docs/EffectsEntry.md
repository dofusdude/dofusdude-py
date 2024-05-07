# EffectsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**int_minimum** | **int** | minimum int value, can be a single if ignore_int_max and no ignore_int_min | [optional] 
**int_maximum** | **int** | maximum int value, if not ignore_int_max and not ignore_int_min, the effect has a range value | [optional] 
**type** | [**SetEffectsEntryType**](SetEffectsEntryType.md) |  | [optional] 
**ignore_int_min** | **bool** | ignore the int min field because the actual value is a string. For readability the templated field is the only important field in this case.  | [optional] 
**ignore_int_max** | **bool** | ignore the int max field, if ignore_int_min is true, int min is a single value | [optional] 
**formatted** | **str** | all fields from above encoded in a single string | [optional] 

## Example

```python
from dofusdude.models.effects_entry import EffectsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EffectsEntry from a JSON string
effects_entry_instance = EffectsEntry.from_json(json)
# print the JSON string representation of the object
print(EffectsEntry.to_json())

# convert the object into a dict
effects_entry_dict = effects_entry_instance.to_dict()
# create an instance of EffectsEntry from a dict
effects_entry_from_dict = EffectsEntry.from_dict(effects_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


