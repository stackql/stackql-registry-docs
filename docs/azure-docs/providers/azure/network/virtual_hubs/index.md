---
title: virtual_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs
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

Creates, updates, deletes, gets or lists a <code>virtual_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hubs', value: 'view', },
        { label: 'virtual_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_branch_to_branch_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_firewall" /> | `text` | field from the `properties` object |
| <CopyableCode code="bgp_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_routing_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="p2_s_vpn_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_routing_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_maps" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_table" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_partner_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_provider_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_hub_route_table_v2s" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_router_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_router_auto_scale_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_router_ips" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_wan" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_gateway" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="kind" /> | `string` | Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for VirtualHub. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of a VirtualHub. |
| <CopyableCode code="get_inbound_routes" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Gets the inbound routes configured for the Virtual Hub on a particular connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the VirtualHubs in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the VirtualHubs in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName, data__location" /> | Creates a VirtualHub resource if it doesn't exist else updates the existing VirtualHub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Deletes a VirtualHub. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Updates VirtualHub tags. |

## `SELECT` examples

Lists all the VirtualHubs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hubs', value: 'view', },
        { label: 'virtual_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
allow_branch_to_branch_traffic,
azure_firewall,
bgp_connections,
etag,
express_route_gateway,
hub_routing_preference,
ip_configurations,
kind,
location,
p2_s_vpn_gateway,
preferred_routing_gateway,
provisioning_state,
resourceGroupName,
route_maps,
route_table,
routing_state,
security_partner_provider,
security_provider_name,
sku,
subscriptionId,
tags,
type,
virtualHubName,
virtual_hub_route_table_v2s,
virtual_router_asn,
virtual_router_auto_scale_configuration,
virtual_router_ips,
virtual_wan,
vpn_gateway
FROM azure.network.vw_virtual_hubs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
tags,
type
FROM azure.network.virtual_hubs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_hubs</code> resource.

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
INSERT INTO azure.network.virtual_hubs (
resourceGroupName,
subscriptionId,
virtualHubName,
data__location,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualHubName }}',
'{{ data__location }}',
'{{ properties }}',
'{{ id }}',
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
        - name: virtualWan
          value:
            - name: id
              value: string
        - name: addressPrefix
          value: string
        - name: routeTable
          value:
            - name: routes
              value:
                - - name: addressPrefixes
                    value:
                      - string
                  - name: nextHopIpAddress
                    value: string
        - name: provisioningState
          value: []
        - name: securityProviderName
          value: string
        - name: virtualHubRouteTableV2s
          value:
            - - name: properties
                value:
                  - name: routes
                    value:
                      - - name: destinationType
                          value: string
                        - name: destinations
                          value:
                            - string
                        - name: nextHopType
                          value: string
                        - name: nextHops
                          value:
                            - string
                  - name: attachedConnections
                    value:
                      - string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: sku
          value: string
        - name: routingState
          value: []
        - name: bgpConnections
          value:
            - - name: id
                value: string
        - name: ipConfigurations
          value:
            - - name: id
                value: string
        - name: routeMaps
          value:
            - - name: id
                value: string
        - name: virtualRouterAsn
          value: integer
        - name: virtualRouterIps
          value:
            - string
        - name: allowBranchToBranchTraffic
          value: boolean
        - name: preferredRoutingGateway
          value: []
        - name: hubRoutingPreference
          value: []
        - name: virtualRouterAutoScaleConfiguration
          value:
            - name: minCapacity
              value: integer
    - name: etag
      value: string
    - name: kind
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_hubs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
