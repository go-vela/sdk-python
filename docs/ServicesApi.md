# vela.ServicesApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServicesApi.md#create_service) | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/services | 
[**create_service_logs**](ServicesApi.md#create_service_logs) | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs | 
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service} | 
[**delete_service_logs**](ServicesApi.md#delete_service_logs) | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs | 
[**get_service**](ServicesApi.md#get_service) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service} | 
[**get_service_logs**](ServicesApi.md#get_service_logs) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs | 
[**get_services**](ServicesApi.md#get_services) | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services | 
[**update_service**](ServicesApi.md#update_service) | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service} | 
[**update_service_log**](ServicesApi.md#update_service_log) | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs | 

# **create_service**
> Service create_service(body, repo, org, build)



Create a service for a build in the configured backend

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
body = vela.Service() # Service | Payload containing the service to create
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number

try:
    api_response = api_instance.create_service(body, repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->create_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)| Payload containing the service to create | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 

### Return type

[**Service**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_logs**
> Log create_service_logs(body, repo, org, build, service)



Create the logs for a service

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
body = vela.Log() # Log | Payload containing the log to create
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.create_service_logs(body, repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->create_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Payload containing the log to create | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> str delete_service(repo, org, build, service)



Delete a service for a build in the configured backend

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.delete_service(repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_logs**
> str delete_service_logs(repo, org, build, service)



Delete the logs for a service

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.delete_service_logs(repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->delete_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> Service get_service(repo, org, build, service)



Get a service for a build in the configured backend

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.get_service(repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

[**Service**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_logs**
> Log get_service_logs(repo, org, build, service)



Retrieve the logs for a service

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.get_service_logs(repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_service_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> list[Service] get_services(repo, org, build)



Get a list of all services for a build in the configured backend

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number

try:
    api_response = api_instance.get_services(repo, org, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 

### Return type

[**list[Service]**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> Service update_service(body, repo, org, build, service)



Update a service for a build in the configured backend

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
body = vela.Service() # Service | Payload containing the service to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.update_service(body, repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)| Payload containing the service to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

[**Service**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_log**
> Log update_service_log(body, repo, org, build, service)



Update the logs for a service

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
api_instance = vela.ServicesApi(vela.ApiClient(configuration))
body = vela.Log() # Log | Payload containing the log to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
build = 56 # int | Build number
service = 56 # int | Name of the service

try:
    api_response = api_instance.update_service_log(body, repo, org, build, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->update_service_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Payload containing the log to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **build** | **int**| Build number | 
 **service** | **int**| Name of the service | 

### Return type

[**Log**](Log.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

