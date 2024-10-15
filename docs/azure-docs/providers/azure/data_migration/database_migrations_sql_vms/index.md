---
title: database_migrations_sql_vms
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_vms
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>database_migrations_sql_vms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_migrations_sql_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_sql_vms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_sql_vms', value: 'view', },
        { label: 'database_migrations_sql_vms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_sql_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlVirtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="targetDbName" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_database_collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for SQL Virtual Machine. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName" /> | Retrieve the specified database migration for a given SQL VM. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName" /> | Create a new database migration to a given SQL VM. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName" /> | Stop in-progress database migration to SQL VM. |
| <CopyableCode code="cutover" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, targetDbName" /> | Initiate cutover for in-progress online database migration to SQL VM. |

## `SELECT` examples

Retrieve the specified database migration for a given SQL VM.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_sql_vms', value: 'view', },
        { label: 'database_migrations_sql_vms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_configuration,
migration_status_details,
offline_configuration,
resourceGroupName,
source_database_name,
source_server_name,
source_sql_connection,
sqlVirtualMachineName,
subscriptionId,
system_data,
targetDbName,
target_database_collation,
type
FROM azure.data_migration.vw_database_migrations_sql_vms
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineName = '{{ sqlVirtualMachineName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbName = '{{ targetDbName }}';
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
FROM azure.data_migration.database_migrations_sql_vms
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineName = '{{ sqlVirtualMachineName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbName = '{{ targetDbName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_migrations_sql_vms</code> resource.

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
INSERT INTO azure.data_migration.database_migrations_sql_vms (
resourceGroupName,
sqlVirtualMachineName,
subscriptionId,
targetDbName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlVirtualMachineName }}',
'{{ subscriptionId }}',
'{{ targetDbName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: sourceSqlConnection
          value:
            - name: dataSource
              value: string
            - name: authentication
              value: string
            - name: userName
              value: string
            - name: password
              value: string
            - name: encryptConnection
              value: boolean
            - name: trustServerCertificate
              value: boolean
        - name: sourceDatabaseName
          value: string
        - name: sourceServerName
          value: string
        - name: targetDatabaseCollation
          value: string
        - name: migrationStatusDetails
          value:
            - name: migrationState
              value: string
            - name: fullBackupSetInfo
              value:
                - name: backupSetId
                  value: string
                - name: firstLSN
                  value: string
                - name: lastLSN
                  value: string
                - name: backupType
                  value: string
                - name: listOfBackupFiles
                  value:
                    - - name: fileName
                        value: string
                      - name: status
                        value: string
                      - name: totalSize
                        value: integer
                      - name: dataRead
                        value: integer
                      - name: dataWritten
                        value: integer
                      - name: copyThroughput
                        value: number
                      - name: copyDuration
                        value: integer
                      - name: familySequenceNumber
                        value: integer
                - name: backupStartDate
                  value: string
                - name: backupFinishDate
                  value: string
                - name: isBackupRestored
                  value: boolean
                - name: hasBackupChecksums
                  value: boolean
                - name: familyCount
                  value: integer
                - name: ignoreReasons
                  value:
                    - string
            - name: activeBackupSets
              value:
                - - name: backupSetId
                    value: string
                  - name: firstLSN
                    value: string
                  - name: lastLSN
                    value: string
                  - name: backupType
                    value: string
                  - name: listOfBackupFiles
                    value:
                      - - name: fileName
                          value: string
                        - name: status
                          value: string
                        - name: totalSize
                          value: integer
                        - name: dataRead
                          value: integer
                        - name: dataWritten
                          value: integer
                        - name: copyThroughput
                          value: number
                        - name: copyDuration
                          value: integer
                        - name: familySequenceNumber
                          value: integer
                  - name: backupStartDate
                    value: string
                  - name: backupFinishDate
                    value: string
                  - name: isBackupRestored
                    value: boolean
                  - name: hasBackupChecksums
                    value: boolean
                  - name: familyCount
                    value: integer
                  - name: ignoreReasons
                    value:
                      - string
            - name: invalidFiles
              value:
                - string
            - name: blobContainerName
              value: string
            - name: isFullBackupRestored
              value: boolean
            - name: restoreBlockingReason
              value: string
            - name: completeRestoreErrorMessage
              value: string
            - name: fileUploadBlockingErrors
              value:
                - string
            - name: currentRestoringFilename
              value: string
            - name: lastRestoredFilename
              value: string
            - name: pendingLogBackupsCount
              value: integer
        - name: backupConfiguration
          value:
            - name: sourceLocation
              value:
                - name: fileShare
                  value:
                    - name: path
                      value: string
                    - name: username
                      value: string
                    - name: password
                      value: string
                - name: azureBlob
                  value:
                    - name: storageAccountResourceId
                      value: string
                    - name: accountKey
                      value: string
                    - name: blobContainerName
                      value: string
                - name: fileStorageType
                  value: string
            - name: targetLocation
              value:
                - name: storageAccountResourceId
                  value: string
                - name: accountKey
                  value: string
        - name: offlineConfiguration
          value:
            - name: offline
              value: boolean
            - name: lastBackupName
              value: string

```
</TabItem>
</Tabs>
