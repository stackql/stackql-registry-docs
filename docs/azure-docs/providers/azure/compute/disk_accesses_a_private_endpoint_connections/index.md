---
title: disk_accesses_a_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses_a_private_endpoint_connections
  - compute
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

Creates, updates, deletes, gets or lists a <code>disk_accesses_a_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_accesses_a_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_accesses_a_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_accesses_a_private_endpoint_connections', value: 'view', },
        { label: 'disk_accesses_a_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | private endpoint connection Id |
| <CopyableCode code="name" /> | `text` | private endpoint connection name |
| <CopyableCode code="diskAccessName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | private endpoint connection type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | private endpoint connection Id |
| <CopyableCode code="name" /> | `string` | private endpoint connection name |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="type" /> | `string` | private endpoint connection type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets information about a private endpoint connection under a disk access resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection under a disk access resource. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approve or reject a private endpoint connection under disk access resource, this can't be used to create a new private endpoint connection. |

## `SELECT` examples

Gets information about a private endpoint connection under a disk access resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_accesses_a_private_endpoint_connections', value: 'view', },
        { label: 'disk_accesses_a_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
diskAccessName,
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.compute.vw_disk_accesses_a_private_endpoint_connections
WHERE diskAccessName = '{{ diskAccessName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.compute.disk_accesses_a_private_endpoint_connections
WHERE diskAccessName = '{{ diskAccessName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>disk_accesses_a_private_endpoint_connections</code> resource.

```sql
/*+ update */
REPLACE azure.compute.disk_accesses_a_private_endpoint_connections
SET 
properties = '{{ properties }}'
WHERE 
diskAccessName = '{{ diskAccessName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>disk_accesses_a_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.disk_accesses_a_private_endpoint_connections
WHERE diskAccessName = '{{ diskAccessName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
