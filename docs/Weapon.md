# Weapon



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 
**is_weapon** | **bool** | always true when the item is a weapon. Many fields are now available. Always check for this flag first when getting single equipment items. | [optional] 
**level** | **int** |  | [optional] 
**pods** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**effects** | [**[EffectsEntry], none_type**](EffectsEntry.md) |  | [optional] 
**conditions** | [**[ConditionEntry], none_type**](ConditionEntry.md) |  | [optional] 
**critical_hit_probability** | **int** |  | [optional] 
**critical_hit_bonus** | **int** |  | [optional] 
**is_two_handed** | **bool** |  | [optional] 
**max_cast_per_turn** | **int** |  | [optional] 
**ap_cost** | **int** |  | [optional] 
**range** | [**WeaponRange**](WeaponRange.md) |  | [optional] 
**recipe** | [**[RecipeEntry], none_type**](RecipeEntry.md) |  | [optional] 
**parent_set** | [**EquipmentParentSet**](EquipmentParentSet.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


