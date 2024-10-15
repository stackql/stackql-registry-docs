---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>managed_private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.managed_private_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdns" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_reserved" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedPrivateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedVirtualNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a managed private endpoint |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId" /> | Gets a managed private endpoint. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId" /> | Lists managed private endpoints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a managed private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, managedPrivateEndpointName, managedVirtualNetworkName, resourceGroupName, subscriptionId" /> | Deletes a managed private endpoint. |

## `SELECT` examples

Lists managed private endpoints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connection_state,
etag,
factoryName,
fqdns,
group_id,
is_reserved,
managedPrivateEndpointName,
managedVirtualNetworkName,
private_link_resource_id,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.data_factory.vw_managed_private_endpoints
WHERE factoryName = '{{ factoryName }}'
AND managedVirtualNetworkName = '{{ managedVirtualNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.data_factory.managed_private_endpoints
WHERE factoryName = '{{ factoryName }}'
AND managedVirtualNetworkName = '{{ managedVirtualNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_private_endpoints</code> resource.

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
INSERT INTO azure.data_factory.managed_private_endpoints (
factoryName,
managedPrivateEndpointName,
managedVirtualNetworkName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ factoryName }}',
'{{ managedPrivateEndpointName }}',
'{{ managedVirtualNetworkName }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: connectionState
          value:
            - name: actionsRequired
              value: string
            - name: description
              value: string
            - name: status
              value: string
        - name: fqdns
          value:
            - string
        - name: groupId
          value: string
        - name: isReserved
          value: boolean
        - name: privateLinkResourceId
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_private_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.managed_private_endpoints
WHERE factoryName = '{{ factoryName }}'
AND managedPrivateEndpointName = '{{ managedPrivateEndpointName }}'
AND managedVirtualNetworkName = '{{ managedVirtualNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
