# ConditionTreeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;true\&quot; for the leaf of a tree | [optional] [default to True]
**relation** | **str** | \&quot;and\&quot;, \&quot;or\&quot; | [optional] [default to 'and']
**children** | [**List[ConditionTreeNode]**](ConditionTreeNode.md) |  | [optional] 
**condition** | [**ConditionEntry**](ConditionEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_tree_node import ConditionTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionTreeNode from a JSON string
condition_tree_node_instance = ConditionTreeNode.from_json(json)
# print the JSON string representation of the object
print(ConditionTreeNode.to_json())

# convert the object into a dict
condition_tree_node_dict = condition_tree_node_instance.to_dict()
# create an instance of ConditionTreeNode from a dict
condition_tree_node_from_dict = ConditionTreeNode.from_dict(condition_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


