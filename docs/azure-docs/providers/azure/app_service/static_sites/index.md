---
title: static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites
  - app_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>static_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_sites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_static_sites', value: 'view', },
        { label: 'static_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="allow_config_file_updates" /> | `text` | field from the `properties` object |
| <CopyableCode code="branch" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_distribution_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_domains" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="enterprise_grade_cdn_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity. |
| <CopyableCode code="key_vault_reference_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="linked_backends" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Description of a SKU for a scalable resource. |
| <CopyableCode code="staging_environment_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="template_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="user_provided_function_apps" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | A static site. |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the details of a static site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all Static Sites for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Deletes a static site. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
| <CopyableCode code="approve_or_reject_private_endpoint_connection" /> | `EXEC` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Approves or rejects a private endpoint connection |
| <CopyableCode code="detach_static_site" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Detaches a static site. |
| <CopyableCode code="detach_user_provided_function_app_from_static_site" /> | `EXEC` | <CopyableCode code="functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Detach the user provided function app from the static site |
| <CopyableCode code="detach_user_provided_function_app_from_static_site_build" /> | `EXEC` | <CopyableCode code="environmentName, functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Detach the user provided function app from the static site build |
| <CopyableCode code="link_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="link_backend_to_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="preview_workflow" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Description for Generates a preview workflow file for the static site |
| <CopyableCode code="register_user_provided_function_app_with_static_site" /> | `EXEC` | <CopyableCode code="functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Register a user provided function app with a static site |
| <CopyableCode code="register_user_provided_function_app_with_static_site_build" /> | `EXEC` | <CopyableCode code="environmentName, functionAppName, name, resourceGroupName, subscriptionId" /> | Description for Register a user provided function app with a static site build |
| <CopyableCode code="reset_static_site_api_key" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Resets the api key for an existing static site. |
| <CopyableCode code="unlink_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="unlink_backend_from_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_backend" /> | `EXEC` | <CopyableCode code="linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_backend_for_build" /> | `EXEC` | <CopyableCode code="environmentName, linkedBackendName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="validate_custom_domain_can_be_added_to_static_site" /> | `EXEC` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Validates a particular custom domain can be added to a static site. |

## `SELECT` examples

Description for Get all Static Sites for a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_static_sites', value: 'view', },
        { label: 'static_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_config_file_updates,
branch,
build_properties,
content_distribution_endpoint,
custom_domains,
database_connections,
default_hostname,
enterprise_grade_cdn_status,
identity,
key_vault_reference_identity,
kind,
linked_backends,
location,
private_endpoint_connections,
provider,
public_network_access,
repository_token,
repository_url,
resourceGroupName,
sku,
staging_environment_policy,
subscriptionId,
tags,
template_properties,
type,
user_provided_function_apps
FROM azure.app_service.vw_static_sites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
sku,
tags,
type
FROM azure.app_service.static_sites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>static_sites</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.app_service.static_sites (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties,
sku,
identity
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: defaultHostname
          value: string
        - name: repositoryUrl
          value: string
        - name: branch
          value: string
        - name: customDomains
          value:
            - string
        - name: repositoryToken
          value: string
        - name: buildProperties
          value:
            - name: appLocation
              value: string
            - name: apiLocation
              value: string
            - name: appArtifactLocation
              value: string
            - name: outputLocation
              value: string
            - name: appBuildCommand
              value: string
            - name: apiBuildCommand
              value: string
            - name: skipGithubActionWorkflowGeneration
              value: boolean
            - name: githubActionSecretNameOverride
              value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: location
                value: string
              - name: tags
                value: object
              - name: plan
                value:
                  - name: name
                    value: string
                  - name: publisher
                    value: string
                  - name: product
                    value: string
                  - name: promotionCode
                    value: string
                  - name: version
                    value: string
              - name: properties
                value:
                  - name: id
                    value: string
                  - name: name
                    value: string
                  - name: kind
                    value: string
                  - name: type
                    value: string
                  - name: properties
                    value:
                      - name: provisioningState
                        value: string
                      - name: privateEndpoint
                        value:
                          - name: id
                            value: string
                      - name: privateLinkServiceConnectionState
                        value:
                          - name: status
                            value: string
                          - name: description
                            value: string
                          - name: actionsRequired
                            value: string
                      - name: ipAddresses
                        value:
                          - string
              - name: sku
                value:
                  - name: name
                    value: string
                  - name: tier
                    value: string
                  - name: size
                    value: string
                  - name: family
                    value: string
                  - name: capacity
                    value: integer
                  - name: skuCapacity
                    value:
                      - name: minimum
                        value: integer
                      - name: maximum
                        value: integer
                      - name: elasticMaximum
                        value: integer
                      - name: default
                        value: integer
                      - name: scaleType
                        value: string
                  - name: locations
                    value:
                      - string
                  - name: capabilities
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                        - name: reason
                          value: string
              - name: status
                value: string
              - name: error
                value:
                  - name: extendedCode
                    value: string
                  - name: messageTemplate
                    value: string
                  - name: parameters
                    value:
                      - string
                  - name: innerErrors
                    value:
                      - - name: extendedCode
                          value: string
                        - name: messageTemplate
                          value: string
                        - name: parameters
                          value:
                            - string
                        - name: innerErrors
                          value:
                            - - name: extendedCode
                                value: string
                              - name: messageTemplate
                                value: string
                              - name: parameters
                                value:
                                  - string
                              - name: innerErrors
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: details
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: target
                                value: string
                              - name: code
                                value: string
                              - name: message
                                value: string
                        - name: details
                          value:
                            - - name: extendedCode
                                value: string
                              - name: messageTemplate
                                value: string
                              - name: parameters
                                value:
                                  - string
                              - name: innerErrors
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: details
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: target
                                value: string
                              - name: code
                                value: string
                              - name: message
                                value: string
                        - name: target
                          value: string
                        - name: code
                          value: string
                        - name: message
                          value: string
                  - name: details
                    value:
                      - - name: extendedCode
                          value: string
                        - name: messageTemplate
                          value: string
                        - name: parameters
                          value:
                            - string
                        - name: innerErrors
                          value:
                            - - name: extendedCode
                                value: string
                              - name: messageTemplate
                                value: string
                              - name: parameters
                                value:
                                  - string
                              - name: innerErrors
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: details
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: target
                                value: string
                              - name: code
                                value: string
                              - name: message
                                value: string
                        - name: details
                          value:
                            - - name: extendedCode
                                value: string
                              - name: messageTemplate
                                value: string
                              - name: parameters
                                value:
                                  - string
                              - name: innerErrors
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: details
                                value:
                                  - - name: extendedCode
                                      value: string
                                    - name: messageTemplate
                                      value: string
                                    - name: parameters
                                      value:
                                        - string
                                    - name: innerErrors
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: details
                                      value:
                                        - - name: extendedCode
                                            value: string
                                          - name: messageTemplate
                                            value: string
                                          - name: parameters
                                            value:
                                              - string
                                          - name: innerErrors
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: details
                                            value:
                                              - - name: extendedCode
                                                  value: string
                                                - name: messageTemplate
                                                  value: string
                                                - name: parameters
                                                  value:
                                                    - string
                                                - name: innerErrors
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: details
                                                  value:
                                                    - - name: extendedCode
                                                        value: string
                                                      - name: messageTemplate
                                                        value: string
                                                      - name: parameters
                                                        value:
                                                          - string
                                                      - name: innerErrors
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: details
                                                        value:
                                                          - - name: extendedCode
                                                              value: string
                                                            - name: messageTemplate
                                                              value: string
                                                            - name: parameters
                                                              value:
                                                                - string
                                                            - name: innerErrors
                                                              value:
                                                                - []
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: target
                                                              value: string
                                                            - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                      - name: target
                                                        value: string
                                                      - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                - name: target
                                                  value: string
                                                - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                          - name: target
                                            value: string
                                          - name: code
                                            value: string
                                          - name: message
                                            value: string
                                    - name: target
                                      value: string
                                    - name: code
                                      value: string
                                    - name: message
                                      value: string
                              - name: target
                                value: string
                              - name: code
                                value: string
                              - name: message
                                value: string
                        - name: target
                          value: string
                        - name: code
                          value: string
                        - name: message
                          value: string
                  - name: target
                    value: string
                  - name: code
                    value: string
                  - name: message
                    value: string
              - name: identity
                value:
                  - name: type
                    value: string
                  - name: tenantId
                    value: string
                  - name: principalId
                    value: string
                  - name: userAssignedIdentities
                    value: object
              - name: zones
                value:
                  - string
        - name: stagingEnvironmentPolicy
          value: string
        - name: allowConfigFileUpdates
          value: boolean
        - name: templateProperties
          value:
            - name: templateRepositoryUrl
              value: string
            - name: owner
              value: string
            - name: repositoryName
              value: string
            - name: description
              value: string
            - name: isPrivate
              value: boolean
        - name: contentDistributionEndpoint
          value: string
        - name: keyVaultReferenceIdentity
          value: string
        - name: userProvidedFunctionApps
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: kind
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: functionAppResourceId
                    value: string
                  - name: functionAppRegion
                    value: string
                  - name: createdOn
                    value: string
        - name: linkedBackends
          value:
            - - name: backendResourceId
                value: string
              - name: region
                value: string
              - name: createdOn
                value: string
              - name: provisioningState
                value: string
        - name: provider
          value: string
        - name: enterpriseGradeCdnStatus
          value: string
        - name: publicNetworkAccess
          value: string
        - name: databaseConnections
          value:
            - - name: resourceId
                value: string
              - name: connectionIdentity
                value: string
              - name: region
                value: string
              - name: configurationFiles
                value:
                  - - name: fileName
                      value: string
                    - name: contents
                      value: string
                    - name: type
                      value: string
              - name: name
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>static_sites</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.static_sites
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>static_sites</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.static_sites
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
