# vela.WorkersApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /api/v1/workers | 
[**delete_worker**](WorkersApi.md#delete_worker) | **DELETE** /api/v1/workers/{worker} | 
[**get_worker**](WorkersApi.md#get_worker) | **GET** /api/v1/workers/{worker} | 
[**get_workers**](WorkersApi.md#get_workers) | **GET** /api/v1/workers | 
[**update_worker**](WorkersApi.md#update_worker) | **PUT** /api/v1/workers/{worker} | 

# **create_worker**
> Worker create_worker(body)



Create a worker for the configured backend

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
api_instance = vela.WorkersApi(vela.ApiClient(configuration))
body = vela.Worker() # Worker | Payload containing the worker to create

try:
    api_response = api_instance.create_worker(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->create_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Worker**](Worker.md)| Payload containing the worker to create | 

### Return type

[**Worker**](Worker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_worker**
> str delete_worker(worker)



Delete a worker for the configured backend

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
api_instance = vela.WorkersApi(vela.ApiClient(configuration))
worker = 'worker_example' # str | Name of the worker

try:
    api_response = api_instance.delete_worker(worker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->delete_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker** | **str**| Name of the worker | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker**
> Worker get_worker(worker)



Retrieve a worker for the configured backend

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
api_instance = vela.WorkersApi(vela.ApiClient(configuration))
worker = 'worker_example' # str | Hostname of the worker

try:
    api_response = api_instance.get_worker(worker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->get_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker** | **str**| Hostname of the worker | 

### Return type

[**Worker**](Worker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workers**
> list[Worker] get_workers(authorization)



Retrieve a list of workers for the configured backend

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.WorkersApi()
authorization = 'authorization_example' # str | Vela bearer token

try:
    api_response = api_instance.get_workers(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->get_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Vela bearer token | 

### Return type

[**list[Worker]**](Worker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_worker**
> Worker update_worker(body, worker)



Update a worker for the configured backend

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
api_instance = vela.WorkersApi(vela.ApiClient(configuration))
body = vela.Worker() # Worker | Payload containing the worker to update
worker = 'worker_example' # str | Name of the worker

try:
    api_response = api_instance.update_worker(body, worker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkersApi->update_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Worker**](Worker.md)| Payload containing the worker to update | 
 **worker** | **str**| Name of the worker | 

### Return type

[**Worker**](Worker.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

