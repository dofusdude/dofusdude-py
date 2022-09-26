# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from dofusdude import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dofusdude import schemas  # noqa: F401

from dofusdude.model.items_list_paged import ItemsListPaged

# query params


class SortLevelSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ASC(cls):
        return cls("asc")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("desc")
FilterTypeNameSchema = schemas.StrSchema
FilterMinLevelSchema = schemas.IntSchema


class FilterMaxLevelSchema(
    schemas.IntSchema
):
    pass


class PageSizeSchema(
    schemas.IntSchema
):
    pass


class PageNumberSchema(
    schemas.IntSchema
):
    pass


class FieldsItemSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def RECIPE(cls):
                return cls("recipe")
            
            @schemas.classproperty
            def DESCRIPTION(cls):
                return cls("description")
            
            @schemas.classproperty
            def CONDITIONS(cls):
                return cls("conditions")
            
            @schemas.classproperty
            def EFFECTS(cls):
                return cls("effects")
            
            @schemas.classproperty
            def IS_WEAPON(cls):
                return cls("is_weapon")
            
            @schemas.classproperty
            def PODS(cls):
                return cls("pods")
            
            @schemas.classproperty
            def PARENT_SET(cls):
                return cls("parent_set")
            
            @schemas.classproperty
            def CRITICAL_HIT_PROBABILITY(cls):
                return cls("critical_hit_probability")
            
            @schemas.classproperty
            def CRITICAL_HIT_BONUS(cls):
                return cls("critical_hit_bonus")
            
            @schemas.classproperty
            def IS_TWO_HANDED(cls):
                return cls("is_two_handed")
            
            @schemas.classproperty
            def MAX_CAST_PER_TURN(cls):
                return cls("max_cast_per_turn")
            
            @schemas.classproperty
            def AP_COST(cls):
                return cls("ap_cost")
            
            @schemas.classproperty
            def RANGE(cls):
                return cls("range")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsItemSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
# path params


class LanguageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def EN(cls):
        return cls("en")
    
    @schemas.classproperty
    def FR(cls):
        return cls("fr")
    
    @schemas.classproperty
    def DE(cls):
        return cls("de")
    
    @schemas.classproperty
    def IT(cls):
        return cls("it")
    
    @schemas.classproperty
    def ES(cls):
        return cls("es")
    
    @schemas.classproperty
    def PT(cls):
        return cls("pt")


class GameSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DOFUS2(cls):
        return cls("dofus2")
    
    @schemas.classproperty
    def DOFUS2BETA(cls):
        return cls("dofus2beta")
SchemaFor200ResponseBodyApplicationJson = ItemsListPaged
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_items_equipment_list_oapg(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        List Equipment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_language,
            request_path_game,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_sort_level,
            request_query_filter_type_name,
            request_query_filter_min_level,
            request_query_filter_max_level,
            request_query_page_size,
            request_query_page_number,
            request_query_fields_item,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class GetItemsEquipmentList(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_items_equipment_list(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_items_equipment_list_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._get_items_equipment_list_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


