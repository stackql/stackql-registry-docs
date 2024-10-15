---
title: autonomous_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_databases
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

Creates, updates, deletes, gets or lists a <code>autonomous_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_databases', value: 'view', },
        { label: 'autonomous_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actual_used_data_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocated_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="apex_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomous_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomous_maintenance_schedule_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="autonomousdatabasename" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_upgrade_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_retention_period_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="character_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_strings" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_urls" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_contacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_base_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_safe_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_workload" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="failed_data_recovery_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_memory_area_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_auto_scaling_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_auto_scaling_for_storage_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_local_data_guard_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_mtls_connection_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_preview" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_preview_version_with_service_terms_accepted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_remote_data_guard_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_adg_auto_failover_max_data_loss_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_disaster_recovery_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_standby_db" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="long_term_backup_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_per_oracle_compute_unit_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="ncharacter_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_long_term_backup_time_stamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="oci_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="operations_insights_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_db_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_db_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="permission_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisionable_cpus" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_console_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_web_developer_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_regions_to_clone_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_data_guard_role_changed" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_deletion_of_free_autonomous_database" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_local_data_guard_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_maintenance_begin" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_maintenance_end" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_of_last_failover" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_of_last_refresh" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_of_last_refresh_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_of_last_switchover" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_reclamation_of_free_autonomous_database" /> | `text` | field from the `properties` object |
| <CopyableCode code="used_data_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="used_data_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="whitelisted_ips" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Autonomous Database base resource model. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Get a AutonomousDatabase |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List AutonomousDatabase resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List AutonomousDatabase resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Create a AutonomousDatabase |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Delete a AutonomousDatabase |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Update a AutonomousDatabase |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Perform failover action on Autonomous Database |
| <CopyableCode code="generate_wallet" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId, data__password" /> | Generate wallet action on Autonomous Database |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId, data__timestamp" /> | Restores an Autonomous Database based on the provided request parameters. |
| <CopyableCode code="shrink" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | This operation shrinks the current allocated storage down to the current actual used data storage. |
| <CopyableCode code="switchover" /> | `EXEC` | <CopyableCode code="autonomousdatabasename, resourceGroupName, subscriptionId" /> | Perform switchover action on Autonomous Database |

## `SELECT` examples

List AutonomousDatabase resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_databases', value: 'view', },
        { label: 'autonomous_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actual_used_data_storage_size_in_tbs,
admin_password,
allocated_storage_size_in_tbs,
apex_details,
autonomous_database_id,
autonomous_maintenance_schedule_type,
autonomousdatabasename,
available_upgrade_versions,
backup_retention_period_in_days,
character_set,
compute_count,
compute_model,
connection_strings,
connection_urls,
cpu_core_count,
customer_contacts,
data_base_type,
data_safe_status,
data_storage_size_in_gbs,
data_storage_size_in_tbs,
database_edition,
db_version,
db_workload,
display_name,
failed_data_recovery_in_seconds,
in_memory_area_in_gbs,
is_auto_scaling_enabled,
is_auto_scaling_for_storage_enabled,
is_local_data_guard_enabled,
is_mtls_connection_required,
is_preview,
is_preview_version_with_service_terms_accepted,
is_remote_data_guard_enabled,
license_model,
lifecycle_details,
lifecycle_state,
local_adg_auto_failover_max_data_loss_limit,
local_disaster_recovery_type,
local_standby_db,
location,
long_term_backup_schedule,
memory_per_oracle_compute_unit_in_gbs,
ncharacter_set,
next_long_term_backup_time_stamp,
oci_url,
ocid,
open_mode,
operations_insights_status,
peer_db_id,
peer_db_ids,
permission_level,
private_endpoint,
private_endpoint_ip,
private_endpoint_label,
provisionable_cpus,
provisioning_state,
resourceGroupName,
role,
scheduled_operations,
service_console_url,
sql_web_developer_url,
subnet_id,
subscriptionId,
supported_regions_to_clone_to,
tags,
time_created,
time_data_guard_role_changed,
time_deletion_of_free_autonomous_database,
time_local_data_guard_enabled,
time_maintenance_begin,
time_maintenance_end,
time_of_last_failover,
time_of_last_refresh,
time_of_last_refresh_point,
time_of_last_switchover,
time_reclamation_of_free_autonomous_database,
used_data_storage_size_in_gbs,
used_data_storage_size_in_tbs,
vnet_id,
whitelisted_ips
FROM azure_isv.oracle.vw_autonomous_databases
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.oracle.autonomous_databases
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autonomous_databases</code> resource.

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
INSERT INTO azure_isv.oracle.autonomous_databases (
autonomousdatabasename,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ autonomousdatabasename }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: adminPassword
          value: []
        - name: dataBaseType
          value: []
        - name: autonomousMaintenanceScheduleType
          value: []
        - name: characterSet
          value: string
        - name: computeCount
          value: number
        - name: computeModel
          value: []
        - name: cpuCoreCount
          value: integer
        - name: customerContacts
          value:
            - - name: email
                value: string
        - name: dataStorageSizeInTbs
          value: integer
        - name: dataStorageSizeInGbs
          value: integer
        - name: dbVersion
          value: string
        - name: dbWorkload
          value: []
        - name: displayName
          value: string
        - name: isAutoScalingEnabled
          value: boolean
        - name: isAutoScalingForStorageEnabled
          value: boolean
        - name: peerDbIds
          value:
            - string
        - name: peerDbId
          value: string
        - name: isLocalDataGuardEnabled
          value: boolean
        - name: isRemoteDataGuardEnabled
          value: boolean
        - name: localDisasterRecoveryType
          value: []
        - name: localStandbyDb
          value:
            - name: lagTimeInSeconds
              value: integer
            - name: lifecycleState
              value: []
            - name: lifecycleDetails
              value: string
            - name: timeDataGuardRoleChanged
              value: string
            - name: timeDisasterRecoveryRoleChanged
              value: string
        - name: failedDataRecoveryInSeconds
          value: integer
        - name: isMtlsConnectionRequired
          value: boolean
        - name: isPreviewVersionWithServiceTermsAccepted
          value: boolean
        - name: licenseModel
          value: []
        - name: ncharacterSet
          value: string
        - name: lifecycleDetails
          value: string
        - name: provisioningState
          value: []
        - name: scheduledOperations
          value:
            - name: dayOfWeek
              value:
                - name: name
                  value: []
            - name: scheduledStartTime
              value: string
            - name: scheduledStopTime
              value: string
        - name: privateEndpointIp
          value: string
        - name: privateEndpointLabel
          value: string
        - name: ociUrl
          value: string
        - name: subnetId
          value: []
        - name: vnetId
          value: []
        - name: timeCreated
          value: string
        - name: timeMaintenanceBegin
          value: string
        - name: timeMaintenanceEnd
          value: string
        - name: actualUsedDataStorageSizeInTbs
          value: number
        - name: allocatedStorageSizeInTbs
          value: number
        - name: apexDetails
          value:
            - name: apexVersion
              value: string
            - name: ordsVersion
              value: string
        - name: availableUpgradeVersions
          value:
            - string
        - name: connectionStrings
          value:
            - name: allConnectionStrings
              value:
                - name: high
                  value: string
                - name: low
                  value: string
                - name: medium
                  value: string
            - name: dedicated
              value: string
            - name: high
              value: string
            - name: low
              value: string
            - name: medium
              value: string
            - name: profiles
              value:
                - - name: consumerGroup
                    value: []
                  - name: displayName
                    value: string
                  - name: hostFormat
                    value: []
                  - name: isRegional
                    value: boolean
                  - name: protocol
                    value: []
                  - name: sessionMode
                    value: []
                  - name: syntaxFormat
                    value: []
                  - name: tlsAuthentication
                    value: []
                  - name: value
                    value: string
        - name: connectionUrls
          value:
            - name: apexUrl
              value: string
            - name: databaseTransformsUrl
              value: string
            - name: graphStudioUrl
              value: string
            - name: machineLearningNotebookUrl
              value: string
            - name: mongoDbUrl
              value: string
            - name: ordsUrl
              value: string
            - name: sqlDevWebUrl
              value: string
        - name: dataSafeStatus
          value: []
        - name: databaseEdition
          value: []
        - name: autonomousDatabaseId
          value: []
        - name: inMemoryAreaInGbs
          value: integer
        - name: nextLongTermBackupTimeStamp
          value: string
        - name: longTermBackupSchedule
          value:
            - name: repeatCadence
              value: []
            - name: timeOfBackup
              value: string
            - name: retentionPeriodInDays
              value: []
            - name: isDisabled
              value: boolean
        - name: isPreview
          value: boolean
        - name: localAdgAutoFailoverMaxDataLossLimit
          value: integer
        - name: memoryPerOracleComputeUnitInGbs
          value: integer
        - name: openMode
          value: []
        - name: operationsInsightsStatus
          value: []
        - name: permissionLevel
          value: []
        - name: privateEndpoint
          value: string
        - name: provisionableCpus
          value:
            - integer
        - name: role
          value: []
        - name: serviceConsoleUrl
          value: string
        - name: sqlWebDeveloperUrl
          value: string
        - name: supportedRegionsToCloneTo
          value:
            - string
        - name: timeDataGuardRoleChanged
          value: string
        - name: timeDeletionOfFreeAutonomousDatabase
          value: string
        - name: timeLocalDataGuardEnabled
          value: string
        - name: timeOfLastFailover
          value: string
        - name: timeOfLastRefresh
          value: string
        - name: timeOfLastRefreshPoint
          value: string
        - name: timeOfLastSwitchover
          value: string
        - name: timeReclamationOfFreeAutonomousDatabase
          value: string
        - name: usedDataStorageSizeInGbs
          value: integer
        - name: usedDataStorageSizeInTbs
          value: integer
        - name: ocid
          value: []
        - name: backupRetentionPeriodInDays
          value: integer
        - name: whitelistedIps
          value:
            - []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>autonomous_databases</code> resource.

```sql
/*+ update */
UPDATE azure_isv.oracle.autonomous_databases
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>autonomous_databases</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.autonomous_databases
WHERE autonomousdatabasename = '{{ autonomousdatabasename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
