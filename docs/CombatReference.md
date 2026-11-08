# CombatReference

A resolved game reference used by selectors, conditions, and triggers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.combat_reference import CombatReference

# TODO update the JSON string below
json = "{}"
# create an instance of CombatReference from a JSON string
combat_reference_instance = CombatReference.from_json(json)
# print the JSON string representation of the object
print(CombatReference.to_json())

# convert the object into a dict
combat_reference_dict = combat_reference_instance.to_dict()
# create an instance of CombatReference from a dict
combat_reference_from_dict = CombatReference.from_dict(combat_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


