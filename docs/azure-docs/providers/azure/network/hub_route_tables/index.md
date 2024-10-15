---
title: hub_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - hub_route_tables
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

Creates, updates, deletes, gets or lists a <code>hub_route_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hub_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.hub_route_tables" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hub_route_tables', value: 'view', },
        { label: 'hub_route_tables', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="associated_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="propagating_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeTableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for RouteTable. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Retrieves the details of a RouteTable. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RouteTables. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Creates a RouteTable resource if it doesn't exist else updates the existing RouteTable. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId, virtualHubName" /> | Deletes a RouteTable. |

## `SELECT` examples

Retrieves the details of all RouteTables.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hub_route_tables', value: 'view', },
        { label: 'hub_route_tables', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
associated_connections,
etag,
labels,
propagating_connections,
provisioning_state,
resourceGroupName,
routeTableName,
routes,
subscriptionId,
type,
virtualHubName
FROM azure.network.vw_hub_route_tables
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
properties,
type
FROM azure.network.hub_route_tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hub_route_tables</code> resource.

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
INSERT INTO azure.network.hub_route_tables (
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
            - - name: name
                value: string
              - name: destinationType
                value: string
              - name: destinations
                value:
                  - string
              - name: nextHopType
                value: string
              - name: nextHop
                value: string
        - name: labels
          value:
            - string
        - name: associatedConnections
          value:
            - string
        - name: propagatingConnections
          value:
            - string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hub_route_tables</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.hub_route_tables
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeTableName = '{{ routeTableName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
