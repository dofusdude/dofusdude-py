# coding: utf-8

"""
    Dofusdude

    # A project for you - the developer. The free, always-up-to-date, low-latency, insert-buzzword-here Ankama API for your next cool project!  ## Client SDKs Don't write types or functions yourself - I already (kinda) did! 😉 - [Javascript](https://github.com/dofusdude/dofusdude-js) npm i dofusdude-js --save - [Typescript](https://github.com/dofusdude/dofusdude-ts) npm i dofusdude-ts --save - [Go](https://github.com/dofusdude/dodugo) go get -u github.com/dofusdude/dodugo - [Python](https://github.com/dofusdude/dofusdude-py) pip install dofusdude - [PHP](https://github.com/dofusdude/dofusdude-php)  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 2 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related Twitter, RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing by the powerful [Meilisearch](https://www.meilisearch.com) written in Rust.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering vector graphics into PNGs up to 800x800 px in the background.   ## Current state - Weapons ✅ - Equipment ✅ - Sets ✅ - Resources ✅ - Consumables ✅ - Pets ✅ - Mounts ✅ - Cosmetics/Ceremonial Items ✅ - Harnesses ✅ - Quest Items ✅ - Almanax ✅ - Monsters ❌ - Spells ❌  ... and much more on the Roadmap on my Discord.   ## Deploy now. Use forever. Everything you see here on this site, you can use now and forever. Updates could introduce new fields, new paths or parameter but never break backwards compatibility, so no field or parameter will be deleted.  There is one exception! **The API will _always_ choose being up-to-date over everything else**. So if Ankama decides to drop languages from the game like they did with their website, the API will loose support for them, too.  ## Only the beginning... 🤯 I want this project to be useful and not just add plain GET-categories no one needs.  There is a long list of features I want to add (see the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h)). But they are all focussed on you, the developers. So please let me know what you need. I will change the list based on demand.  # Get started! 🥳 Scroll down and try it for yourself!  Or see how these other awesome projects use it: - [KaellyBot](https://github.com/Kaysoro/KaellyBot) by Kaysoro - [Dofus Craftlist](https://dofuscraftlist-dev.netlify.app) by Lystina - [AlmanaxApp](https://almanaxapp.netlify.app) by Lystina - [DofuStuffSimulator](https://dofusstuffsimulator.netlify.app/)  I highly recommend using the SDKs for quick results. I use them myself for parts of the API.  ## Thank you! I highly welcome everyone on my [Discord](https://discord.gg/3EtHskZD8h) to just talk about projects and use cases or give feedback of any kind.  The servers have a fixed monthly cost to provide very fast responses. If you want to help me keeping them running or simply  donate, consider becoming a [GitHub Sponsor](https://github.com/sponsors/dofusdude).   # noqa: E501

    The version of the OpenAPI document: 0.7.2
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, conint, constr

from typing import List, Optional

from dofusdude.models.items_list_entry_typed import ItemsListEntryTyped

from dofusdude.api_client import ApiClient
from dofusdude.api_response import ApiResponse
from dofusdude.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AllItemsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_items_all_search(self, language : Annotated[constr(strict=True, max_length=2, min_length=2), Field(..., description="a valid language code")], game : StrictStr, query : Annotated[StrictStr, Field(..., description="case sensitive search query")], filter_type_name : Annotated[Optional[StrictStr], Field(description="only results with the translated type name across all item_subtypes")] = None, filter_min_level : Annotated[Optional[conint(strict=True, le=200, ge=0)], Field(description="only results which level is equal or above this value")] = None, filter_max_level : Annotated[Optional[conint(strict=True, le=200, ge=0)], Field(description="only results which level is equal or below this value")] = None, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="maximum number of returned results")] = None, **kwargs) -> List[ItemsListEntryTyped]:  # noqa: E501
        """Search All Items  # noqa: E501

        Search in all names and descriptions of Dofus items (including all subtypes) with a query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_items_all_search(language, game, query, filter_type_name, filter_min_level, filter_max_level, limit, async_req=True)
        >>> result = thread.get()

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
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ItemsListEntryTyped]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_items_all_search_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_items_all_search_with_http_info(language, game, query, filter_type_name, filter_min_level, filter_max_level, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_items_all_search_with_http_info(self, language : Annotated[constr(strict=True, max_length=2, min_length=2), Field(..., description="a valid language code")], game : StrictStr, query : Annotated[StrictStr, Field(..., description="case sensitive search query")], filter_type_name : Annotated[Optional[StrictStr], Field(description="only results with the translated type name across all item_subtypes")] = None, filter_min_level : Annotated[Optional[conint(strict=True, le=200, ge=0)], Field(description="only results which level is equal or above this value")] = None, filter_max_level : Annotated[Optional[conint(strict=True, le=200, ge=0)], Field(description="only results which level is equal or below this value")] = None, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="maximum number of returned results")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search All Items  # noqa: E501

        Search in all names and descriptions of Dofus items (including all subtypes) with a query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_items_all_search_with_http_info(language, game, query, filter_type_name, filter_min_level, filter_max_level, limit, async_req=True)
        >>> result = thread.get()

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
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[ItemsListEntryTyped], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'language',
            'game',
            'query',
            'filter_type_name',
            'filter_min_level',
            'filter_max_level',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_items_all_search" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['language']:
            _path_params['language'] = _params['language']

        if _params['game']:
            _path_params['game'] = _params['game']


        # process the query parameters
        _query_params = []
        if _params.get('query') is not None:  # noqa: E501
            _query_params.append(('query', _params['query']))

        if _params.get('filter_type_name') is not None:  # noqa: E501
            _query_params.append(('filter[type_name]', _params['filter_type_name']))

        if _params.get('filter_min_level') is not None:  # noqa: E501
            _query_params.append(('filter[min_level]', _params['filter_min_level']))

        if _params.get('filter_max_level') is not None:  # noqa: E501
            _query_params.append(('filter[max_level]', _params['filter_max_level']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "List[ItemsListEntryTyped]",
            '400': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/{game}/{language}/items/search', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
