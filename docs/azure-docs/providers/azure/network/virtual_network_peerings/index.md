---
title: virtual_network_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_peerings
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

Creates, updates, deletes, gets or lists a <code>virtual_network_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_peerings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_peerings', value: 'view', },
        { label: 'virtual_network_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="allow_forwarded_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_gateway_transit" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_virtual_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="do_not_verify_remote_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_only_ipv6_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="local_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_subnet_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_virtual_network_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_complete_vnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_sync_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_bgp_communities" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_subnet_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_virtual_network_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_virtual_network_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="use_remote_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkPeeringName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the virtual network peering. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName" /> | Gets the specified virtual network peering. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Gets all virtual network peerings in a virtual network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName" /> | Creates or updates a peering in the specified virtual network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName" /> | Deletes the specified virtual network peering. |

## `SELECT` examples

Gets all virtual network peerings in a virtual network.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_peerings', value: 'view', },
        { label: 'virtual_network_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_forwarded_traffic,
allow_gateway_transit,
allow_virtual_network_access,
do_not_verify_remote_gateways,
enable_only_ipv6_peering,
etag,
local_address_space,
local_subnet_names,
local_virtual_network_address_space,
peer_complete_vnets,
peering_state,
peering_sync_level,
provisioning_state,
remote_address_space,
remote_bgp_communities,
remote_subnet_names,
remote_virtual_network,
remote_virtual_network_address_space,
remote_virtual_network_encryption,
resourceGroupName,
resource_guid,
subscriptionId,
type,
use_remote_gateways,
virtualNetworkName,
virtualNetworkPeeringName
FROM azure.network.vw_virtual_network_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
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
FROM azure.network.virtual_network_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_peerings</code> resource.

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
INSERT INTO azure.network.virtual_network_peerings (
resourceGroupName,
subscriptionId,
virtualNetworkName,
virtualNetworkPeeringName,
properties,
name,
type,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkName }}',
'{{ virtualNetworkPeeringName }}',
'{{ properties }}',
'{{ name }}',
'{{ type }}',
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
        - name: allowVirtualNetworkAccess
          value: boolean
        - name: allowForwardedTraffic
          value: boolean
        - name: allowGatewayTransit
          value: boolean
        - name: useRemoteGateways
          value: boolean
        - name: remoteVirtualNetwork
          value:
            - name: id
              value: string
        - name: localAddressSpace
          value:
            - name: addressPrefixes
              value:
                - string
        - name: remoteBgpCommunities
          value:
            - name: virtualNetworkCommunity
              value: string
            - name: regionalCommunity
              value: string
        - name: remoteVirtualNetworkEncryption
          value:
            - name: enabled
              value: boolean
            - name: enforcement
              value: string
        - name: peeringState
          value: string
        - name: peeringSyncLevel
          value: string
        - name: provisioningState
          value: []
        - name: doNotVerifyRemoteGateways
          value: boolean
        - name: resourceGuid
          value: string
        - name: peerCompleteVnets
          value: boolean
        - name: enableOnlyIPv6Peering
          value: boolean
        - name: localSubnetNames
          value:
            - string
        - name: remoteSubnetNames
          value:
            - string
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

Deletes the specified <code>virtual_network_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_network_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}'
AND virtualNetworkPeeringName = '{{ virtualNetworkPeeringName }}';
```
