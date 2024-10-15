---
title: private_link_services_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_private_endpoint_connections
  - network
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

Creates, updates, deletes, gets or lists a <code>private_link_services_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_services_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_link_services_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_services_private_endpoint_connections', value: 'view', },
        { label: 'private_link_services_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="link_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="peConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Get the specific private end point connection by specific private link service in the resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all private end point connections for a specific private link service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Delete private end point connection for a private link service in a subscription. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Approve or reject private end point connection for a private link service in a subscription. |

## `SELECT` examples

Gets all private end point connections for a specific private link service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_services_private_endpoint_connections', value: 'view', },
        { label: 'private_link_services_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
link_identifier,
peConnectionName,
private_endpoint,
private_endpoint_location,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId,
type
FROM azure.network.vw_private_link_services_private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
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
FROM azure.network.private_link_services_private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>private_link_services_private_endpoint_connections</code> resource.

```sql
/*+ update */
REPLACE azure.network.private_link_services_private_endpoint_connections
SET 
properties = '{{ properties }}',
name = '{{ name }}',
id = '{{ id }}'
WHERE 
peConnectionName = '{{ peConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_link_services_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.private_link_services_private_endpoint_connections
WHERE peConnectionName = '{{ peConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
