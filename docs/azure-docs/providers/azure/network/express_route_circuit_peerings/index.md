---
title: express_route_circuit_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_peerings
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

Creates, updates, deletes, gets or lists a <code>express_route_circuit_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuit_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_peerings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_peerings', value: 'view', },
        { label: 'express_route_circuit_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="azure_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_manager_etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_peering_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="microsoft_peering_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peered_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_azure_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_peer_address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_azure_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_peer_address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="stats" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
| <CopyableCode code="vlan_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the express route circuit peering. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Gets the specified peering for the express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Gets all peerings in a specified express route circuit. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Creates or updates a peering in the specified express route circuits. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Deletes the specified peering from the specified express route circuit. |

## `SELECT` examples

Gets all peerings in a specified express route circuit.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_peerings', value: 'view', },
        { label: 'express_route_circuit_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azure_asn,
circuitName,
connections,
etag,
express_route_connection,
gateway_manager_etag,
ipv6_peering_config,
last_modified_by,
microsoft_peering_config,
peer_asn,
peered_connections,
peeringName,
peering_type,
primary_azure_port,
primary_peer_address_prefix,
provisioning_state,
resourceGroupName,
route_filter,
secondary_azure_port,
secondary_peer_address_prefix,
shared_key,
state,
stats,
subscriptionId,
type,
vlan_id
FROM azure.network.vw_express_route_circuit_peerings
WHERE circuitName = '{{ circuitName }}'
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
FROM azure.network.express_route_circuit_peerings
WHERE circuitName = '{{ circuitName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_circuit_peerings</code> resource.

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
INSERT INTO azure.network.express_route_circuit_peerings (
circuitName,
peeringName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ circuitName }}',
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
        - name: peeringType
          value: []
        - name: state
          value: []
        - name: azureASN
          value: integer
        - name: peerASN
          value: integer
        - name: primaryPeerAddressPrefix
          value: string
        - name: secondaryPeerAddressPrefix
          value: string
        - name: primaryAzurePort
          value: string
        - name: secondaryAzurePort
          value: string
        - name: sharedKey
          value: string
        - name: vlanId
          value: integer
        - name: microsoftPeeringConfig
          value:
            - name: advertisedPublicPrefixes
              value:
                - string
            - name: advertisedCommunities
              value:
                - string
            - name: advertisedPublicPrefixesState
              value: string
            - name: legacyMode
              value: integer
            - name: customerASN
              value: integer
            - name: routingRegistryName
              value: string
        - name: stats
          value:
            - name: primarybytesIn
              value: integer
            - name: primarybytesOut
              value: integer
            - name: secondarybytesIn
              value: integer
            - name: secondarybytesOut
              value: integer
        - name: provisioningState
          value: []
        - name: gatewayManagerEtag
          value: string
        - name: lastModifiedBy
          value: string
        - name: routeFilter
          value:
            - name: id
              value: string
        - name: ipv6PeeringConfig
          value:
            - name: primaryPeerAddressPrefix
              value: string
            - name: secondaryPeerAddressPrefix
              value: string
            - name: state
              value: string
        - name: expressRouteConnection
          value:
            - name: id
              value: string
        - name: connections
          value:
            - - name: properties
                value:
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
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: peeredConnections
          value:
            - - name: properties
                value:
                  - name: addressPrefix
                    value: string
                  - name: connectionName
                    value: string
                  - name: authResourceGuid
                    value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
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

Deletes the specified <code>express_route_circuit_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_circuit_peerings
WHERE circuitName = '{{ circuitName }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
