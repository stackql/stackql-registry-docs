---
title: maintenance_window_options
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window_options
  - sql
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

Creates, updates, deletes, gets or lists a <code>maintenance_window_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.maintenance_window_options" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_window_options', value: 'view', },
        { label: 'maintenance_window_options', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allow_multiple_maintenance_windows_per_cycle" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_duration_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenanceWindowOptionsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_window_cycles" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_cycles" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_duration_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_granularity_in_minutes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Maintenance window options properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, maintenanceWindowOptionsName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of available maintenance windows. |

## `SELECT` examples

Gets a list of available maintenance windows.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_window_options', value: 'view', },
        { label: 'maintenance_window_options', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allow_multiple_maintenance_windows_per_cycle,
databaseName,
default_duration_in_minutes,
is_enabled,
maintenanceWindowOptionsName,
maintenance_window_cycles,
min_cycles,
min_duration_in_minutes,
resourceGroupName,
serverName,
subscriptionId,
time_granularity_in_minutes
FROM azure.sql.vw_maintenance_window_options
WHERE databaseName = '{{ databaseName }}'
AND maintenanceWindowOptionsName = '{{ maintenanceWindowOptionsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.maintenance_window_options
WHERE databaseName = '{{ databaseName }}'
AND maintenanceWindowOptionsName = '{{ maintenanceWindowOptionsName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

