---
title: autonomous_database_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_backups
  - oracle
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

Creates, updates, deletes, gets or lists a <code>autonomous_database_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_database_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_database_backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_database_backups', value: 'view', },
        { label: 'autonomous_database_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="adbbackupid" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomous_database_ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomousdatabasename" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_automatic" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_restorable" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_period_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_available_til" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_ended" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_started" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | AutonomousDatabaseBackup resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Get a AutonomousDatabaseBackup |
| <CopyableCode code="list_by_autonomous_database" /> | `SELECT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | List AutonomousDatabaseBackup resources by AutonomousDatabase |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Create a AutonomousDatabaseBackup |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Delete a AutonomousDatabaseBackup |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="adbbackupid, autonomousdatabasename, resourceGroupName, subscriptionId" /> | Update a AutonomousDatabaseBackup |

## `SELECT` examples

List AutonomousDatabaseBackup resources by AutonomousDatabase

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_database_backups', value: 'view', },
        { label: 'autonomous_database_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
adbbackupid,
autonomous_database_ocid,
autonomousdatabasename,
backup_type,
database_size_in_tbs,
db_version,
display_name,
is_automatic,
is_restorable,
lifecycle_details,
lifecycle_state,
ocid,
provisioning_state,
resourceGroupName,
retention_period_in_days,
size_in_tbs,
subscriptionId,
time_available_til,
time_ended,
time_started
FROM azure_isv.oracle.vw_autonomous_database_backups
WHERE autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.autonomous_database_backups
WHERE autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autonomous_database_backups</code> resource.

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
INSERT INTO azure_isv.oracle.autonomous_database_backups (
adbbackupid,
autonomousdatabasename,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ adbbackupid }}',
'{{ autonomousdatabasename }}',
'{{ resourceGroupName }}',
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
        - name: autonomousDatabaseOcid
          value: []
        - name: databaseSizeInTbs
          value: number
        - name: dbVersion
          value: string
        - name: displayName
          value: string
        - name: isAutomatic
          value: boolean
        - name: isRestorable
          value: boolean
        - name: lifecycleDetails
          value: string
        - name: lifecycleState
          value: []
        - name: retentionPeriodInDays
          value: integer
        - name: sizeInTbs
          value: number
        - name: timeAvailableTil
          value: string
        - name: timeStarted
          value: string
        - name: timeEnded
          value: string
        - name: backupType
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>autonomous_database_backups</code> resource.

```sql
/*+ update */
UPDATE azure_isv.oracle.autonomous_database_backups
SET 
properties = '{{ properties }}'
WHERE 
adbbackupid = '{{ adbbackupid }}'
AND autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>autonomous_database_backups</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.autonomous_database_backups
WHERE adbbackupid = '{{ adbbackupid }}'
AND autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
