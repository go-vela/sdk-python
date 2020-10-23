# vela.BuildsApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_build**](BuildsApi.md#create_build) | **POST** /api/v1/repos/{org}/{repo}/builds | 
[**delete_build**](BuildsApi.md#delete_build) | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build} | 
[**get_build**](BuildsApi.md#get_build) | **GET** /api/v1/repos/{org}/{repo}/builds/{build} | 
[**get_build_logs**](BuildsApi.md#get_build_logs) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/logs | 
[**get_builds**](BuildsApi.md#get_builds) | **GET** /api/v1/repos/{org}/{repo}/builds | 
[**get_org_builds**](BuildsApi.md#get_org_builds) | **GET** /api/v1/repos/{org} | 
[**restart_build**](BuildsApi.md#restart_build) | **POST** /api/v1/repos/{org}/{repo}/builds/{build} | 
[**update_build**](BuildsApi.md#update_build) | **PUT** /api/v1/repos/{org}/{repo}/builds/{build} | 

# **create_build**
> Build create_build(body, repo, org)



Create a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
body = vela.Build() # Build | Payload containing the build to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.create_build(body, repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->create_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Build**](Build.md)| Payload containing the build to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build**
> str delete_build(repo, org, build)



Delete a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number to restart

try:
    api_response = api_instance.delete_build(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->delete_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number to restart | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build**
> Build get_build(repo, org, build)



Get a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number to restart

try:
    api_response = api_instance.get_build(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number to restart | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_logs**
> Log get_build_logs(repo, org, build)



Get logs for a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number to restart

try:
    api_response = api_instance.get_build_logs(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number to restart | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> Build get_builds(repo, org)



Create a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.get_builds(repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_builds**
> Build get_org_builds(org, authorization)



Get a list of builds by org in the configured backend

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.BuildsApi()
org = 'org_example' # str | Name of the org
authorization = 'authorization_example' # str | Vela bearer token

try:
    api_response = api_instance.get_org_builds(org, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_org_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| Name of the org | 
 **authorization** | **str**| Vela bearer token | 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_build**
> Build restart_build(repo, org, build)



Restart a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number to restart

try:
    api_response = api_instance.restart_build(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->restart_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number to restart | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> Build update_build(body, repo, org, build)



Updates a build in the configured backend

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
api_instance = vela.BuildsApi(vela.ApiClient(configuration))
body = vela.Build() # Build | Payload containing the build to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number to restart

try:
    api_response = api_instance.update_build(body, repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->update_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Build**](Build.md)| Payload containing the build to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number to restart | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

