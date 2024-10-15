---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routes', value: 'view', },
        { label: 'routes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="has_bgp_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_hop_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_hop_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeTableName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Route resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Gets the specified route from a route table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId" /> | Gets all routes in a route table. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Creates or updates a route in the specified route table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Deletes the specified route from a route table. |

## `SELECT` examples

Gets all routes in a route table.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routes', value: 'view', },
        { label: 'routes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_prefix,
etag,
has_bgp_override,
next_hop_ip_address,
next_hop_type,
provisioning_state,
resourceGroupName,
routeName,
routeTableName,
subscriptionId,
type
FROM azure.network.vw_routes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeTableName = '{{ routeTableName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.routes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeTableName = '{{ routeTableName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routes</code> resource.

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
INSERT INTO azure.network.routes (
resourceGroupName,
routeName,
routeTableName,
subscriptionId,
properties,
name,
type,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ routeName }}',
'{{ routeTableName }}',
'{{ subscriptionId }}',
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
        - name: addressPrefix
          value: string
        - name: nextHopType
          value: []
        - name: nextHopIpAddress
          value: string
        - name: provisioningState
          value: []
        - name: hasBgpOverride
          value: boolean
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

Deletes the specified <code>routes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.routes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeName = '{{ routeName }}'
AND routeTableName = '{{ routeTableName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
