# vela.WebhookApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hook**](WebhookApi.md#create_hook) | **POST** /api/v1/hooks/{org}/{repo} | 
[**update_hook**](WebhookApi.md#update_hook) | **PUT** /api/v1/hooks/{org}/{repo}/{hook} | 

# **create_hook**
> Webhook create_hook(body, org, repo)



Create a webhook for the configured backend

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = vela.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = vela.WebhookApi(vela.ApiClient(configuration))
body = vela.Webhook() # Webhook | Webhook payload that we expect from the user or VCS
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo

try:
    api_response = api_instance.create_hook(body, org, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)| Webhook payload that we expect from the user or VCS | 
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hook**
> Webhook update_hook(body, org, repo, hook)



Update a webhook for the configured backend

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = vela.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = vela.WebhookApi(vela.ApiClient(configuration))
body = vela.Webhook() # Webhook | Webhook payload that we expect from the user or VCS
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo
hook = 'hook_example' # str | Name of the org

try:
    api_response = api_instance.update_hook(body, org, repo, hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->update_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)| Webhook payload that we expect from the user or VCS | 
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 
 **hook** | **str**| Name of the org | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

