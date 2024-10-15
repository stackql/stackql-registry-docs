---
title: maintenance_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_windows
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

Creates, updates, deletes, gets or lists a <code>maintenance_windows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.maintenance_windows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_windows', value: 'view', },
        { label: 'maintenance_windows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenanceWindowName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_ranges" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Maintenance windows resource properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, maintenanceWindowName, resourceGroupName, serverName, subscriptionId" /> | Gets maintenance windows settings for a database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, maintenanceWindowName, resourceGroupName, serverName, subscriptionId" /> | Sets maintenance windows settings for a database. |

## `SELECT` examples

Gets maintenance windows settings for a database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_windows', value: 'view', },
        { label: 'maintenance_windows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
maintenanceWindowName,
resourceGroupName,
serverName,
subscriptionId,
time_ranges
FROM azure.sql.vw_maintenance_windows
WHERE databaseName = '{{ databaseName }}'
AND maintenanceWindowName = '{{ maintenanceWindowName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.maintenance_windows
WHERE databaseName = '{{ databaseName }}'
AND maintenanceWindowName = '{{ maintenanceWindowName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>maintenance_windows</code> resource.

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
INSERT INTO azure.sql.maintenance_windows (
databaseName,
maintenanceWindowName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ maintenanceWindowName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
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
