# vela.ReposApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chown_repo**](ReposApi.md#chown_repo) | **PATCH** /api/v1/repos/{org}/{repo}/chown | 
[**create_repo**](ReposApi.md#create_repo) | **POST** /api/v1/repos | 
[**delete_repo**](ReposApi.md#delete_repo) | **DELETE** /api/v1/repos/{org}/{repo} | 
[**get_repo**](ReposApi.md#get_repo) | **GET** /api/v1/repos/{org}/{repo} | 
[**get_repos**](ReposApi.md#get_repos) | **GET** /api/v1/repos | 
[**repair_repo**](ReposApi.md#repair_repo) | **DELETE** /api/v1/repos/{org}/{repo}/repair | 
[**update_repo**](ReposApi.md#update_repo) | **PUT** /api/v1/repos/{org}/{repo} | 

# **chown_repo**
> str chown_repo(repo, org)



Remove and recreate the webhook for a repo

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.chown_repo(repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->chown_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo**
> Repo create_repo(body)



Create a repo in the configured backend

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
body = vela.Repo() # Repo | Payload containing the repo to create

try:
    api_response = api_instance.create_repo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->create_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Repo**](Repo.md)| Payload containing the repo to create | 

### Return type

[**Repo**](Repo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo**
> str delete_repo(repo, org)



Delete a repo in the configured backend

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.delete_repo(repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->delete_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repo**
> Repo get_repo(repo, org)



Get a repo in the configured backend

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.get_repo(repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->get_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

[**Repo**](Repo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repos**
> Repo get_repos()



Get all repos in the configured backend

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.get_repos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->get_repos: %s\n" % e)
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

# **repair_repo**
> str repair_repo(repo, org)



Remove and recreate the webhook for a repo

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.repair_repo(repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->repair_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo**
> Repo update_repo(body, repo, org)



Update a repo in the configured backend

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
api_instance = vela.ReposApi(vela.ApiClient(configuration))
body = vela.Repo() # Repo | Payload containing the repo to update
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org

try:
    api_response = api_instance.update_repo(body, repo, org)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReposApi->update_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Repo**](Repo.md)| Payload containing the repo to update | 
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 

### Return type

[**Repo**](Repo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

