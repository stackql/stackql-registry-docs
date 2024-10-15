---
title: restore_point_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_point_collections
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

Creates, updates, deletes, gets or lists a <code>restore_point_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_point_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.restore_point_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_point_collections', value: 'view', },
        { label: 'restore_point_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_collection_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_points" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The restore point collection properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId" /> | The operation to get the restore point collection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of restore point collections in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId" /> | The operation to create or update the restore point collection. Please refer to https://aka.ms/RestorePoints for more details. When updating a restore point collection, only tags may be modified. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId" /> | The operation to delete the restore point collection. This operation will also delete all the contained restore points. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, restorePointCollectionName, subscriptionId" /> | The operation to update the restore point collection. |

## `SELECT` examples

Gets the list of restore point collections in the subscription. Use nextLink property in the response to get the next page of restore point collections. Do this till nextLink is not null to fetch all the restore point collections.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_point_collections', value: 'view', },
        { label: 'restore_point_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
provisioning_state,
resourceGroupName,
restorePointCollectionName,
restore_point_collection_id,
restore_points,
source,
subscriptionId,
tags,
type
FROM azure.compute.vw_restore_point_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.restore_point_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restore_point_collections</code> resource.

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
INSERT INTO azure.compute.restore_point_collections (
resourceGroupName,
restorePointCollectionName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ restorePointCollectionName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: source
          value:
            - name: location
              value: string
            - name: id
              value: string
        - name: provisioningState
          value: string
        - name: restorePointCollectionId
          value: string
        - name: restorePoints
          value:
            - - name: properties
                value:
                  - name: excludeDisks
                    value:
                      - - name: id
                          value: string
                  - name: sourceMetadata
                    value:
                      - name: hardwareProfile
                        value:
                          - name: vmSize
                            value: string
                          - name: vmSizeProperties
                            value:
                              - name: vCPUsAvailable
                                value: integer
                              - name: vCPUsPerCore
                                value: integer
                      - name: storageProfile
                        value:
                          - name: osDisk
                            value:
                              - name: osType
                                value: string
                              - name: encryptionSettings
                                value:
                                  - name: diskEncryptionKey
                                    value:
                                      - name: secretUrl
                                        value: string
                                      - name: sourceVault
                                        value:
                                          - name: id
                                            value: string
                                  - name: keyEncryptionKey
                                    value:
                                      - name: keyUrl
                                        value: string
                                  - name: enabled
                                    value: boolean
                              - name: name
                                value: string
                              - name: caching
                                value: []
                              - name: diskSizeGB
                                value: integer
                              - name: managedDisk
                                value:
                                  - name: storageAccountType
                                    value: []
                                  - name: diskEncryptionSet
                                    value:
                                      - name: id
                                        value: string
                                  - name: securityProfile
                                    value:
                                      - name: securityEncryptionType
                                        value: string
                                  - name: id
                                    value: string
                              - name: diskRestorePoint
                                value:
                                  - name: encryption
                                    value:
                                      - name: type
                                        value: []
                                  - name: sourceDiskRestorePoint
                                    value:
                                      - name: id
                                        value: string
                                  - name: id
                                    value: string
                              - name: writeAcceleratorEnabled
                                value: boolean
                          - name: dataDisks
                            value:
                              - - name: lun
                                  value: integer
                                - name: name
                                  value: string
                                - name: diskSizeGB
                                  value: integer
                                - name: writeAcceleratorEnabled
                                  value: boolean
                          - name: diskControllerType
                            value: []
                      - name: osProfile
                        value:
                          - name: computerName
                            value: string
                          - name: adminUsername
                            value: string
                          - name: adminPassword
                            value: string
                          - name: customData
                            value: string
                          - name: windowsConfiguration
                            value:
                              - name: provisionVMAgent
                                value: boolean
                              - name: enableAutomaticUpdates
                                value: boolean
                              - name: timeZone
                                value: string
                              - name: additionalUnattendContent
                                value:
                                  - - name: passName
                                      value: string
                                    - name: componentName
                                      value: string
                                    - name: settingName
                                      value: string
                                    - name: content
                                      value: string
                              - name: patchSettings
                                value:
                                  - name: patchMode
                                    value: string
                                  - name: enableHotpatching
                                    value: boolean
                                  - name: assessmentMode
                                    value: string
                                  - name: automaticByPlatformSettings
                                    value:
                                      - name: rebootSetting
                                        value: string
                                      - name: bypassPlatformSafetyChecksOnUserSchedule
                                        value: boolean
                              - name: winRM
                                value:
                                  - name: listeners
                                    value:
                                      - - name: protocol
                                          value: string
                                        - name: certificateUrl
                                          value: string
                              - name: enableVMAgentPlatformUpdates
                                value: boolean
                          - name: linuxConfiguration
                            value:
                              - name: disablePasswordAuthentication
                                value: boolean
                              - name: ssh
                                value:
                                  - name: publicKeys
                                    value:
                                      - - name: path
                                          value: string
                                        - name: keyData
                                          value: string
                              - name: provisionVMAgent
                                value: boolean
                              - name: patchSettings
                                value:
                                  - name: patchMode
                                    value: string
                                  - name: assessmentMode
                                    value: string
                                  - name: automaticByPlatformSettings
                                    value:
                                      - name: rebootSetting
                                        value: string
                                      - name: bypassPlatformSafetyChecksOnUserSchedule
                                        value: boolean
                              - name: enableVMAgentPlatformUpdates
                                value: boolean
                          - name: secrets
                            value:
                              - - name: vaultCertificates
                                  value:
                                    - - name: certificateUrl
                                        value: string
                                      - name: certificateStore
                                        value: string
                          - name: allowExtensionOperations
                            value: boolean
                          - name: requireGuestProvisionSignal
                            value: boolean
                      - name: diagnosticsProfile
                        value:
                          - name: bootDiagnostics
                            value:
                              - name: enabled
                                value: boolean
                              - name: storageUri
                                value: string
                      - name: licenseType
                        value: string
                      - name: vmId
                        value: string
                      - name: securityProfile
                        value:
                          - name: uefiSettings
                            value:
                              - name: secureBootEnabled
                                value: boolean
                              - name: vTpmEnabled
                                value: boolean
                          - name: encryptionAtHost
                            value: boolean
                          - name: securityType
                            value: string
                          - name: encryptionIdentity
                            value:
                              - name: userAssignedIdentityResourceId
                                value: string
                          - name: proxyAgentSettings
                            value:
                              - name: enabled
                                value: boolean
                              - name: mode
                                value: string
                              - name: keyIncarnationId
                                value: integer
                      - name: location
                        value: string
                      - name: userData
                        value: string
                      - name: hyperVGeneration
                        value: []
                  - name: provisioningState
                    value: string
                  - name: consistencyMode
                    value: string
                  - name: timeCreated
                    value: string
                  - name: instanceView
                    value:
                      - name: diskRestorePoints
                        value:
                          - - name: id
                              value: string
                            - name: replicationStatus
                              value:
                                - name: status
                                  value:
                                    - name: code
                                      value: string
                                    - name: level
                                      value: string
                                    - name: displayStatus
                                      value: string
                                    - name: message
                                      value: string
                                    - name: time
                                      value: string
                                - name: completionPercent
                                  value: integer
                      - name: statuses
                        value:
                          - - name: code
                              value: string
                            - name: level
                              value: string
                            - name: displayStatus
                              value: string
                            - name: message
                              value: string
                            - name: time
                              value: string
              - name: id
                value: string
              - name: name
                value: string
              - name: type
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

Updates a <code>restore_point_collections</code> resource.

```sql
/*+ update */
UPDATE azure.compute.restore_point_collections
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>restore_point_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.restore_point_collections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
