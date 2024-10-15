---
title: express_route_circuits
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits
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

Creates, updates, deletes, gets or lists a <code>express_route_circuits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuits', value: 'view', },
        { label: 'express_route_circuits', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="allow_classic_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="bandwidth_in_gbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuit_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_direct_port_rate_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_manager_etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="global_reach_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="peerings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provider_notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provider_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provider_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Contains SKU in an ExpressRouteCircuit. |
| <CopyableCode code="stag" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of ExpressRouteCircuit. |
| <CopyableCode code="sku" /> | `object` | Contains SKU in an ExpressRouteCircuit. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Gets information about the specified express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the express route circuits in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the express route circuits in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Creates or updates an express route circuit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Deletes the specified express route circuit. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Updates an express route circuit tags. |

## `SELECT` examples

Gets all the express route circuits in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuits', value: 'view', },
        { label: 'express_route_circuits', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_classic_operations,
authorization_key,
authorization_status,
authorizations,
bandwidth_in_gbps,
circuitName,
circuit_provisioning_state,
enable_direct_port_rate_limit,
etag,
express_route_port,
gateway_manager_etag,
global_reach_enabled,
location,
peerings,
provisioning_state,
resourceGroupName,
service_key,
service_provider_notes,
service_provider_properties,
service_provider_provisioning_state,
sku,
stag,
subscriptionId,
tags,
type
FROM azure.network.vw_express_route_circuits
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
tags,
type
FROM azure.network.express_route_circuits
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_circuits</code> resource.

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
INSERT INTO azure.network.express_route_circuits (
circuitName,
resourceGroupName,
subscriptionId,
sku,
properties,
id,
location,
tags
)
SELECT 
'{{ circuitName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: family
          value: string
    - name: properties
      value:
        - name: allowClassicOperations
          value: boolean
        - name: circuitProvisioningState
          value: string
        - name: serviceProviderProvisioningState
          value: []
        - name: authorizations
          value:
            - - name: properties
                value:
                  - name: authorizationKey
                    value: string
                  - name: authorizationUseStatus
                    value: string
                  - name: connectionResourceUri
                    value: string
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
        - name: peerings
          value:
            - - name: properties
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
        - name: serviceKey
          value: string
        - name: serviceProviderNotes
          value: string
        - name: serviceProviderProperties
          value:
            - name: serviceProviderName
              value: string
            - name: peeringLocation
              value: string
            - name: bandwidthInMbps
              value: integer
        - name: bandwidthInGbps
          value: number
        - name: stag
          value: integer
        - name: gatewayManagerEtag
          value: string
        - name: globalReachEnabled
          value: boolean
        - name: authorizationKey
          value: string
        - name: authorizationStatus
          value: string
        - name: enableDirectPortRateLimit
          value: boolean
    - name: etag
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

Deletes the specified <code>express_route_circuits</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_circuits
WHERE circuitName = '{{ circuitName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
