# Vela Python SDK

[![license](https://img.shields.io/crates/l/gl.svg)](LICENSE)

Python SDK for Vela (Target's official Pipeline Automation Framework)

> Vela is in active development and is a pre-release product.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.6.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

### pip install

You can install directly from Github

```sh
pip install git+https://github.com/go-vela/sdk-python.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/go-vela/sdk-python.git`)

Then import the package:

```python
import vela
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import vela
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import vela
from vela.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = vela.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Configure API endpoint
configuration.host = 'https://your-vela-server.example.com'

# create an instance of the API class
api_instance = vela.BuildsApi(vela.ApiClient(configuration))

try:
    api_response = api_instance.get_builds(org="go-vela",repo="sdk-python")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_builds: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to _http://localhost/api/v1_

| Class             | Method                                                                  | HTTP request                                                                 | Description                                             |
| ----------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------- |
| _AdminApi_        | [**admin_all_builds**](docs/AdminApi.md#admin_all_builds)               | **GET** /api/v1/admin/builds                                                 |
| _AdminApi_        | [**admin_all_deployments**](docs/AdminApi.md#admin_all_deployments)     | **GET** /api/v1/admin/deployments                                            |
| _AdminApi_        | [**admin_all_hooks**](docs/AdminApi.md#admin_all_hooks)                 | **GET** /api/v1/admin/hooks                                                  |
| _AdminApi_        | [**admin_all_repos**](docs/AdminApi.md#admin_all_repos)                 | **GET** /api/v1/admin/repos                                                  |
| _AdminApi_        | [**admin_all_secrets**](docs/AdminApi.md#admin_all_secrets)             | **GET** /api/v1/admin/secrets                                                |
| _AdminApi_        | [**admin_all_services**](docs/AdminApi.md#admin_all_services)           | **GET** /api/v1/admin/services                                               |
| _AdminApi_        | [**admin_all_steps**](docs/AdminApi.md#admin_all_steps)                 | **GET** /api/v1/admin/steps                                                  |
| _AdminApi_        | [**admin_all_users**](docs/AdminApi.md#admin_all_users)                 | **GET** /api/v1/admin/users                                                  |
| _AdminApi_        | [**admin_update_build**](docs/AdminApi.md#admin_update_build)           | **PUT** /api/v1/admin/build                                                  |
| _AdminApi_        | [**admin_update_deployment**](docs/AdminApi.md#admin_update_deployment) | **PUT** /api/v1/admin/deployment                                             |
| _AdminApi_        | [**admin_update_hook**](docs/AdminApi.md#admin_update_hook)             | **PUT** /api/v1/admin/hook                                                   |
| _AdminApi_        | [**admin_update_repo**](docs/AdminApi.md#admin_update_repo)             | **PUT** /api/v1/admin/repo                                                   |
| _AdminApi_        | [**admin_update_secret**](docs/AdminApi.md#admin_update_secret)         | **PUT** /api/v1/admin/secret                                                 |
| _AdminApi_        | [**admin_update_service**](docs/AdminApi.md#admin_update_service)       | **PUT** /api/v1/admin/service                                                |
| _AdminApi_        | [**admin_update_step**](docs/AdminApi.md#admin_update_step)             | **PUT** /api/v1/admin/step                                                   |
| _AdminApi_        | [**admin_update_user**](docs/AdminApi.md#admin_update_user)             | **PUT** /api/v1/admin/user                                                   |
| _AuthenticateApi_ | [**get_authenticate**](docs/AuthenticateApi.md#get_authenticate)        | **GET** /authenticate                                                        |
| _AuthenticateApi_ | [**get_login**](docs/AuthenticateApi.md#get_login)                      | **GET** /login                                                               |
| _AuthenticateApi_ | [**logout**](docs/AuthenticateApi.md#logout)                            | **GET** /logout                                                              |
| _AuthenticateApi_ | [**post_authenticate**](docs/AuthenticateApi.md#post_authenticate)      | **POST** /authenticate                                                       |
| _AuthenticateApi_ | [**post_login**](docs/AuthenticateApi.md#post_login)                    | **POST** /login                                                              |
| _BuildsApi_       | [**create_build**](docs/BuildsApi.md#create_build)                      | **POST** /api/v1/repos/{org}/{repo}/builds                                   |
| _BuildsApi_       | [**delete_build**](docs/BuildsApi.md#delete_build)                      | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}                         |
| _BuildsApi_       | [**get_build**](docs/BuildsApi.md#get_build)                            | **GET** /api/v1/repos/{org}/{repo}/builds/{build}                            |
| _BuildsApi_       | [**get_build_logs**](docs/BuildsApi.md#get_build_logs)                  | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/logs                       |
| _BuildsApi_       | [**get_builds**](docs/BuildsApi.md#get_builds)                          | **GET** /api/v1/repos/{org}/{repo}/builds                                    |
| _BuildsApi_       | [**get_org_builds**](docs/BuildsApi.md#get_org_builds)                  | **GET** /api/v1/repos/{org}                                                  |
| _BuildsApi_       | [**restart_build**](docs/BuildsApi.md#restart_build)                    | **POST** /api/v1/repos/{org}/{repo}/builds/{build}                           |
| _BuildsApi_       | [**update_build**](docs/BuildsApi.md#update_build)                      | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}                            |
| _DeploymentApi_   | [**create_deployment**](docs/DeploymentApi.md#create_deployment)        | **POST** /api/v1/deployments/{org}/{repo}                                    |
| _DeploymentApi_   | [**delete_hooks**](docs/DeploymentApi.md#delete_hooks)                  | **DELETE** /api/v1/hooks/{org}/{repo}/{hook}                                 |
| _DeploymentApi_   | [**get_deployment**](docs/DeploymentApi.md#get_deployment)              | **GET** /api/v1/deployments/{org}/{repo}/{deployment}                        |
| _DeploymentApi_   | [**get_deployments**](docs/DeploymentApi.md#get_deployments)            | **GET** /api/v1/deployments/{org}/{repo}                                     |
| _DeploymentApi_   | [**get_hook**](docs/DeploymentApi.md#get_hook)                          | **GET** /api/v1/hooks/{org}/{repo}/{hook}                                    |
| _DeploymentApi_   | [**get_hooks**](docs/DeploymentApi.md#get_hooks)                        | **GET** /api/v1/hooks/{org}/{repo}                                           |
| _PipelinesApi_    | [**compile_pipeline**](docs/PipelinesApi.md#compile_pipeline)           | **POST** /api/v1/pipelines/{org}/{repo}/compile                              |
| _PipelinesApi_    | [**expand_pipeline**](docs/PipelinesApi.md#expand_pipeline)             | **POST** /api/v1/pipelines/{org}/{repo}/expand                               |
| _PipelinesApi_    | [**get_pipeline**](docs/PipelinesApi.md#get_pipeline)                   | **GET** /api/v1/pipelines/{org}/{repo}                                       |
| _PipelinesApi_    | [**get_templates**](docs/PipelinesApi.md#get_templates)                 | **GET** /api/v1/pipelines/{org}/{repo}/templates                             |
| _PipelinesApi_    | [**validate_pipeline**](docs/PipelinesApi.md#validate_pipeline)         | **POST** /api/v1/pipelines/{org}/{repo}/validate                             |
| _ReposApi_        | [**chown_repo**](docs/ReposApi.md#chown_repo)                           | **PATCH** /api/v1/repos/{org}/{repo}/chown                                   |
| _ReposApi_        | [**create_repo**](docs/ReposApi.md#create_repo)                         | **POST** /api/v1/repos                                                       |
| _ReposApi_        | [**delete_repo**](docs/ReposApi.md#delete_repo)                         | **DELETE** /api/v1/repos/{org}/{repo}                                        |
| _ReposApi_        | [**get_repo**](docs/ReposApi.md#get_repo)                               | **GET** /api/v1/repos/{org}/{repo}                                           |
| _ReposApi_        | [**get_repos**](docs/ReposApi.md#get_repos)                             | **GET** /api/v1/repos                                                        |
| _ReposApi_        | [**repair_repo**](docs/ReposApi.md#repair_repo)                         | **PATCH** /api/v1/repos/{org}/{repo}/repair                                  |
| _ReposApi_        | [**update_repo**](docs/ReposApi.md#update_repo)                         | **PUT** /api/v1/repos/{org}/{repo}                                           |
| _RouterApi_       | [**base_metrics**](docs/RouterApi.md#base_metrics)                      | **GET** /metrics                                                             |
| _RouterApi_       | [**get_badge**](docs/RouterApi.md#get_badge)                            | **GET** /badge/{org}/{repo}/status.svg                                       |
| _RouterApi_       | [**health**](docs/RouterApi.md#health)                                  | **GET** /health                                                              |
| _RouterApi_       | [**post_webhook**](docs/RouterApi.md#post_webhook)                      | **POST** /webhook                                                            |
| _RouterApi_       | [**version**](docs/RouterApi.md#version)                                | **GET** /version                                                             |
| _SecretsApi_      | [**create_secret**](docs/SecretsApi.md#create_secret)                   | **POST** /api/v1/secrets/{engine}/{type}/{org}/{name}                        |
| _SecretsApi_      | [**delete_secret**](docs/SecretsApi.md#delete_secret)                   | **DELETE** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}             | Delete a secret from the configured backend.            |
| _SecretsApi_      | [**get_secret**](docs/SecretsApi.md#get_secret)                         | **GET** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}                | Retrieve a secret from the configured backend.          |
| _SecretsApi_      | [**get_secrets**](docs/SecretsApi.md#get_secrets)                       | **GET** /api/v1/secrets/{engine}/{type}/{org}/{name}                         | Retrieve a list of secrets from the configured backend. |
| _SecretsApi_      | [**update_secrets**](docs/SecretsApi.md#update_secrets)                 | **PUT** /api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}                | Update a secret from the configured backend.            |
| _ServicesApi_     | [**create_service**](docs/ServicesApi.md#create_service)                | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/services                  |
| _ServicesApi_     | [**create_service_logs**](docs/ServicesApi.md#create_service_logs)      | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs   |
| _ServicesApi_     | [**delete_service**](docs/ServicesApi.md#delete_service)                | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}      |
| _ServicesApi_     | [**delete_service_logs**](docs/ServicesApi.md#delete_service_logs)      | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs |
| _ServicesApi_     | [**get_service**](docs/ServicesApi.md#get_service)                      | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}         |
| _ServicesApi_     | [**get_service_logs**](docs/ServicesApi.md#get_service_logs)            | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs    |
| _ServicesApi_     | [**get_services**](docs/ServicesApi.md#get_services)                    | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/services                   |
| _ServicesApi_     | [**update_service**](docs/ServicesApi.md#update_service)                | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}         |
| _ServicesApi_     | [**update_service_log**](docs/ServicesApi.md#update_service_log)        | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/services/{service}/logs    |
| _StepsApi_        | [**create_step**](docs/StepsApi.md#create_step)                         | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/steps                     |
| _StepsApi_        | [**create_step_log**](docs/StepsApi.md#create_step_log)                 | **POST** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs         |
| _StepsApi_        | [**delete_step**](docs/StepsApi.md#delete_step)                         | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}            |
| _StepsApi_        | [**delete_step_log**](docs/StepsApi.md#delete_step_log)                 | **DELETE** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs       |
| _StepsApi_        | [**get_step**](docs/StepsApi.md#get_step)                               | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}               |
| _StepsApi_        | [**get_step_log**](docs/StepsApi.md#get_step_log)                       | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs          |
| _StepsApi_        | [**get_steps**](docs/StepsApi.md#get_steps)                             | **GET** /api/v1/repos/{org}/{repo}/builds/{build}/steps                      |
| _StepsApi_        | [**update_step**](docs/StepsApi.md#update_step)                         | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}               |
| _StepsApi_        | [**update_step_log**](docs/StepsApi.md#update_step_log)                 | **PUT** /api/v1/repos/{org}/{repo}/builds/{build}/steps/{step}/logs          |
| _UsersApi_        | [**create_token**](docs/UsersApi.md#create_token)                       | **POST** /api/v1/user/token                                                  |
| _UsersApi_        | [**create_user**](docs/UsersApi.md#create_user)                         | **POST** /api/v1/users                                                       |
| _UsersApi_        | [**delete_token**](docs/UsersApi.md#delete_token)                       | **DELETE** /api/v1/user/token                                                |
| _UsersApi_        | [**delete_user**](docs/UsersApi.md#delete_user)                         | **DELETE** /api/v1/users/{user}                                              |
| _UsersApi_        | [**get_current_user**](docs/UsersApi.md#get_current_user)               | **GET** /api/v1/user                                                         |
| _UsersApi_        | [**get_user**](docs/UsersApi.md#get_user)                               | **GET** /api/v1/users/{user}                                                 |
| _UsersApi_        | [**get_user_source_repos**](docs/UsersApi.md#get_user_source_repos)     | **GET** /api/v1/user/source/repos                                            |
| _UsersApi_        | [**get_users**](docs/UsersApi.md#get_users)                             | **GET** /api/v1/users                                                        |
| _UsersApi_        | [**update_current_user**](docs/UsersApi.md#update_current_user)         | **PUT** /api/v1/user                                                         |
| _UsersApi_        | [**update_user**](docs/UsersApi.md#update_user)                         | **PUT** /api/v1/users/{user}                                                 |
| _WebhookApi_      | [**create_hook**](docs/WebhookApi.md#create_hook)                       | **POST** /api/v1/hooks/{org}/{repo}                                          |
| _WebhookApi_      | [**update_hook**](docs/WebhookApi.md#update_hook)                       | **PUT** /api/v1/hooks/{org}/{repo}/{hook}                                    |
| _WorkersApi_      | [**create_worker**](docs/WorkersApi.md#create_worker)                   | **POST** /api/v1/workers                                                     |
| _WorkersApi_      | [**delete_worker**](docs/WorkersApi.md#delete_worker)                   | **DELETE** /api/v1/workers/{worker}                                          |
| _WorkersApi_      | [**get_worker**](docs/WorkersApi.md#get_worker)                         | **GET** /api/v1/workers/{worker}                                             |
| _WorkersApi_      | [**get_workers**](docs/WorkersApi.md#get_workers)                       | **GET** /api/v1/workers                                                      |
| _WorkersApi_      | [**update_worker**](docs/WorkersApi.md#update_worker)                   | **PUT** /api/v1/workers/{worker}                                             |

## Documentation For Models

- [Build](docs/Build.md)
- [Container](docs/Container.md)
- [ContainerSlice](docs/ContainerSlice.md)
- [Deployment](docs/Deployment.md)
- [Executor](docs/Executor.md)
- [Log](docs/Log.md)
- [Login](docs/Login.md)
- [PipelineBuild](docs/PipelineBuild.md)
- [PipelineMetadata](docs/PipelineMetadata.md)
- [PipelineWorker](docs/PipelineWorker.md)
- [Repo](docs/Repo.md)
- [Rules](docs/Rules.md)
- [Ruleset](docs/Ruleset.md)
- [Ruletype](docs/Ruletype.md)
- [Secret](docs/Secret.md)
- [SecretSlice](docs/SecretSlice.md)
- [Service](docs/Service.md)
- [Stage](docs/Stage.md)
- [StageSlice](docs/StageSlice.md)
- [Step](docs/Step.md)
- [StepSecret](docs/StepSecret.md)
- [StepSecretSlice](docs/StepSecretSlice.md)
- [Template](docs/Template.md)
- [Ulimit](docs/Ulimit.md)
- [UlimitSlice](docs/UlimitSlice.md)
- [User](docs/User.md)
- [Volume](docs/Volume.md)
- [VolumeSlice](docs/VolumeSlice.md)
- [Webhook](docs/Webhook.md)
- [Worker](docs/Worker.md)

## Documentation For Authorization

## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
- **Prefix**: `Bearer`

## Contributing

We are always welcome to new pull requests!

Please see our [contributing](.github/CONTRIBUTING.md) documentation for further instructions.

## Support

We are always here to help!

Please see our [support](.github/SUPPORT.md) documentation for further instructions.

## Copyright and License

```
Copyright (c) 2022 Target Brands, Inc.
```

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
