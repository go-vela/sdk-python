# vela.SecretsApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret**](SecretsApi.md#create_secret) | **POST** /api/v1/secrets/{engine}/{type}/{org}/{name} | 
[**delete_secret**](SecretsApi.md#delete_secret) | **DELETE** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret} | Delete a secret from the configured backend.
[**get_secret**](SecretsApi.md#get_secret) | **GET** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret} | Retrieve a secret from the configured backend.
[**get_secrets**](SecretsApi.md#get_secrets) | **GET** /api/v1/secrets/{engine}/{type}/{org}/{name} | Retrieve a list of secrets from the configured backend.
[**update_secrets**](SecretsApi.md#update_secrets) | **PUT** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret} | Update a secret from the configured backend.

# **create_secret**
> Secret create_secret(body, engine, org, type, name)



Create a secret

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
api_instance = vela.SecretsApi(vela.ApiClient(configuration))
body = vela.Secret() # Secret | Payload containing the secret to create
engine = 'engine_example' # str | Secret engine to create a secret in
org = 'org_example' # str | Name of the org
type = 'type_example' # str | Secret type to create. Options 'org', 'repo', or 'shared'
name = 'name_example' # str | Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret

try:
    api_response = api_instance.create_secret(body, engine, org, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Secret**](Secret.md)| Payload containing the secret to create | 
 **engine** | **str**| Secret engine to create a secret in | 
 **org** | **str**| Name of the org | 
 **type** | **str**| Secret type to create. Options &#x27;org&#x27;, &#x27;repo&#x27;, or &#x27;shared&#x27; | 
 **name** | **str**| Name of the repo if a repo secret, team name if a shared secret, or &#x27;*&#x27; if an org secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> str delete_secret(body, engine, org, type, name, secret)

Delete a secret from the configured backend.

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
api_instance = vela.SecretsApi(vela.ApiClient(configuration))
body = vela.Secret() # Secret | Payload containing secret to update
engine = 'engine_example' # str | Secret engine to create a secret in
org = 'org_example' # str | Name of the org
type = 'type_example' # str | Secret type to create. Options 'org', 'repo', or 'shared'
name = 'name_example' # str | Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret
secret = 'secret_example' # str | Name of the secret

try:
    # Delete a secret from the configured backend.
    api_response = api_instance.delete_secret(body, engine, org, type, name, secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Secret**](Secret.md)| Payload containing secret to update | 
 **engine** | **str**| Secret engine to create a secret in | 
 **org** | **str**| Name of the org | 
 **type** | **str**| Secret type to create. Options &#x27;org&#x27;, &#x27;repo&#x27;, or &#x27;shared&#x27; | 
 **name** | **str**| Name of the repo if a repo secret, team name if a shared secret, or &#x27;*&#x27; if an org secret | 
 **secret** | **str**| Name of the secret | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret**
> Secret get_secret(engine, org, type, name, secret)

Retrieve a secret from the configured backend.

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
api_instance = vela.SecretsApi(vela.ApiClient(configuration))
engine = 'engine_example' # str | Secret engine to create a secret in
org = 'org_example' # str | Name of the org
type = 'type_example' # str | Secret type to create. Options 'org', 'repo', or 'shared'
name = 'name_example' # str | Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret
secret = 'secret_example' # str | Name of the secret

try:
    # Retrieve a secret from the configured backend.
    api_response = api_instance.get_secret(engine, org, type, name, secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->get_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **str**| Secret engine to create a secret in | 
 **org** | **str**| Name of the org | 
 **type** | **str**| Secret type to create. Options &#x27;org&#x27;, &#x27;repo&#x27;, or &#x27;shared&#x27; | 
 **name** | **str**| Name of the repo if a repo secret, team name if a shared secret, or &#x27;*&#x27; if an org secret | 
 **secret** | **str**| Name of the secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secrets**
> Secret get_secrets(engine, org, type, name)

Retrieve a list of secrets from the configured backend.

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
api_instance = vela.SecretsApi(vela.ApiClient(configuration))
engine = 'engine_example' # str | Secret engine to create a secret in
org = 'org_example' # str | Name of the org
type = 'type_example' # str | Secret type to create. Options 'org', 'repo', or 'shared'
name = 'name_example' # str | Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret

try:
    # Retrieve a list of secrets from the configured backend.
    api_response = api_instance.get_secrets(engine, org, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->get_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine** | **str**| Secret engine to create a secret in | 
 **org** | **str**| Name of the org | 
 **type** | **str**| Secret type to create. Options &#x27;org&#x27;, &#x27;repo&#x27;, or &#x27;shared&#x27; | 
 **name** | **str**| Name of the repo if a repo secret, team name if a shared secret, or &#x27;*&#x27; if an org secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secrets**
> Secret update_secrets(body, engine, org, type, name, secret)

Update a secret from the configured backend.

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
api_instance = vela.SecretsApi(vela.ApiClient(configuration))
body = vela.Secret() # Secret | Payload containing the secret to create
engine = 'engine_example' # str | Secret engine to create a secret in
org = 'org_example' # str | Name of the org
type = 'type_example' # str | Secret type to create. Options 'org', 'repo', or 'shared'
name = 'name_example' # str | Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret
secret = 'secret_example' # str | Name of the secret

try:
    # Update a secret from the configured backend.
    api_response = api_instance.update_secrets(body, engine, org, type, name, secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->update_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Secret**](Secret.md)| Payload containing the secret to create | 
 **engine** | **str**| Secret engine to create a secret in | 
 **org** | **str**| Name of the org | 
 **type** | **str**| Secret type to create. Options &#x27;org&#x27;, &#x27;repo&#x27;, or &#x27;shared&#x27; | 
 **name** | **str**| Name of the repo if a repo secret, team name if a shared secret, or &#x27;*&#x27; if an org secret | 
 **secret** | **str**| Name of the secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

