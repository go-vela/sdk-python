# vela.DeploymentApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](DeploymentApi.md#create_deployment) | **POST** /api/v1/deployments/{org}/{repo} | 
[**delete_hooks**](DeploymentApi.md#delete_hooks) | **DELETE** /api/v1/hooks/{org}/{repo}/{hook} | 
[**get_deployment**](DeploymentApi.md#get_deployment) | **GET** /api/v1/deployments/{org}/{repo}/{deployment} | 
[**get_deployments**](DeploymentApi.md#get_deployments) | **GET** /api/v1/deployments/{org}/{repo} | 
[**get_hook**](DeploymentApi.md#get_hook) | **GET** /api/v1/hooks/{org}/{repo}/{hook} | 
[**get_hooks**](DeploymentApi.md#get_hooks) | **GET** /api/v1/hooks/{org}/{repo} | 

# **create_deployment**
> Deployment create_deployment(org, repo)



Create a deployment for the configured backend

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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo

try:
    api_response = api_instance.create_deployment(org, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hooks**
> str delete_hooks(org, repo, hook)



Delete a webhook for the configured backend

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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo
hook = 'hook_example' # str | Name of the org

try:
    api_response = api_instance.delete_hooks(org, repo, hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->delete_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 
 **hook** | **str**| Name of the org | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> str get_deployment(org, repo, deployment)



Get a deployment from the configured backend

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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo
deployment = 'deployment_example' # str | Name of the org

try:
    api_response = api_instance.get_deployment(org, repo, deployment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 
 **deployment** | **str**| Name of the org | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> list[Deployment] get_deployments(org, repo)



Get a list of deployments for the configured backend

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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo

try:
    api_response = api_instance.get_deployments(org, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 

### Return type

[**list[Deployment]**](Deployment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> Webhook get_hook(org, repo, hook)



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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo
hook = 'hook_example' # str | Name of the org

try:
    api_response = api_instance.get_hook(org, repo, hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 
 **hook** | **str**| Name of the org | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hooks**
> list[Webhook] get_hooks(org, repo)



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
api_instance = vela.DeploymentApi(vela.ApiClient(configuration))
org = 'org_example' # str | Name of the org
repo = 'repo_example' # str | Name of the repo

try:
    api_response = api_instance.get_hooks(org, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentApi->get_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **repo** | **str**| Name of the repo | 

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

