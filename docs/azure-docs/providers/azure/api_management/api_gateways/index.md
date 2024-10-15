---
title: api_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateways
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

Creates, updates, deletes, gets or lists a <code>api_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_gateways', value: 'view', },
        { label: 'api_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="backend" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_api" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the resource. |
| <CopyableCode code="frontend" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | API Management gateway resource SKU properties. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| <CopyableCode code="virtual_network_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an API Management gateway resource description. |
| <CopyableCode code="sku" /> | `object` | API Management gateway resource SKU properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Gets an API Management gateway resource description. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all API Management gateways within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all API Management gateways within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Creates or updates an API Management gateway. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Deletes an existing API Management gateway. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Updates an existing API Management gateway. |

## `SELECT` examples

List all API Management gateways within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_gateways', value: 'view', },
        { label: 'api_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backend,
configuration_api,
created_at_utc,
etag,
frontend,
gatewayName,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
target_provisioning_state,
type,
virtual_network_type
FROM azure.api_management.vw_api_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.api_management.api_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_gateways</code> resource.

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
INSERT INTO azure.api_management.api_gateways (
gatewayName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
data__sku,
properties,
sku,
location,
tags
)
SELECT 
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}'
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
        - name: targetProvisioningState
          value: string
        - name: createdAtUtc
          value: string
        - name: frontend
          value:
            - name: defaultHostname
              value: string
        - name: backend
          value:
            - name: subnet
              value:
                - name: id
                  value: string
        - name: configurationApi
          value:
            - name: hostname
              value: string
        - name: virtualNetworkType
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: location
      value: string
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>api_gateways</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.api_gateways
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>api_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_gateways
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
