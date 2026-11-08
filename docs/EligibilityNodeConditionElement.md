# EligibilityNodeConditionElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Existing persisted item-condition element ID, or -1 for a condition without a persisted ID. | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.eligibility_node_condition_element import EligibilityNodeConditionElement

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityNodeConditionElement from a JSON string
eligibility_node_condition_element_instance = EligibilityNodeConditionElement.from_json(json)
# print the JSON string representation of the object
print(EligibilityNodeConditionElement.to_json())

# convert the object into a dict
eligibility_node_condition_element_dict = eligibility_node_condition_element_instance.to_dict()
# create an instance of EligibilityNodeConditionElement from a dict
eligibility_node_condition_element_from_dict = EligibilityNodeConditionElement.from_dict(eligibility_node_condition_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


