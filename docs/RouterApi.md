# vela.RouterApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**base_metrics**](RouterApi.md#base_metrics) | **GET** /metrics | 
[**get_badge**](RouterApi.md#get_badge) | **GET** /badge/{org}/{repo}/status.svg | 
[**health**](RouterApi.md#health) | **GET** /health | 
[**post_webhook**](RouterApi.md#post_webhook) | **POST** /webhook | 
[**version**](RouterApi.md#version) | **GET** /version | 

# **base_metrics**
> str base_metrics()



Retrieve metrics from the  Vela api

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.RouterApi()

try:
    api_response = api_instance.base_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouterApi->base_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_badge**
> str get_badge(org, repo)



Get a badge for the repo

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.RouterApi()
org = 'org_example' # str | Name of the org the repo belongs to
repo = 'repo_example' # str | Name of the repo to get the badge for

try:
    api_response = api_instance.get_badge(org, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouterApi->get_badge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org the repo belongs to | 
 **repo** | **str**| Name of the repo to get the badge for | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> str health()



Check if the Vela API is available

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.RouterApi()

try:
    api_response = api_instance.health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouterApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook**
> str post_webhook(body)



Deliver a webhook to the vela api

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.RouterApi()
body = vela.Webhook() # Webhook | Webhook payload that we expect from the user or VCS

try:
    api_response = api_instance.post_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouterApi->post_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)| Webhook payload that we expect from the user or VCS | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> str version()



Get the version of the Vela API

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.RouterApi()

try:
    api_response = api_instance.version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouterApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

