---
title: express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_connections
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

Creates, updates, deletes, gets or lists a <code>express_route_circuit_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_connections', value: 'view', },
        { label: 'express_route_circuit_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuit_connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_circuit_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_circuit_connection_config" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of the express route circuit connection. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Gets the specified Express Route Circuit Connection from the specified express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Gets all global reach connections associated with a private peering in an express route circuit. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Creates or updates a Express Route Circuit Connection in the specified express route circuits. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Deletes the specified Express Route Circuit Connection from the specified express route circuit. |

## `SELECT` examples

Gets all global reach connections associated with a private peering in an express route circuit.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_connections', value: 'view', },
        { label: 'express_route_circuit_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
authorization_key,
circuitName,
circuit_connection_status,
connectionName,
etag,
express_route_circuit_peering,
ipv6_circuit_connection_config,
peer_express_route_circuit_peering,
peeringName,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_express_route_circuit_connections
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
FROM azure.network.express_route_circuit_connections
WHERE circuitName = '{{ circuitName }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_circuit_connections</code> resource.

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
INSERT INTO azure.network.express_route_circuit_connections (
circuitName,
connectionName,
peeringName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ circuitName }}',
'{{ connectionName }}',
'{{ peeringName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: expressRouteCircuitPeering
          value:
            - name: id
              value: string
        - name: addressPrefix
          value: string
        - name: authorizationKey
          value: string
        - name: ipv6CircuitConnectionConfig
          value:
            - name: addressPrefix
              value: string
            - name: circuitConnectionStatus
              value: []
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>express_route_circuit_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_circuit_connections
WHERE circuitName = '{{ circuitName }}'
AND connectionName = '{{ connectionName }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
