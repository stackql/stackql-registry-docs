---
title: express_route_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_connections
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

Creates, updates, deletes, gets or lists a <code>express_route_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_connections', value: 'view', },
        { label: 'express_route_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_internet_security" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_private_link_fast_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="expressRouteGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="express_route_circuit_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="express_route_gateway_bypass" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_weight" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the ExpressRouteConnection subresource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified ExpressRouteConnection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Lists ExpressRouteConnections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId, data__name" /> | Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Deletes a connection to a ExpressRoute circuit. |

## `SELECT` examples

Lists ExpressRouteConnections.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_connections', value: 'view', },
        { label: 'express_route_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorization_key,
connectionName,
enable_internet_security,
enable_private_link_fast_path,
expressRouteGatewayName,
express_route_circuit_peering,
express_route_gateway_bypass,
provisioning_state,
resourceGroupName,
routing_configuration,
routing_weight,
subscriptionId
FROM azure.network.vw_express_route_connections
WHERE expressRouteGatewayName = '{{ expressRouteGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.network.express_route_connections
WHERE expressRouteGatewayName = '{{ expressRouteGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_connections</code> resource.

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
INSERT INTO azure.network.express_route_connections (
connectionName,
expressRouteGatewayName,
resourceGroupName,
subscriptionId,
data__name,
properties,
name,
id
)
SELECT 
'{{ connectionName }}',
'{{ expressRouteGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__name }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>express_route_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_connections
WHERE connectionName = '{{ connectionName }}'
AND expressRouteGatewayName = '{{ expressRouteGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
