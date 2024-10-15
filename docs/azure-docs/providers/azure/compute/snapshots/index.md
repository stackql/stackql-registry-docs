---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="completion_percent" /> | `text` | field from the `properties` object |
| <CopyableCode code="copy_completion_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_access_auth_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_access_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_settings_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="incremental" /> | `text` | field from the `properties` object |
| <CopyableCode code="incremental_snapshot_family_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_access_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_hibernation" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | Unused. Always Null. |
| <CopyableCode code="properties" /> | `object` | Snapshot resource properties. |
| <CopyableCode code="sku" /> | `object` | The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Gets information about a snapshot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists snapshots under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists snapshots under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Creates or updates a snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Deletes a snapshot. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Updates (patches) a snapshot. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId, data__access, data__durationInSeconds" /> | Grants access to a snapshot. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Revokes access to a snapshot. |

## `SELECT` examples

Lists snapshots under a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
completion_percent,
copy_completion_error,
creation_data,
data_access_auth_mode,
disk_access_id,
disk_size_bytes,
disk_size_gb,
disk_state,
encryption,
encryption_settings_collection,
extended_location,
hyper_v_generation,
incremental,
incremental_snapshot_family_id,
location,
managed_by,
network_access_policy,
os_type,
provisioning_state,
public_network_access,
purchase_plan,
resourceGroupName,
security_profile,
sku,
snapshotName,
subscriptionId,
supported_capabilities,
supports_hibernation,
tags,
time_created,
type,
unique_id
FROM azure.compute.vw_snapshots
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
properties,
sku,
tags,
type
FROM azure.compute.snapshots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshots</code> resource.

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
INSERT INTO azure.compute.snapshots (
resourceGroupName,
snapshotName,
subscriptionId,
sku,
extendedLocation,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ snapshotName }}',
'{{ subscriptionId }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
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
        - name: diskState
          value: []
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
        - name: incremental
          value: boolean
        - name: incrementalSnapshotFamilyId
          value: string
        - name: encryption
          value:
            - name: diskEncryptionSetId
              value: string
            - name: type
              value: []
        - name: networkAccessPolicy
          value: []
        - name: diskAccessId
          value: string
        - name: securityProfile
          value:
            - name: securityType
              value: []
            - name: secureVMDiskEncryptionSetId
              value: string
        - name: supportsHibernation
          value: boolean
        - name: publicNetworkAccess
          value: []
        - name: completionPercent
          value: number
        - name: copyCompletionError
          value:
            - name: errorCode
              value: string
            - name: errorMessage
              value: string
        - name: dataAccessAuthMode
          value: []
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

Updates a <code>snapshots</code> resource.

```sql
/*+ update */
UPDATE azure.compute.snapshots
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.snapshots
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
