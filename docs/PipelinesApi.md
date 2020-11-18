# vela.PipelinesApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile_pipeline**](PipelinesApi.md#compile_pipeline) | **POST** /api/v1/pipelines/{org}/{repo}/compile | 
[**expand_pipeline**](PipelinesApi.md#expand_pipeline) | **POST** /api/v1/pipelines/{org}/{repo}/expand | 
[**get_pipeline**](PipelinesApi.md#get_pipeline) | **GET** /api/v1/pipelines/{org}/{repo} | 
[**get_templates**](PipelinesApi.md#get_templates) | **GET** /api/v1/pipelines/{org}/{repo}/templates | 
[**validate_pipeline**](PipelinesApi.md#validate_pipeline) | **POST** /api/v1/pipelines/{org}/{repo}/validate | 

# **compile_pipeline**
> PipelineBuild compile_pipeline(repo, org, ref=ref, output=output)



Get, expand and compile a pipeline configuration from the source provider

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
api_instance = vela.PipelinesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
ref = 'ref_example' # str | Ref for retrieving pipeline configuration file (optional)
output = 'output_example' # str | Output string for specifying output format (optional)

try:
    api_response = api_instance.compile_pipeline(repo, org, ref=ref, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->compile_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **ref** | **str**| Ref for retrieving pipeline configuration file | [optional] 
 **output** | **str**| Output string for specifying output format | [optional] 

### Return type

[**PipelineBuild**](PipelineBuild.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expand_pipeline**
> PipelineBuild expand_pipeline(repo, org, ref=ref, output=output)



Get and expand a pipeline configuration from the source provider

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
api_instance = vela.PipelinesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
ref = 'ref_example' # str | Ref for retrieving pipeline configuration file (optional)
output = 'output_example' # str | Output string for specifying output format (optional)

try:
    api_response = api_instance.expand_pipeline(repo, org, ref=ref, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->expand_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **ref** | **str**| Ref for retrieving pipeline configuration file | [optional] 
 **output** | **str**| Output string for specifying output format | [optional] 

### Return type

[**PipelineBuild**](PipelineBuild.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> PipelineBuild get_pipeline(repo, org, ref=ref, output=output)



Get a pipeline configuration from the source provider

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
api_instance = vela.PipelinesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
ref = 'ref_example' # str | Ref for retrieving pipeline configuration file (optional)
output = 'output_example' # str | Output string for specifying output format (optional)

try:
    api_response = api_instance.get_pipeline(repo, org, ref=ref, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **ref** | **str**| Ref for retrieving pipeline configuration file | [optional] 
 **output** | **str**| Output string for specifying output format | [optional] 

### Return type

[**PipelineBuild**](PipelineBuild.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> Template get_templates(repo, org, ref=ref, output=output)



Get a map of templates utilized by a pipeline configuration from the source provider

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
api_instance = vela.PipelinesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
ref = 'ref_example' # str | Ref for retrieving pipeline configuration file (optional)
output = 'output_example' # str | Output string for specifying output format (optional)

try:
    api_response = api_instance.get_templates(repo, org, ref=ref, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->get_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **ref** | **str**| Ref for retrieving pipeline configuration file | [optional] 
 **output** | **str**| Output string for specifying output format | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pipeline**
> str validate_pipeline(repo, org, ref=ref, output=output)



Get, expand and validate a pipeline configuration from the source provider

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
api_instance = vela.PipelinesApi(vela.ApiClient(configuration))
repo = 'repo_example' # str | Name of the repo
org = 'org_example' # str | Name of the org
ref = 'ref_example' # str | Ref for retrieving pipeline configuration file (optional)
output = 'output_example' # str | Output string for specifying output format (optional)

try:
    api_response = api_instance.validate_pipeline(repo, org, ref=ref, output=output)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PipelinesApi->validate_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Name of the repo | 
 **org** | **str**| Name of the org | 
 **ref** | **str**| Ref for retrieving pipeline configuration file | [optional] 
 **output** | **str**| Output string for specifying output format | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

