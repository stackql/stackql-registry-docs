---
title: edge_gateway_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_gateway_pools
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>edge_gateway_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_gateway_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.edge_gateway_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_gateway_pools', value: 'view', },
        { label: 'edge_gateway_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="edgeGatewayPool" /> | `text` | field from the `properties` object |
| <CopyableCode code="edge_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_capacity_kilo_bits_per_second" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="gre_vip_subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="number_of_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="redundant_gateway_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | An object that contains the properties of an edge gateway pool. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="edgeGatewayPool, location, resourceGroupName, subscriptionId" /> | Returns the requested edge gateway pool object. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all edge gateway pool objects at a location. |

## `SELECT` examples

Returns a list of all edge gateway pool objects at a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_gateway_pools', value: 'view', },
        { label: 'edge_gateway_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
edgeGatewayPool,
edge_gateways,
gateway_capacity_kilo_bits_per_second,
gateway_type,
gre_vip_subnet,
location,
number_of_gateways,
public_ip_address,
redundant_gateway_count,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure_stack.fabric_admin.vw_edge_gateway_pools
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.fabric_admin.edge_gateway_pools
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

