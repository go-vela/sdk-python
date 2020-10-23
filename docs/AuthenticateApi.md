# vela.AuthenticateApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticateApi.md#authenticate) | **GET** /authenticate | 

# **authenticate**
> str authenticate(body)



Authenticate with the Vela API

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
    api_response = api_instance.authenticate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->authenticate: %s\n" % e)
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

