---
title: sql_server_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_databases
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_databases', value: 'view', },
        { label: 'sql_server_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backup_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="collation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="compatibility_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_database_upload_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="space_available_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of Arc Sql Server database resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves an Arc Sql Server database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId, data__properties" /> | Creates or replaces an Arc Sql Server Database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Deletes an Arc Sql Server database resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Updates an existing database. |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_databases', value: 'view', },
        { label: 'sql_server_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backup_information,
backup_policy,
collation_name,
compatibility_level,
create_mode,
databaseName,
database_creation_date,
database_options,
earliest_restore_date,
is_read_only,
last_database_upload_time,
location,
provisioning_state,
recovery_mode,
resourceGroupName,
restore_point_in_time,
size_mb,
source_database_id,
space_available_mb,
sqlServerInstanceName,
state,
subscriptionId,
tags
FROM azure.azure_arc_data.vw_sql_server_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.azure_arc_data.sql_server_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_server_databases</code> resource.

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
INSERT INTO azure.azure_arc_data.sql_server_databases (
databaseName,
resourceGroupName,
sqlServerInstanceName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ sqlServerInstanceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: collationName
          value: string
        - name: databaseCreationDate
          value: string
        - name: compatibilityLevel
          value: integer
        - name: sizeMB
          value: number
        - name: spaceAvailableMB
          value: number
        - name: state
          value: string
        - name: isReadOnly
          value: boolean
        - name: recoveryMode
          value: string
        - name: databaseOptions
          value:
            - name: isAutoCloseOn
              value: boolean
            - name: isAutoShrinkOn
              value: boolean
            - name: isAutoCreateStatsOn
              value: boolean
            - name: isAutoUpdateStatsOn
              value: boolean
            - name: isRemoteDataArchiveEnabled
              value: boolean
            - name: isMemoryOptimizationEnabled
              value: boolean
            - name: isEncrypted
              value: boolean
            - name: isTrustworthyOn
              value: boolean
        - name: backupInformation
          value:
            - name: lastFullBackup
              value: string
            - name: lastLogBackup
              value: string
        - name: backupPolicy
          value:
            - name: retentionPeriodDays
              value: integer
            - name: fullBackupDays
              value: integer
            - name: differentialBackupHours
              value: integer
            - name: transactionLogBackupMinutes
              value: integer
        - name: earliestRestoreDate
          value: string
        - name: createMode
          value: string
        - name: sourceDatabaseId
          value: string
        - name: restorePointInTime
          value: string
        - name: provisioningState
          value: string
        - name: lastDatabaseUploadTime
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_server_databases</code> resource.

```sql
/*+ update */
UPDATE azure.azure_arc_data.sql_server_databases
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_server_databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.sql_server_databases
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerInstanceName = '{{ sqlServerInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
