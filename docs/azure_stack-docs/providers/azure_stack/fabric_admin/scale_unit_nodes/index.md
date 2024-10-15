---
title: scale_unit_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_unit_nodes
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

Creates, updates, deletes, gets or lists a <code>scale_unit_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scale_unit_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.scale_unit_nodes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_unit_nodes', value: 'view', },
        { label: 'scale_unit_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="bios_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="bmc_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="can_power_off" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="gpus" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaleUnitNode" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_node_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="vendor" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Holds all properties related to a scale unit node. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Return the requested scale unit node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all scale unit nodes in a location. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Power off a scale unit node. |
| <CopyableCode code="power_on" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Power on a scale unit node. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Repairs a node of the cluster. |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Shutdown a scale unit node. |
| <CopyableCode code="start_maintenance_mode" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Start maintenance mode for a scale unit node. |
| <CopyableCode code="stop_maintenance_mode" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, scaleUnitNode, subscriptionId" /> | Stop maintenance mode for a scale unit node. |

## `SELECT` examples

Returns a list of all scale unit nodes in a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_unit_nodes', value: 'view', },
        { label: 'scale_unit_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bios_version,
bmc_address,
can_power_off,
capacity,
gpus,
location,
model,
power_state,
resourceGroupName,
scaleUnitNode,
scale_unit_name,
scale_unit_node_status,
scale_unit_uri,
serial_number,
subscriptionId,
tags,
type,
vendor
FROM azure_stack.fabric_admin.vw_scale_unit_nodes
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
FROM azure_stack.fabric_admin.scale_unit_nodes
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

