# vela.AuthenticateApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authenticate**](AuthenticateApi.md#get_authenticate) | **GET** /authenticate | 
[**get_login**](AuthenticateApi.md#get_login) | **GET** /login | 
[**logout**](AuthenticateApi.md#logout) | **GET** /logout | 
[**post_authenticate**](AuthenticateApi.md#post_authenticate) | **POST** /authenticate | 
[**post_login**](AuthenticateApi.md#post_login) | **POST** /login | 

# **get_authenticate**
> get_authenticate()



Start the OAuth flow with the Vela API

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AuthenticateApi()

try:
    api_instance.get_authenticate()
except ApiException as e:
    print("Exception when calling AuthenticateApi->get_authenticate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login**
> get_login()



Log into the Vela api

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AuthenticateApi()

try:
    api_instance.get_login()
except ApiException as e:
    print("Exception when calling AuthenticateApi->get_login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()



Log into the Vela api

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AuthenticateApi()

try:
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthenticateApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authenticate**
> str post_authenticate(body)



Complete the OAuth flow with the Vela API

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AuthenticateApi()
body = vela.Login() # Login | Payload containing login information

try:
    api_response = api_instance.post_authenticate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->post_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| Payload containing login information | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_login**
> Login post_login(body)



Login to the Vela api

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AuthenticateApi()
body = vela.Login() # Login | Login payload that we expect from the user

try:
    api_response = api_instance.post_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->post_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Login**](Login.md)| Login payload that we expect from the user | 

### Return type

[**Login**](Login.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

