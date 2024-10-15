---
title: logical_subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - logical_subnets
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

Creates, updates, deletes, gets or lists a <code>logical_subnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logical_subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.logical_subnets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logical_subnets', value: 'view', },
        { label: 'logical_subnets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="ip_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_public" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="logicalNetwork" /> | `text` | field from the `properties` object |
| <CopyableCode code="logicalSubnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of a logical subnet. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, logicalNetwork, logicalSubnet, resourceGroupName, subscriptionId" /> | Returns the requested logical subnet. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, logicalNetwork, resourceGroupName, subscriptionId" /> | Returns a list of all logical subnets. |

## `SELECT` examples

Returns a list of all logical subnets.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logical_subnets', value: 'view', },
        { label: 'logical_subnets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ip_pools,
is_public,
location,
logicalNetwork,
logicalSubnet,
metadata,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure_stack.fabric_admin.vw_logical_subnets
WHERE location = '{{ location }}'
AND logicalNetwork = '{{ logicalNetwork }}'
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
FROM azure_stack.fabric_admin.logical_subnets
WHERE location = '{{ location }}'
AND logicalNetwork = '{{ logicalNetwork }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

