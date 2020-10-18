# vela.AdminApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_all_builds**](AdminApi.md#admin_all_builds) | **GET** /api/v1/admin/builds | 
[**admin_all_deployments**](AdminApi.md#admin_all_deployments) | **GET** /api/v1/admin/deployments | 
[**admin_all_hooks**](AdminApi.md#admin_all_hooks) | **GET** /api/v1/admin/hooks | 
[**admin_all_repos**](AdminApi.md#admin_all_repos) | **GET** /api/v1/admin/repos | 
[**admin_all_secrets**](AdminApi.md#admin_all_secrets) | **GET** /api/v1/admin/secrets | 
[**admin_all_services**](AdminApi.md#admin_all_services) | **GET** /api/v1/admin/services | 
[**admin_all_steps**](AdminApi.md#admin_all_steps) | **GET** /api/v1/admin/steps | 
[**admin_all_users**](AdminApi.md#admin_all_users) | **GET** /api/v1/admin/users | 
[**admin_update_build**](AdminApi.md#admin_update_build) | **PUT** /api/v1/admin/build | 
[**admin_update_deployment**](AdminApi.md#admin_update_deployment) | **PUT** /api/v1/admin/deployment | 
[**admin_update_hook**](AdminApi.md#admin_update_hook) | **PUT** /api/v1/admin/hook | 
[**admin_update_repo**](AdminApi.md#admin_update_repo) | **PUT** /api/v1/admin/repo | 
[**admin_update_secret**](AdminApi.md#admin_update_secret) | **PUT** /api/v1/admin/secret | 
[**admin_update_service**](AdminApi.md#admin_update_service) | **PUT** /api/v1/admin/service | 
[**admin_update_step**](AdminApi.md#admin_update_step) | **PUT** /api/v1/admin/step | 
[**admin_update_user**](AdminApi.md#admin_update_user) | **PUT** /api/v1/admin/user | 

# **admin_all_builds**
> Build admin_all_builds()



Get all of the builds in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_builds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_builds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_deployments**
> admin_all_deployments()



Get all of the deployments in the database

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AdminApi()

try:
    api_instance.admin_all_deployments()
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_deployments: %s\n" % e)
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

# **admin_all_hooks**
> Webhook admin_all_hooks()



Get all of the webhooks stored in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_hooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_hooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_repos**
> Repo admin_all_repos()



Get all of the repos in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_repos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_repos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Repo**](Repo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_secrets**
> Secret admin_all_secrets()



Get all of the secrets in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_secrets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_secrets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_services**
> Service admin_all_services()



Get all of the services in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Service**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_steps**
> Step admin_all_steps()



Get all of the steps in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_steps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_steps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Step**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_all_users**
> User admin_all_users()



Get all of the users in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.admin_all_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_build**
> Build admin_update_build(body)



Update a build in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Build() # Build | Payload containing build to update

try:
    api_response = api_instance.admin_update_build(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Build**](Build.md)| Payload containing build to update | 

### Return type

[**Build**](Build.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_deployment**
> admin_update_deployment()



Get All

### Example
```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vela.AdminApi()

try:
    api_instance.admin_update_deployment()
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_deployment: %s\n" % e)
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

# **admin_update_hook**
> Webhook admin_update_hook(body)



Update a hook in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Webhook() # Webhook | Payload containing hook to update

try:
    api_response = api_instance.admin_update_hook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Webhook**](Webhook.md)| Payload containing hook to update | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_repo**
> Repo admin_update_repo(body)



Update a repo in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Repo() # Repo | Payload containing repo to update

try:
    api_response = api_instance.admin_update_repo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Repo**](Repo.md)| Payload containing repo to update | 

### Return type

[**Repo**](Repo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_secret**
> Secret admin_update_secret(body)



Update a secret in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Secret() # Secret | Payload containing secret to update

try:
    api_response = api_instance.admin_update_secret(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Secret**](Secret.md)| Payload containing secret to update | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_service**
> Service admin_update_service(body)



Update a hook in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Service() # Service | Payload containing service to update

try:
    api_response = api_instance.admin_update_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)| Payload containing service to update | 

### Return type

[**Service**](Service.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_step**
> Step admin_update_step(body)



Update a step in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.Step() # Step | Payload containing step to update

try:
    api_response = api_instance.admin_update_step(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Step**](Step.md)| Payload containing step to update | 

### Return type

[**Step**](Step.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_update_user**
> User admin_update_user(body)



Update a user in the database

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
api_instance = vela.AdminApi(vela.ApiClient(configuration))
body = vela.User() # User | Payload containing user to update

try:
    api_response = api_instance.admin_update_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| Payload containing user to update | 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

