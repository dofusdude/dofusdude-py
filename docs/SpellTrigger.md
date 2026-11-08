# SpellTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Resolved event that activates the effect. | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**reference** | [**CombatReference**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.spell_trigger import SpellTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of SpellTrigger from a JSON string
spell_trigger_instance = SpellTrigger.from_json(json)
# print the JSON string representation of the object
print(SpellTrigger.to_json())

# convert the object into a dict
spell_trigger_dict = spell_trigger_instance.to_dict()
# create an instance of SpellTrigger from a dict
spell_trigger_from_dict = SpellTrigger.from_dict(spell_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


