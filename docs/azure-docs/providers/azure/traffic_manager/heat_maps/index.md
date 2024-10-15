---
title: heat_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - heat_maps
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>heat_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>heat_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.heat_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_heat_maps', value: 'view', },
        { label: 'heat_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="heatMapType" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="traffic_flows" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class representing a Traffic Manager HeatMap properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="heatMapType, profileName, resourceGroupName, subscriptionId" /> | Gets latest heatmap for Traffic Manager profile. |

## `SELECT` examples

Gets latest heatmap for Traffic Manager profile.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_heat_maps', value: 'view', },
        { label: 'heat_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
end_time,
endpoints,
heatMapType,
profileName,
resourceGroupName,
start_time,
subscriptionId,
traffic_flows
FROM azure.traffic_manager.vw_heat_maps
WHERE heatMapType = '{{ heatMapType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.traffic_manager.heat_maps
WHERE heatMapType = '{{ heatMapType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

