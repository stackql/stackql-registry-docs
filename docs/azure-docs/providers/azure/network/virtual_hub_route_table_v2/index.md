---
title: virtual_hub_route_table_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_route_table_v2
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

Creates, updates, deletes, gets or lists a <code>virtual_hub_route_table_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hub_route_table_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_route_table_v2" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hub_route_table_v2', value: 'view', },
        { label: 'virtual_hub_route_table_v2', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="attached_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeTableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VirtualHubRouteTableV2. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Retrieves the details of a VirtualHubRouteTableV2. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all VirtualHubRouteTableV2s. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Creates a VirtualHubRouteTableV2 resource if it doesn't exist else updates the existing VirtualHubRouteTableV2. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Deletes a VirtualHubRouteTableV2. |

## `SELECT` examples

Retrieves the details of all VirtualHubRouteTableV2s.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hub_route_table_v2', value: 'view', },
        { label: 'virtual_hub_route_table_v2', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
attached_connections,
etag,
provisioning_state,
resourceGroupName,
routeTableName,
routes,
subscriptionId,
virtualHubName
FROM azure.network.vw_virtual_hub_route_table_v2
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties
FROM azure.network.virtual_hub_route_table_v2
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_hub_route_table_v2</code> resource.

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
INSERT INTO azure.network.virtual_hub_route_table_v2 (
resourceGroupName,
routeTableName,
subscriptionId,
virtualHubName,
properties,
name,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ routeTableName }}',
'{{ subscriptionId }}',
'{{ virtualHubName }}',
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
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_hub_route_table_v2</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_hub_route_table_v2
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeTableName = '{{ routeTableName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
