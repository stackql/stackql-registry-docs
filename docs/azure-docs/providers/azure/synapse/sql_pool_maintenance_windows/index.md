---
title: sql_pool_maintenance_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_maintenance_windows
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

Creates, updates, deletes, gets or lists a <code>sql_pool_maintenance_windows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_maintenance_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_maintenance_windows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_maintenance_windows', value: 'view', },
        { label: 'sql_pool_maintenance_windows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="maintenanceWindowName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_ranges" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Maintenance windows resource properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="maintenanceWindowName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get a SQL pool's Maintenance Windows. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="maintenanceWindowName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Creates or updates a Sql pool's maintenance windows settings. |

## `SELECT` examples

Get a SQL pool's Maintenance Windows.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_maintenance_windows', value: 'view', },
        { label: 'sql_pool_maintenance_windows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
maintenanceWindowName,
resourceGroupName,
sqlPoolName,
subscriptionId,
time_ranges,
workspaceName
FROM azure.synapse.vw_sql_pool_maintenance_windows
WHERE maintenanceWindowName = '{{ maintenanceWindowName }}'
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
FROM azure.synapse.sql_pool_maintenance_windows
WHERE maintenanceWindowName = '{{ maintenanceWindowName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_maintenance_windows</code> resource.

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
INSERT INTO azure.synapse.sql_pool_maintenance_windows (
maintenanceWindowName,
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ maintenanceWindowName }}',
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: timeRanges
          value:
            - - name: dayOfWeek
                value: string
              - name: startTime
                value: string
              - name: duration
                value: string

```
</TabItem>
</Tabs>
