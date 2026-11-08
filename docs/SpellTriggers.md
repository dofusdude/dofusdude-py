# SpellTriggers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** | Original trigger tokens retained for lossless debugging. | 
**logic** | **str** |  | [optional] 
**events** | [**List[SpellTrigger]**](SpellTrigger.md) |  | 

## Example

```python
from dofusdude.models.spell_triggers import SpellTriggers

# TODO update the JSON string below
json = "{}"
# create an instance of SpellTriggers from a JSON string
spell_triggers_instance = SpellTriggers.from_json(json)
# print the JSON string representation of the object
print(SpellTriggers.to_json())

# convert the object into a dict
spell_triggers_dict = spell_triggers_instance.to_dict()
# create an instance of SpellTriggers from a dict
spell_triggers_from_dict = SpellTriggers.from_dict(spell_triggers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


