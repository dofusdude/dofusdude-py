# ConditionNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;true\&quot; for the leaf of a tree | [optional] [default to True]
**relation** | **str** | \&quot;and\&quot;, \&quot;or\&quot; | [optional] [default to 'and']
**children** | [**List[Optional[ConditionNode]]**](ConditionNode.md) |  | [optional] 
**condition** | [**Condition**](Condition.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_node import ConditionNode

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionNode from a JSON string
condition_node_instance = ConditionNode.from_json(json)
# print the JSON string representation of the object
print(ConditionNode.to_json())

# convert the object into a dict
condition_node_dict = condition_node_instance.to_dict()
# create an instance of ConditionNode from a dict
condition_node_from_dict = ConditionNode.from_dict(condition_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


