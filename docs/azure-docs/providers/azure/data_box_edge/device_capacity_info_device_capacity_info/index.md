---
title: device_capacity_info_device_capacity_info
hide_title: false
hide_table_of_contents: false
keywords:
  - device_capacity_info_device_capacity_info
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>device_capacity_info_device_capacity_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_capacity_info_device_capacity_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.device_capacity_info_device_capacity_info" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_capacity_info_device_capacity_info', value: 'view', },
        { label: 'device_capacity_info_device_capacity_info', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="cluster_compute_capacity_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_storage_capacity_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_capacity_infos" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_stamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The properties of Device Capacity Info |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified device capacity info. |

## `SELECT` examples

Gets the properties of the specified device capacity info.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_capacity_info_device_capacity_info', value: 'view', },
        { label: 'device_capacity_info_device_capacity_info', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cluster_compute_capacity_info,
cluster_storage_capacity_info,
deviceName,
node_capacity_infos,
resourceGroupName,
subscriptionId,
system_data,
time_stamp,
type
FROM azure.data_box_edge.vw_device_capacity_info_device_capacity_info
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_box_edge.device_capacity_info_device_capacity_info
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

