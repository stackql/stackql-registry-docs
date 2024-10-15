---
title: database_migrations_sql_dbs
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_sql_dbs
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

Creates, updates, deletes, gets or lists a <code>database_migrations_sql_dbs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_migrations_sql_dbs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_sql_dbs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_sql_dbs', value: 'view', },
        { label: 'database_migrations_sql_dbs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="offline_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_sql_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlDbInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="targetDbName" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_database_collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_sql_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for SQL database. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Retrieve the Database Migration resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Create or Update Database Migration resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Delete Database Migration resource. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlDbInstanceName, subscriptionId, targetDbName" /> | Stop on going migration for the database. |

## `SELECT` examples

Retrieve the Database Migration resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_sql_dbs', value: 'view', },
        { label: 'database_migrations_sql_dbs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
migration_status_details,
offline_configuration,
resourceGroupName,
source_database_name,
source_server_name,
source_sql_connection,
sqlDbInstanceName,
subscriptionId,
system_data,
table_list,
targetDbName,
target_database_collation,
target_sql_connection,
type
FROM azure.data_migration.vw_database_migrations_sql_dbs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlDbInstanceName = '{{ sqlDbInstanceName }}'
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
FROM azure.data_migration.database_migrations_sql_dbs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlDbInstanceName = '{{ sqlDbInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbName = '{{ targetDbName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_migrations_sql_dbs</code> resource.

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
INSERT INTO azure.data_migration.database_migrations_sql_dbs (
resourceGroupName,
sqlDbInstanceName,
subscriptionId,
targetDbName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlDbInstanceName }}',
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
            - name: sqlDataCopyErrors
              value:
                - string
            - name: listOfCopyProgressDetails
              value:
                - - name: tableName
                    value: string
                  - name: status
                    value: string
                  - name: parallelCopyType
                    value: string
                  - name: usedParallelCopies
                    value: integer
                  - name: dataRead
                    value: integer
                  - name: dataWritten
                    value: integer
                  - name: rowsRead
                    value: integer
                  - name: rowsCopied
                    value: integer
                  - name: copyStart
                    value: string
                  - name: copyThroughput
                    value: number
                  - name: copyDuration
                    value: integer
        - name: offlineConfiguration
          value:
            - name: offline
              value: boolean
        - name: tableList
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>database_migrations_sql_dbs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.database_migrations_sql_dbs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlDbInstanceName = '{{ sqlDbInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbName = '{{ targetDbName }}';
```
