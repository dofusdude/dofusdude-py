# coding: utf-8

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude - [PHP](https://github.com/dofusdude/dofusdude-php)  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply donate to that cause, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).

    The version of the OpenAPI document: 0.8.1
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from dofusdude.models.get_game_search200_response_inner import GetGameSearch200ResponseInner
from dofusdude.models.items_list_entry_typed import ItemsListEntryTyped

from dofusdude.api_client import ApiClient, RequestSerialized
from dofusdude.api_response import ApiResponse
from dofusdude.rest import RESTResponseType


class GameApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_game_search(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="search query")],
        filter_type: Annotated[Optional[List[StrictStr]], Field(description="only results with all specific type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        fields_item: Annotated[Optional[List[StrictStr]], Field(description="adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[GetGameSearch200ResponseInner]:
        """Game Search

        Search in all names and descriptions of all supported types in the game. For the list of supported types see the endpoint /dofus2/meta/search/types.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: search query (required)
        :type query: str
        :param filter_type: only results with all specific type
        :type filter_type: List[str]
        :param limit: maximum number of returned results
        :type limit: int
        :param fields_item: adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.
        :type fields_item: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_game_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type=filter_type,
            limit=limit,
            fields_item=fields_item,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GetGameSearch200ResponseInner]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_game_search_with_http_info(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="search query")],
        filter_type: Annotated[Optional[List[StrictStr]], Field(description="only results with all specific type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        fields_item: Annotated[Optional[List[StrictStr]], Field(description="adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[GetGameSearch200ResponseInner]]:
        """Game Search

        Search in all names and descriptions of all supported types in the game. For the list of supported types see the endpoint /dofus2/meta/search/types.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: search query (required)
        :type query: str
        :param filter_type: only results with all specific type
        :type filter_type: List[str]
        :param limit: maximum number of returned results
        :type limit: int
        :param fields_item: adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.
        :type fields_item: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_game_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type=filter_type,
            limit=limit,
            fields_item=fields_item,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GetGameSearch200ResponseInner]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_game_search_without_preload_content(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="search query")],
        filter_type: Annotated[Optional[List[StrictStr]], Field(description="only results with all specific type")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        fields_item: Annotated[Optional[List[StrictStr]], Field(description="adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Game Search

        Search in all names and descriptions of all supported types in the game. For the list of supported types see the endpoint /dofus2/meta/search/types.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: search query (required)
        :type query: str
        :param filter_type: only results with all specific type
        :type filter_type: List[str]
        :param limit: maximum number of returned results
        :type limit: int
        :param fields_item: adds fields from the item search to the list entries if the hit is a item. Multiple comma separated values allowed.
        :type fields_item: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_game_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type=filter_type,
            limit=limit,
            fields_item=fields_item,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[GetGameSearch200ResponseInner]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_game_search_serialize(
        self,
        language,
        game,
        query,
        filter_type,
        limit,
        fields_item,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'filter[type]': 'csv',
            'fields[item]': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if language is not None:
            _path_params['language'] = language
        if game is not None:
            _path_params['game'] = game
        # process the query parameters
        if query is not None:
            
            _query_params.append(('query', query))
            
        if filter_type is not None:
            
            _query_params.append(('filter[type]', filter_type))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if fields_item is not None:
            
            _query_params.append(('fields[item]', fields_item))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/{game}/{language}/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_items_all_search(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="case sensitive search query")],
        filter_type_name: Annotated[Optional[StrictStr], Field(description="only results with the translated type name across all item_subtypes")] = None,
        filter_min_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or above this value")] = None,
        filter_max_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or below this value")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[ItemsListEntryTyped]:
        """Search All Items

        Search in all names and descriptions of Dofus items (including all subtypes) with a query.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: case sensitive search query (required)
        :type query: str
        :param filter_type_name: only results with the translated type name across all item_subtypes
        :type filter_type_name: str
        :param filter_min_level: only results which level is equal or above this value
        :type filter_min_level: int
        :param filter_max_level: only results which level is equal or below this value
        :type filter_max_level: int
        :param limit: maximum number of returned results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_items_all_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type_name=filter_type_name,
            filter_min_level=filter_min_level,
            filter_max_level=filter_max_level,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ItemsListEntryTyped]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_items_all_search_with_http_info(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="case sensitive search query")],
        filter_type_name: Annotated[Optional[StrictStr], Field(description="only results with the translated type name across all item_subtypes")] = None,
        filter_min_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or above this value")] = None,
        filter_max_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or below this value")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[ItemsListEntryTyped]]:
        """Search All Items

        Search in all names and descriptions of Dofus items (including all subtypes) with a query.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: case sensitive search query (required)
        :type query: str
        :param filter_type_name: only results with the translated type name across all item_subtypes
        :type filter_type_name: str
        :param filter_min_level: only results which level is equal or above this value
        :type filter_min_level: int
        :param filter_max_level: only results which level is equal or below this value
        :type filter_max_level: int
        :param limit: maximum number of returned results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_items_all_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type_name=filter_type_name,
            filter_min_level=filter_min_level,
            filter_max_level=filter_max_level,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ItemsListEntryTyped]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_items_all_search_without_preload_content(
        self,
        language: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="a valid language code")],
        game: StrictStr,
        query: Annotated[StrictStr, Field(description="case sensitive search query")],
        filter_type_name: Annotated[Optional[StrictStr], Field(description="only results with the translated type name across all item_subtypes")] = None,
        filter_min_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or above this value")] = None,
        filter_max_level: Annotated[Optional[Annotated[int, Field(le=200, strict=True, ge=0)]], Field(description="only results which level is equal or below this value")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="maximum number of returned results")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search All Items

        Search in all names and descriptions of Dofus items (including all subtypes) with a query.

        :param language: a valid language code (required)
        :type language: str
        :param game: (required)
        :type game: str
        :param query: case sensitive search query (required)
        :type query: str
        :param filter_type_name: only results with the translated type name across all item_subtypes
        :type filter_type_name: str
        :param filter_min_level: only results which level is equal or above this value
        :type filter_min_level: int
        :param filter_max_level: only results which level is equal or below this value
        :type filter_max_level: int
        :param limit: maximum number of returned results
        :type limit: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_items_all_search_serialize(
            language=language,
            game=game,
            query=query,
            filter_type_name=filter_type_name,
            filter_min_level=filter_min_level,
            filter_max_level=filter_max_level,
            limit=limit,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ItemsListEntryTyped]",
            '400': None,
            '404': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_items_all_search_serialize(
        self,
        language,
        game,
        query,
        filter_type_name,
        filter_min_level,
        filter_max_level,
        limit,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if language is not None:
            _path_params['language'] = language
        if game is not None:
            _path_params['game'] = game
        # process the query parameters
        if query is not None:
            
            _query_params.append(('query', query))
            
        if filter_type_name is not None:
            
            _query_params.append(('filter[type_name]', filter_type_name))
            
        if filter_min_level is not None:
            
            _query_params.append(('filter[min_level]', filter_min_level))
            
        if filter_max_level is not None:
            
            _query_params.append(('filter[max_level]', filter_max_level))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/{game}/{language}/items/search',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


