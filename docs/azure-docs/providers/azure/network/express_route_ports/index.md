---
title: express_route_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_ports
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

Creates, updates, deletes, gets or lists a <code>express_route_ports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_ports" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_ports', value: 'view', },
        { label: 'express_route_ports', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="allocation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="bandwidth_in_gbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuits" /> | `text` | field from the `properties` object |
| <CopyableCode code="encapsulation" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ether_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="expressRoutePortName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="mtu" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_bandwidth_in_gbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties specific to ExpressRoutePort resources. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Retrieves the requested ExpressRoutePort resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the ExpressRoutePort resources in the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the ExpressRoutePort resources in the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Creates or updates the specified ExpressRoutePort resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Deletes the specified ExpressRoutePort resource. |
| <CopyableCode code="generate_loa" /> | `EXEC` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId, data__customerName" /> | Generate a letter of authorization for the requested ExpressRoutePort resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Update ExpressRoutePort tags. |

## `SELECT` examples

List all the ExpressRoutePort resources in the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_ports', value: 'view', },
        { label: 'express_route_ports', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allocation_date,
bandwidth_in_gbps,
billing_type,
circuits,
encapsulation,
etag,
ether_type,
expressRoutePortName,
identity,
links,
location,
mtu,
peering_location,
provisioned_bandwidth_in_gbps,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
type
FROM azure.network.vw_express_route_ports
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
tags,
type
FROM azure.network.express_route_ports
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_ports</code> resource.

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
INSERT INTO azure.network.express_route_ports (
expressRoutePortName,
resourceGroupName,
subscriptionId,
properties,
identity,
id,
location,
tags
)
SELECT 
'{{ expressRoutePortName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: peeringLocation
          value: string
        - name: bandwidthInGbps
          value: integer
        - name: provisionedBandwidthInGbps
          value: number
        - name: mtu
          value: string
        - name: encapsulation
          value: string
        - name: etherType
          value: string
        - name: allocationDate
          value: string
        - name: links
          value:
            - - name: properties
                value:
                  - name: routerName
                    value: string
                  - name: interfaceName
                    value: string
                  - name: patchPanelId
                    value: string
                  - name: rackId
                    value: string
                  - name: coloLocation
                    value: string
                  - name: connectorType
                    value: string
                  - name: adminState
                    value: string
                  - name: provisioningState
                    value: []
                  - name: macSecConfig
                    value:
                      - name: cknSecretIdentifier
                        value: string
                      - name: cakSecretIdentifier
                        value: string
                      - name: cipher
                        value: string
                      - name: sciState
                        value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: circuits
          value:
            - - name: id
                value: string
        - name: resourceGuid
          value: string
        - name: billingType
          value: string
    - name: etag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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

Deletes the specified <code>express_route_ports</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_ports
WHERE expressRoutePortName = '{{ expressRoutePortName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
