# EligibilityNode

Client-side conditions using the v1 condition-node structure. Confirmed server-owned predicates are excluded during mapping. This is not the complete server eligibility formula, and the API does not dynamically remove fields based on interpretation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** |  | [optional] 
**relation** | **str** |  | [optional] 
**children** | [**List[EligibilityNode]**](EligibilityNode.md) |  | [optional] 
**condition** | [**EligibilityNodeCondition**](EligibilityNodeCondition.md) |  | [optional] 

## Example

```python
from dofusdude.models.eligibility_node import EligibilityNode

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityNode from a JSON string
eligibility_node_instance = EligibilityNode.from_json(json)
# print the JSON string representation of the object
print(EligibilityNode.to_json())

# convert the object into a dict
eligibility_node_dict = eligibility_node_instance.to_dict()
# create an instance of EligibilityNode from a dict
eligibility_node_from_dict = EligibilityNode.from_dict(eligibility_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


