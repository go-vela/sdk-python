# vela.StepsApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_step**](StepsApi.md#create_step) | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/steps | 
[**create_step_log**](StepsApi.md#create_step_log) | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs | 
[**delete_step**](StepsApi.md#delete_step) | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step} | 
[**delete_step_log**](StepsApi.md#delete_step_log) | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs | 
[**get_step**](StepsApi.md#get_step) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step} | 
[**get_step_log**](StepsApi.md#get_step_log) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs | 
[**get_steps**](StepsApi.md#get_steps) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps | 
[**update_step**](StepsApi.md#update_step) | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step} | 
[**update_step_log**](StepsApi.md#update_step_log) | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs | 

# **create_step**
> Step create_step(body, repo, org, build)



Create a step for a build

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
body = vela.Step() # Step | Payload containing the step to create
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number

try:
    api_response = api_instance.create_step(body, repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->create_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Step**](Step.md)| Payload containing the step to create | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 

### Return type

[**Step**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_step_log**
> Log create_step_log(body, repo, org, build, step)



Create the logs for a step

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
body = vela.Log() # Log | Payload containing the log to create
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.create_step_log(body, repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->create_step_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Payload containing the log to create | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_step**
> str delete_step(repo, org, build, step)



Delete a step for a build

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.delete_step(repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->delete_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_step_log**
> str delete_step_log(repo, org, build, step)



Delete the logs for a step

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.delete_step_log(repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->delete_step_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step**
> Step get_step(repo, org, build, step)



Retrieve a step for a build

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.get_step(repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->get_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

[**Step**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_step_log**
> Log get_step_log(repo, org, build, step)



Retrieve the logs for a step

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.get_step_log(repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->get_step_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_steps**
> list[Step] get_steps(repo, org, build)



Retrieve a list of steps for a build

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number

try:
    api_response = api_instance.get_steps(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->get_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 

### Return type

[**list[Step]**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_step**
> Step update_step(body, repo, org, build, step)



Update a step for a build

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
body = vela.Step() # Step | Payload containing the step to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.update_step(body, repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->update_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Step**](Step.md)| Payload containing the step to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

[**Step**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_step_log**
> Log update_step_log(body, repo, org, build, step)



Update the logs for a step

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
api_instance = vela.StepsApi(vela.ApiClient(configuration))
body = vela.Log() # Log | Payload containing the log to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
step = 'step_example' # str | Build number

try:
    api_response = api_instance.update_step_log(body, repo, org, build, step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StepsApi->update_step_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Payload containing the log to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **step** | **str**| Build number | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

