# EligibilityNodeCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**int_value** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**kind** | **str** | Verified semantic requirement type, for example item_received_age or profession_level. | [optional] 
**unit** | **str** |  | [optional] 
**string_value** | **str** |  | [optional] 
**value_label** | **str** |  | [optional] 
**element** | [**EligibilityNodeConditionElement**](EligibilityNodeConditionElement.md) |  | [optional] 
**reference** | [**CombatReference**](CombatReference.md) |  | [optional] 
**secondary_reference** | [**CombatReference**](CombatReference.md) |  | [optional] 

## Example

```python
from dofusdude.models.eligibility_node_condition import EligibilityNodeCondition

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityNodeCondition from a JSON string
eligibility_node_condition_instance = EligibilityNodeCondition.from_json(json)
# print the JSON string representation of the object
print(EligibilityNodeCondition.to_json())

# convert the object into a dict
eligibility_node_condition_dict = eligibility_node_condition_instance.to_dict()
# create an instance of EligibilityNodeCondition from a dict
eligibility_node_condition_from_dict = EligibilityNodeCondition.from_dict(eligibility_node_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


