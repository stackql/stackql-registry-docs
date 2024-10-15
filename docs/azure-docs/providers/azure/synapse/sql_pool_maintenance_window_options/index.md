---
title: sql_pool_maintenance_window_options
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_maintenance_window_options
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_maintenance_window_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_maintenance_window_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_maintenance_window_options" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_maintenance_window_options', value: 'view', },
        { label: 'sql_pool_maintenance_window_options', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allow_multiple_maintenance_windows_per_cycle" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_duration_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenanceWindowOptionsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_window_cycles" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_cycles" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_duration_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_granularity_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Maintenance window options properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="maintenanceWindowOptionsName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool's available maintenance windows. |

## `SELECT` examples

Get list of SQL pool's available maintenance windows.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_maintenance_window_options', value: 'view', },
        { label: 'sql_pool_maintenance_window_options', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allow_multiple_maintenance_windows_per_cycle,
default_duration_in_minutes,
is_enabled,
maintenanceWindowOptionsName,
maintenance_window_cycles,
min_cycles,
min_duration_in_minutes,
resourceGroupName,
sqlPoolName,
subscriptionId,
time_granularity_in_minutes,
workspaceName
FROM azure.synapse.vw_sql_pool_maintenance_window_options
WHERE maintenanceWindowOptionsName = '{{ maintenanceWindowOptionsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.sql_pool_maintenance_window_options
WHERE maintenanceWindowOptionsName = '{{ maintenanceWindowOptionsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

