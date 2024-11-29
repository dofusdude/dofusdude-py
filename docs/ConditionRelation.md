# ConditionRelation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;false\&quot; for relations | [optional] [default to False]
**relation** | **str** | \&quot;and\&quot;, \&quot;or\&quot; | [optional] [default to 'and']
**children** | [**List[Optional[ConditionNode]]**](ConditionNode.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_relation import ConditionRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionRelation from a JSON string
condition_relation_instance = ConditionRelation.from_json(json)
# print the JSON string representation of the object
print(ConditionRelation.to_json())

# convert the object into a dict
condition_relation_dict = condition_relation_instance.to_dict()
# create an instance of ConditionRelation from a dict
condition_relation_from_dict = ConditionRelation.from_dict(condition_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


