---
title: express_route_cross_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections
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

Creates, updates, deletes, gets or lists a <code>express_route_cross_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_cross_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_cross_connections', value: 'view', },
        { label: 'express_route_cross_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="bandwidth_in_mbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="crossConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_circuit" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="peering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="peerings" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_azure_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="s_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_azure_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provider_notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provider_provisioning_state" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of ExpressRouteCrossConnection. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="crossConnectionName, resourceGroupName, subscriptionId" /> | Gets details about the specified ExpressRouteCrossConnection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all the ExpressRouteCrossConnections in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the ExpressRouteCrossConnections in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="crossConnectionName, resourceGroupName, subscriptionId" /> | Update the specified ExpressRouteCrossConnection. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="crossConnectionName, resourceGroupName, subscriptionId" /> | Updates an express route cross connection tags. |

## `SELECT` examples

Retrieves all the ExpressRouteCrossConnections in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_cross_connections', value: 'view', },
        { label: 'express_route_cross_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bandwidth_in_mbps,
crossConnectionName,
etag,
express_route_circuit,
location,
peering_location,
peerings,
primary_azure_port,
provisioning_state,
resourceGroupName,
s_tag,
secondary_azure_port,
service_provider_notes,
service_provider_provisioning_state,
subscriptionId,
tags,
type
FROM azure.network.vw_express_route_cross_connections
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
tags,
type
FROM azure.network.express_route_cross_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_cross_connections</code> resource.

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
INSERT INTO azure.network.express_route_cross_connections (
crossConnectionName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ crossConnectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: primaryAzurePort
          value: string
        - name: secondaryAzurePort
          value: string
        - name: sTag
          value: integer
        - name: peeringLocation
          value: string
        - name: bandwidthInMbps
          value: integer
        - name: expressRouteCircuit
          value:
            - name: id
              value: string
        - name: serviceProviderProvisioningState
          value: []
        - name: serviceProviderNotes
          value: string
        - name: provisioningState
          value: []
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
                  - name: gatewayManagerEtag
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: ipv6PeeringConfig
                    value:
                      - name: primaryPeerAddressPrefix
                        value: string
                      - name: secondaryPeerAddressPrefix
                        value: string
                      - name: routeFilter
                        value:
                          - name: id
                            value: string
                      - name: state
                        value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
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
