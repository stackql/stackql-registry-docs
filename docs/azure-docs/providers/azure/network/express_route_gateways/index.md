---
title: express_route_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_gateways
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

Creates, updates, deletes, gets or lists a <code>express_route_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_gateways', value: 'view', },
        { label: 'express_route_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="allow_non_virtual_wan_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scale_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="expressRouteGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="express_route_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | ExpressRoute gateway resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Fetches the details of a ExpressRoute gateway in a resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists ExpressRoute gateways in a given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists ExpressRoute gateways under a given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Creates or updates a ExpressRoute gateway in a specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Updates express route gateway tags. |

## `SELECT` examples

Lists ExpressRoute gateways under a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_gateways', value: 'view', },
        { label: 'express_route_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_non_virtual_wan_traffic,
auto_scale_configuration,
etag,
expressRouteGatewayName,
express_route_connections,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
virtual_hub
FROM azure.network.vw_express_route_gateways
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
FROM azure.network.express_route_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_gateways</code> resource.

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
INSERT INTO azure.network.express_route_gateways (
expressRouteGatewayName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ expressRouteGatewayName }}',
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
        - name: autoScaleConfiguration
          value: string
        - name: expressRouteConnections
          value:
            - - name: properties
                value:
                  - name: provisioningState
                    value: []
                  - name: expressRouteCircuitPeering
                    value:
                      - name: id
                        value: string
                  - name: authorizationKey
                    value: string
                  - name: routingWeight
                    value: integer
                  - name: enableInternetSecurity
                    value: boolean
                  - name: expressRouteGatewayBypass
                    value: boolean
                  - name: enablePrivateLinkFastPath
                    value: boolean
                  - name: routingConfiguration
                    value:
                      - name: associatedRouteTable
                        value:
                          - name: id
                            value: string
                      - name: propagatedRouteTables
                        value:
                          - name: labels
                            value:
                              - string
                          - name: ids
                            value:
                              - - name: id
                                  value: string
                      - name: vnetRoutes
                        value:
                          - name: staticRoutesConfig
                            value:
                              - name: propagateStaticRoutes
                                value: boolean
                              - name: vnetLocalRouteOverrideCriteria
                                value: []
                          - name: staticRoutes
                            value:
                              - - name: name
                                  value: string
                                - name: addressPrefixes
                                  value:
                                    - string
                                - name: nextHopIpAddress
                                  value: string
                          - name: bgpConnections
                            value:
                              - - name: id
                                  value: string
              - name: name
                value: string
              - name: id
                value: string
        - name: virtualHub
          value:
            - name: id
              value: string
        - name: allowNonVirtualWanTraffic
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

Deletes the specified <code>express_route_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_gateways
WHERE expressRouteGatewayName = '{{ expressRouteGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
