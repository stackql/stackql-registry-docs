---
title: peer_express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_express_route_circuit_connections
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

Creates, updates, deletes, gets or lists a <code>peer_express_route_circuit_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peer_express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.peer_express_route_circuit_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peer_express_route_circuit_connections', value: 'view', },
        { label: 'peer_express_route_circuit_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="auth_resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuit_connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_circuit_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_express_route_circuit_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the peer express route circuit connection. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Gets the specified Peer Express Route Circuit Connection from the specified express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Gets all global reach peer connections associated with a private peering in an express route circuit. |

## `SELECT` examples

Gets all global reach peer connections associated with a private peering in an express route circuit.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peer_express_route_circuit_connections', value: 'view', },
        { label: 'peer_express_route_circuit_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
auth_resource_guid,
circuitName,
circuit_connection_status,
connectionName,
connection_name,
etag,
express_route_circuit_peering,
peer_express_route_circuit_peering,
peeringName,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_peer_express_route_circuit_connections
WHERE circuitName = '{{ circuitName }}'
AND peeringName = '{{ peeringName }}'
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
FROM azure.network.peer_express_route_circuit_connections
WHERE circuitName = '{{ circuitName }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

