---
title: route_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filters
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

Creates, updates, deletes, gets or lists a <code>route_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_filters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_filters', value: 'view', },
        { label: 'route_filters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ipv6_peerings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="peerings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeFilterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Route Filter Resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeFilterName, subscriptionId" /> | Gets the specified route filter. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all route filters in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all route filters in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeFilterName, subscriptionId, data__location" /> | Creates or updates a route filter in a specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeFilterName, subscriptionId" /> | Deletes the specified route filter. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, routeFilterName, subscriptionId" /> | Updates tags of a route filter. |

## `SELECT` examples

Gets all route filters in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_filters', value: 'view', },
        { label: 'route_filters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
ipv6_peerings,
location,
peerings,
provisioning_state,
resourceGroupName,
routeFilterName,
rules,
subscriptionId,
tags,
type
FROM azure.network.vw_route_filters
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
FROM azure.network.route_filters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route_filters</code> resource.

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
INSERT INTO azure.network.route_filters (
resourceGroupName,
routeFilterName,
subscriptionId,
data__location,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ routeFilterName }}',
'{{ subscriptionId }}',
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
        - name: rules
          value:
            - - name: properties
                value:
                  - name: access
                    value: []
                  - name: routeFilterRuleType
                    value: string
                  - name: communities
                    value:
                      - string
                  - name: provisioningState
                    value: []
              - name: name
                value: string
              - name: location
                value: string
              - name: etag
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
        - name: ipv6Peerings
          value:
            - - name: name
                value: string
              - name: etag
                value: string
              - name: type
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

## `DELETE` example

Deletes the specified <code>route_filters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.route_filters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeFilterName = '{{ routeFilterName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
