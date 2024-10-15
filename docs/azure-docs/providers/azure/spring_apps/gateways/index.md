---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addon_configs" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_metadata_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="apm_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="apms" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_variables" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="response_cache_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="sso_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Spring Cloud Gateway properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Get the Spring Cloud Gateway and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Spring Cloud Gateway. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Restart the Spring Cloud Gateway. |
| <CopyableCode code="validate_domain" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId, data__name" /> | Check the domains are valid as well as not in use. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
addon_configs,
api_metadata_properties,
apm_types,
apms,
client_auth,
cors_properties,
environment_variables,
gatewayName,
https_only,
instances,
operator_properties,
provisioning_state,
public,
resourceGroupName,
resource_requests,
response_cache_properties,
serviceName,
sku,
sso_properties,
subscriptionId,
url
FROM azure.spring_apps.vw_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.spring_apps.gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateways</code> resource.

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
INSERT INTO azure.spring_apps.gateways (
gatewayName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
sku
)
SELECT 
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: public
          value: boolean
        - name: url
          value: string
        - name: httpsOnly
          value: boolean
        - name: ssoProperties
          value:
            - name: scope
              value:
                - string
            - name: clientId
              value: string
            - name: clientSecret
              value: string
            - name: issuerUri
              value: string
        - name: apiMetadataProperties
          value:
            - name: title
              value: string
            - name: description
              value: string
            - name: documentation
              value: string
            - name: version
              value: string
            - name: serverUrl
              value: string
        - name: corsProperties
          value:
            - name: allowedOrigins
              value:
                - string
            - name: allowedOriginPatterns
              value:
                - string
            - name: allowedMethods
              value:
                - string
            - name: allowedHeaders
              value:
                - string
            - name: maxAge
              value: integer
            - name: allowCredentials
              value: boolean
            - name: exposedHeaders
              value:
                - string
        - name: clientAuth
          value:
            - name: certificates
              value:
                - string
            - name: certificateVerification
              value: string
        - name: apmTypes
          value:
            - string
        - name: apms
          value: []
        - name: environmentVariables
          value:
            - name: properties
              value: object
            - name: secrets
              value: object
        - name: resourceRequests
          value:
            - name: cpu
              value: string
            - name: memory
              value: string
        - name: addonConfigs
          value: object
        - name: instances
          value:
            - - name: name
                value: string
              - name: status
                value: string
        - name: operatorProperties
          value:
            - name: resourceRequests
              value:
                - name: cpu
                  value: string
                - name: memory
                  value: string
                - name: instanceCount
                  value: integer
            - name: instances
              value:
                - - name: name
                    value: string
                  - name: status
                    value: string
        - name: responseCacheProperties
          value:
            - name: responseCacheType
              value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.gateways
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
