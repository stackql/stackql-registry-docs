---
title: api_gateway_config_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateway_config_connections
  - api_management
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

Creates, updates, deletes, gets or lists a <code>api_gateway_config_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_gateway_config_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_gateway_config_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_gateway_config_connections', value: 'view', },
        { label: 'api_gateway_config_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the resource. |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostnames" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configConnectionName, gatewayName, resourceGroupName, subscriptionId" /> | Gets an API Management gateway config connection resource description. |
| <CopyableCode code="list_by_gateway" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | List all API Management gateway config connections within a gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configConnectionName, gatewayName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an API Management gateway config connection. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, configConnectionName, gatewayName, resourceGroupName, subscriptionId" /> | Deletes an existing API Management gateway config connection. |

## `SELECT` examples

List all API Management gateway config connections within a gateway.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_gateway_config_connections', value: 'view', },
        { label: 'api_gateway_config_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configConnectionName,
default_hostname,
etag,
gatewayName,
hostnames,
provisioning_state,
resourceGroupName,
source_id,
subscriptionId
FROM azure.api_management.vw_api_gateway_config_connections
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.api_management.api_gateway_config_connections
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_gateway_config_connections</code> resource.

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
INSERT INTO azure.api_management.api_gateway_config_connections (
configConnectionName,
gatewayName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ configConnectionName }}',
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
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
        - name: sourceId
          value: string
        - name: defaultHostname
          value: string
        - name: hostnames
          value:
            - string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_gateway_config_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_gateway_config_connections
WHERE If-Match = '{{ If-Match }}'
AND configConnectionName = '{{ configConnectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
