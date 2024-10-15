---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - compute
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

Creates, updates, deletes, gets or lists a <code>disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="bursting_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="bursting_enabled_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="completion_percent" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_access_auth_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="diskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_access_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_iops_read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_iops_read_write" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_mbps_read_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_mbps_read_write" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_settings_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_ownership_update_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by_extended" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_shares" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_access_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="optimized_for_frequent_attach" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="property_updates_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_hibernation" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | The Logical zone list for Disk. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | A relative URI containing the ID of the VM that has the disk attached. |
| <CopyableCode code="managedByExtended" /> | `array` | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs. |
| <CopyableCode code="properties" /> | `object` | Disk resource properties. |
| <CopyableCode code="sku" /> | `object` | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The Logical zone list for Disk. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Gets information about a disk. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disks under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disks under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Creates or updates a disk. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Deletes a disk. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="diskName, resourceGroupName, subscriptionId, data__access, data__durationInSeconds" /> | Grants access to a disk. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="diskName, resourceGroupName, subscriptionId" /> | Revokes access to a disk. |

## `SELECT` examples

Lists all the disks under a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bursting_enabled,
bursting_enabled_time,
completion_percent,
creation_data,
data_access_auth_mode,
diskName,
disk_access_id,
disk_iops_read_only,
disk_iops_read_write,
disk_mbps_read_only,
disk_mbps_read_write,
disk_size_bytes,
disk_size_gb,
disk_state,
encryption,
encryption_settings_collection,
extended_location,
hyper_v_generation,
last_ownership_update_time,
location,
managed_by,
managed_by_extended,
max_shares,
network_access_policy,
optimized_for_frequent_attach,
os_type,
property_updates_in_progress,
provisioning_state,
public_network_access,
purchase_plan,
resourceGroupName,
security_profile,
share_info,
sku,
subscriptionId,
supported_capabilities,
supports_hibernation,
tags,
tier,
time_created,
type,
unique_id,
zones
FROM azure.compute.vw_disks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
location,
managedBy,
managedByExtended,
properties,
sku,
tags,
type,
zones
FROM azure.compute.disks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disks</code> resource.

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
INSERT INTO azure.compute.disks (
diskName,
resourceGroupName,
subscriptionId,
sku,
zones,
extendedLocation,
properties,
location,
tags
)
SELECT 
'{{ diskName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
'{{ zones }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: managedBy
      value: string
    - name: managedByExtended
      value:
        - string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: zones
      value:
        - string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: properties
      value:
        - name: timeCreated
          value: string
        - name: osType
          value: string
        - name: hyperVGeneration
          value: string
        - name: purchasePlan
          value:
            - name: name
              value: string
            - name: publisher
              value: string
            - name: product
              value: string
            - name: promotionCode
              value: string
        - name: supportedCapabilities
          value:
            - name: diskControllerTypes
              value: string
            - name: acceleratedNetwork
              value: boolean
            - name: architecture
              value: string
        - name: creationData
          value:
            - name: createOption
              value: string
            - name: storageAccountId
              value: string
            - name: imageReference
              value:
                - name: id
                  value: string
                - name: sharedGalleryImageId
                  value: string
                - name: communityGalleryImageId
                  value: string
                - name: lun
                  value: integer
            - name: sourceUri
              value: string
            - name: sourceResourceId
              value: string
            - name: sourceUniqueId
              value: string
            - name: uploadSizeBytes
              value: integer
            - name: logicalSectorSize
              value: integer
            - name: securityDataUri
              value: string
            - name: performancePlus
              value: boolean
            - name: elasticSanResourceId
              value: string
            - name: provisionedBandwidthCopySpeed
              value: string
        - name: diskSizeGB
          value: integer
        - name: diskSizeBytes
          value: integer
        - name: uniqueId
          value: string
        - name: encryptionSettingsCollection
          value:
            - name: enabled
              value: boolean
            - name: encryptionSettings
              value:
                - - name: diskEncryptionKey
                    value:
                      - name: sourceVault
                        value:
                          - name: id
                            value: string
                      - name: secretUrl
                        value: string
                  - name: keyEncryptionKey
                    value:
                      - name: keyUrl
                        value: string
            - name: encryptionSettingsVersion
              value: string
        - name: provisioningState
          value: string
        - name: diskIOPSReadWrite
          value: integer
        - name: diskMBpsReadWrite
          value: integer
        - name: diskIOPSReadOnly
          value: integer
        - name: diskMBpsReadOnly
          value: integer
        - name: diskState
          value: []
        - name: encryption
          value:
            - name: diskEncryptionSetId
              value: string
            - name: type
              value: []
        - name: maxShares
          value: integer
        - name: shareInfo
          value:
            - - name: vmUri
                value: string
        - name: networkAccessPolicy
          value: []
        - name: diskAccessId
          value: string
        - name: burstingEnabledTime
          value: string
        - name: tier
          value: string
        - name: burstingEnabled
          value: boolean
        - name: propertyUpdatesInProgress
          value:
            - name: targetTier
              value: string
        - name: supportsHibernation
          value: boolean
        - name: securityProfile
          value:
            - name: securityType
              value: []
            - name: secureVMDiskEncryptionSetId
              value: string
        - name: completionPercent
          value: number
        - name: publicNetworkAccess
          value: []
        - name: dataAccessAuthMode
          value: []
        - name: optimizedForFrequentAttach
          value: boolean
        - name: LastOwnershipUpdateTime
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>disks</code> resource.

```sql
/*+ update */
UPDATE azure.compute.disks
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
diskName = '{{ diskName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>disks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.disks
WHERE diskName = '{{ diskName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
