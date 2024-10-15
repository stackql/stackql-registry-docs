---
title: managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases
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

Creates, updates, deletes, gets or lists a <code>managed_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_databases', value: 'view', },
        { label: 'managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_complete_restore" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalog_collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="cross_subscription_restorable_dropped_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cross_subscription_source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cross_subscription_target_managed_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_secondary_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_ledger_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_backup_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="long_term_retention_backup_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoverable_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorable_dropped_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_container_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_container_sas_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_container_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The managed database's properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__location" /> | Creates a new database or updates an existing database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed database. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates an existing database. |
| <CopyableCode code="cancel_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Cancels a managed database move operation. |
| <CopyableCode code="complete_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Completes a managed database move operation. |
| <CopyableCode code="complete_restore" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__lastBackupName" /> | Completes the restore operation on a managed database. |
| <CopyableCode code="start_move" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId, data__destinationManagedDatabaseId" /> | Starts a managed database move operation. |

## `SELECT` examples

Gets a managed database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_databases', value: 'view', },
        { label: 'managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_complete_restore,
catalog_collation,
collation,
create_mode,
creation_date,
cross_subscription_restorable_dropped_database_id,
cross_subscription_source_database_id,
cross_subscription_target_managed_instance_id,
databaseName,
default_secondary_location,
earliest_restore_point,
failover_group_id,
is_ledger_on,
last_backup_name,
location,
long_term_retention_backup_resource_id,
managedInstanceName,
recoverable_database_id,
resourceGroupName,
restorable_dropped_database_id,
restore_point_in_time,
source_database_id,
status,
storage_container_identity,
storage_container_sas_token,
storage_container_uri,
subscriptionId,
tags
FROM azure.sql.vw_managed_databases
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.sql.managed_databases
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_databases</code> resource.

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
INSERT INTO azure.sql.managed_databases (
databaseName,
managedInstanceName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
properties
)
SELECT 
'{{ databaseName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: collation
          value: string
        - name: status
          value: string
        - name: creationDate
          value: string
        - name: earliestRestorePoint
          value: string
        - name: restorePointInTime
          value: string
        - name: defaultSecondaryLocation
          value: string
        - name: catalogCollation
          value: string
        - name: createMode
          value: string
        - name: storageContainerUri
          value: string
        - name: sourceDatabaseId
          value: string
        - name: crossSubscriptionSourceDatabaseId
          value: string
        - name: restorableDroppedDatabaseId
          value: string
        - name: crossSubscriptionRestorableDroppedDatabaseId
          value: string
        - name: storageContainerIdentity
          value: string
        - name: storageContainerSasToken
          value: string
        - name: failoverGroupId
          value: string
        - name: recoverableDatabaseId
          value: string
        - name: longTermRetentionBackupResourceId
          value: string
        - name: autoCompleteRestore
          value: boolean
        - name: lastBackupName
          value: string
        - name: crossSubscriptionTargetManagedInstanceId
          value: string
        - name: isLedgerOn
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_databases</code> resource.

```sql
/*+ update */
UPDATE azure.sql.managed_databases
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_databases
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
