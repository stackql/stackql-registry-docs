---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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

Creates, updates, deletes, gets or lists a <code>databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_databases', value: 'view', },
        { label: 'databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_pause_delay" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalog_collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_service_objective_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_secondary_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="elastic_pool_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_protector" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_protector_auto_rotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="federated_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="free_limit_exhaustion_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="high_availability_replica_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="is_infra_encryption_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_ledger_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of database. This is metadata used for the Azure portal experience. |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="long_term_retention_backup_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="manual_cutover" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_log_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="paused_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="perform_cutover" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_enclave_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="read_scale" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoverable_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_services_recovery_point_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="requested_backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="requested_service_objective_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorable_dropped_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resumed_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="sample_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="source_database_deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="use_free_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_redundant" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="kind" /> | `string` | Kind of database. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the database. |
| <CopyableCode code="properties" /> | `object` | The database's properties. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database. |
| <CopyableCode code="list_by_elastic_pool" /> | `SELECT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of databases in an elastic pool. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of databases. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, data__location" /> | Creates a new database or updates an existing database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Deletes the database. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Updates an existing database. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri" /> | Exports a database. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Failovers a database. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri" /> | Imports a bacpac into a new database. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Pauses a database. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, data__id" /> | Renames a database. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Resumes a database. |
| <CopyableCode code="upgrade_data_warehouse" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Upgrades a data warehouse. |

## `SELECT` examples

Gets a list of databases.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_databases', value: 'view', },
        { label: 'databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_pause_delay,
availability_zone,
catalog_collation,
collation,
create_mode,
creation_date,
current_backup_storage_redundancy,
current_service_objective_name,
current_sku,
databaseName,
database_id,
default_secondary_location,
earliest_restore_date,
elastic_pool_id,
encryption_protector,
encryption_protector_auto_rotation,
failover_group_id,
federated_client_id,
free_limit_exhaustion_behavior,
high_availability_replica_count,
identity,
is_infra_encryption_enabled,
is_ledger_on,
keys,
kind,
license_type,
location,
long_term_retention_backup_resource_id,
maintenance_configuration_id,
managed_by,
manual_cutover,
max_log_size_bytes,
max_size_bytes,
min_capacity,
paused_date,
perform_cutover,
preferred_enclave_type,
read_scale,
recoverable_database_id,
recovery_services_recovery_point_id,
requested_backup_storage_redundancy,
requested_service_objective_name,
resourceGroupName,
restorable_dropped_database_id,
restore_point_in_time,
resumed_date,
sample_name,
secondary_type,
serverName,
sku,
source_database_deletion_date,
source_database_id,
source_resource_id,
status,
subscriptionId,
tags,
use_free_limit,
zone_redundant
FROM azure.sql.vw_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
managedBy,
properties,
sku,
tags
FROM azure.sql.databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>databases</code> resource.

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
INSERT INTO azure.sql.databases (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
data__location,
location,
tags,
sku,
identity,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ identity }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: kind
      value: string
    - name: managedBy
      value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: createMode
          value: string
        - name: collation
          value: string
        - name: maxSizeBytes
          value: integer
        - name: sampleName
          value: string
        - name: elasticPoolId
          value: string
        - name: sourceDatabaseId
          value: string
        - name: status
          value: string
        - name: databaseId
          value: string
        - name: creationDate
          value: string
        - name: currentServiceObjectiveName
          value: string
        - name: requestedServiceObjectiveName
          value: string
        - name: defaultSecondaryLocation
          value: string
        - name: failoverGroupId
          value: string
        - name: restorePointInTime
          value: string
        - name: sourceDatabaseDeletionDate
          value: string
        - name: recoveryServicesRecoveryPointId
          value: string
        - name: longTermRetentionBackupResourceId
          value: string
        - name: recoverableDatabaseId
          value: string
        - name: restorableDroppedDatabaseId
          value: string
        - name: catalogCollation
          value: string
        - name: zoneRedundant
          value: boolean
        - name: licenseType
          value: string
        - name: maxLogSizeBytes
          value: integer
        - name: earliestRestoreDate
          value: string
        - name: readScale
          value: string
        - name: highAvailabilityReplicaCount
          value: integer
        - name: secondaryType
          value: string
        - name: autoPauseDelay
          value: integer
        - name: currentBackupStorageRedundancy
          value: string
        - name: requestedBackupStorageRedundancy
          value: string
        - name: minCapacity
          value: number
        - name: pausedDate
          value: string
        - name: resumedDate
          value: string
        - name: maintenanceConfigurationId
          value: string
        - name: isLedgerOn
          value: boolean
        - name: isInfraEncryptionEnabled
          value: boolean
        - name: federatedClientId
          value: string
        - name: keys
          value: object
        - name: encryptionProtector
          value: string
        - name: preferredEnclaveType
          value: string
        - name: useFreeLimit
          value: boolean
        - name: freeLimitExhaustionBehavior
          value: string
        - name: sourceResourceId
          value: string
        - name: manualCutover
          value: boolean
        - name: performCutover
          value: boolean
        - name: availabilityZone
          value: string
        - name: encryptionProtectorAutoRotation
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>databases</code> resource.

```sql
/*+ update */
UPDATE azure.sql.databases
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.databases
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
