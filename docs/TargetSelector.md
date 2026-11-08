# TargetSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Human-readable target category or relationship. | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**negated** | **bool** |  | [optional] 
**reference** | [**CombatReference**](CombatReference.md) |  | [optional] 
**conditions** | [**List[CombatCondition]**](CombatCondition.md) |  | [optional] 

## Example

```python
from dofusdude.models.target_selector import TargetSelector

# TODO update the JSON string below
json = "{}"
# create an instance of TargetSelector from a JSON string
target_selector_instance = TargetSelector.from_json(json)
# print the JSON string representation of the object
print(TargetSelector.to_json())

# convert the object into a dict
target_selector_dict = target_selector_instance.to_dict()
# create an instance of TargetSelector from a dict
target_selector_from_dict = TargetSelector.from_dict(target_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


