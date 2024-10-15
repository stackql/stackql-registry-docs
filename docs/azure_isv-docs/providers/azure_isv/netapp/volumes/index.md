---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - netapp
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="actual_throughput_mibps" /> | `text` | field from the `properties` object |
| <CopyableCode code="avs_data_store" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="baremetal_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_pool_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="clone_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="cool_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="cool_access_retrieval_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="coolness_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_protection" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_store_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_group_quota_in_ki_bs" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_user_quota_in_ki_bs" /> | `text` | field from the `properties` object |
| <CopyableCode code="delete_base_snapshot" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_subvolumes" /> | `text` | field from the `properties` object |
| <CopyableCode code="encrypted" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_key_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="export_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_access_logs" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_system_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_default_quota_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_large_volume" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_restoring" /> | `text` | field from the `properties` object |
| <CopyableCode code="kerberos_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_private_endpoint_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ldap_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="maximum_number_of_files" /> | `text` | field from the `properties` object |
| <CopyableCode code="mount_targets" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_features" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_sibling_set_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="originating_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_style" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="smb_access_based_enumeration" /> | `text` | field from the `properties` object |
| <CopyableCode code="smb_continuously_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="smb_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="smb_non_browsable" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_directory_visible" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_to_network_proximity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="t2_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="throughput_mibps" /> | `text` | field from the `properties` object |
| <CopyableCode code="unix_permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="usage_threshold" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_spec_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | Availability Zone |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Volume properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | Availability Zone |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Get the details of the specified volume |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | List all volumes within the capacity pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__location, data__properties" /> | Create or update the specified volume within the capacity pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Delete the specified volume |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Patch the specified volume |
| <CopyableCode code="authorize_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Authorize the replication connection on the source volume |
| <CopyableCode code="break_file_locks" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Break all the file locks on a volume |
| <CopyableCode code="break_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Break the replication connection on the destination volume |
| <CopyableCode code="finalize_relocation" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Finalizes the relocation of the volume and cleans up the old volume. |
| <CopyableCode code="pool_change" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__newPoolResourceId" /> | Moves volume to another pool |
| <CopyableCode code="populate_availability_zone" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | This operation will populate availability zone information for a volume |
| <CopyableCode code="re_initialize_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Re-Initializes the replication connection on the destination volume |
| <CopyableCode code="reestablish_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Re-establish a previously deleted replication between 2 volumes that have a common ad-hoc or policy-based snapshots |
| <CopyableCode code="relocate" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Relocates volume to a new stamp |
| <CopyableCode code="replication_status" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Get the status of the replication |
| <CopyableCode code="reset_cifs_password" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Reset cifs password from volume |
| <CopyableCode code="resync_replication" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from destination to source. |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Revert a volume to the snapshot specified in the body |
| <CopyableCode code="revert_relocation" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Reverts the volume relocation process, cleans up the new volume and starts using the former-existing volume. |

## `SELECT` examples

List all volumes within the capacity pool

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
actual_throughput_mibps,
avs_data_store,
backup_id,
baremetal_tenant_id,
capacity_pool_resource_id,
clone_progress,
cool_access,
cool_access_retrieval_policy,
coolness_period,
creation_token,
data_protection,
data_store_resource_id,
default_group_quota_in_ki_bs,
default_user_quota_in_ki_bs,
delete_base_snapshot,
enable_subvolumes,
encrypted,
encryption_key_source,
etag,
export_policy,
file_access_logs,
file_system_id,
is_default_quota_enabled,
is_large_volume,
is_restoring,
kerberos_enabled,
key_vault_private_endpoint_resource_id,
ldap_enabled,
location,
maximum_number_of_files,
mount_targets,
network_features,
network_sibling_set_id,
originating_resource_id,
placement_rules,
poolName,
protocol_types,
provisioned_availability_zone,
provisioning_state,
proximity_placement_group,
resourceGroupName,
security_style,
service_level,
smb_access_based_enumeration,
smb_continuously_available,
smb_encryption,
smb_non_browsable,
snapshot_directory_visible,
snapshot_id,
storage_to_network_proximity,
subnet_id,
subscriptionId,
t2_network,
tags,
throughput_mibps,
unix_permissions,
usage_threshold,
volumeName,
volume_group_name,
volume_spec_name,
volume_type,
zones
FROM azure_isv.netapp.vw_volumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags,
zones
FROM azure_isv.netapp.volumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

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
INSERT INTO azure_isv.netapp.volumes (
accountName,
poolName,
resourceGroupName,
subscriptionId,
volumeName,
data__location,
data__properties,
tags,
location,
zones,
properties
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ zones }}',
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
    - name: etag
      value: string
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: fileSystemId
          value: string
        - name: creationToken
          value: string
        - name: serviceLevel
          value: []
        - name: usageThreshold
          value: integer
        - name: exportPolicy
          value: string
        - name: protocolTypes
          value:
            - string
        - name: provisioningState
          value: string
        - name: snapshotId
          value: string
        - name: deleteBaseSnapshot
          value: boolean
        - name: backupId
          value: string
        - name: baremetalTenantId
          value: string
        - name: subnetId
          value: string
        - name: networkFeatures
          value: []
        - name: networkSiblingSetId
          value: string
        - name: storageToNetworkProximity
          value: string
        - name: mountTargets
          value:
            - - name: mountTargetId
                value: string
              - name: fileSystemId
                value: string
              - name: ipAddress
                value: string
              - name: smbServerFqdn
                value: string
        - name: volumeType
          value: string
        - name: dataProtection
          value: string
        - name: isRestoring
          value: boolean
        - name: snapshotDirectoryVisible
          value: boolean
        - name: kerberosEnabled
          value: boolean
        - name: securityStyle
          value: string
        - name: smbEncryption
          value: boolean
        - name: smbAccessBasedEnumeration
          value: []
        - name: smbNonBrowsable
          value: []
        - name: smbContinuouslyAvailable
          value: boolean
        - name: throughputMibps
          value: number
        - name: actualThroughputMibps
          value: number
        - name: encryptionKeySource
          value: string
        - name: keyVaultPrivateEndpointResourceId
          value: string
        - name: ldapEnabled
          value: boolean
        - name: coolAccess
          value: boolean
        - name: coolnessPeriod
          value: integer
        - name: coolAccessRetrievalPolicy
          value: []
        - name: unixPermissions
          value: string
        - name: cloneProgress
          value: integer
        - name: fileAccessLogs
          value: string
        - name: avsDataStore
          value: string
        - name: dataStoreResourceId
          value:
            - string
        - name: isDefaultQuotaEnabled
          value: boolean
        - name: defaultUserQuotaInKiBs
          value: integer
        - name: defaultGroupQuotaInKiBs
          value: integer
        - name: maximumNumberOfFiles
          value: integer
        - name: volumeGroupName
          value: string
        - name: capacityPoolResourceId
          value: string
        - name: proximityPlacementGroup
          value: string
        - name: t2Network
          value: string
        - name: volumeSpecName
          value: string
        - name: encrypted
          value: boolean
        - name: placementRules
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: enableSubvolumes
          value: string
        - name: provisionedAvailabilityZone
          value: string
        - name: isLargeVolume
          value: boolean
        - name: originatingResourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volumes</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.volumes
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.volumes
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
