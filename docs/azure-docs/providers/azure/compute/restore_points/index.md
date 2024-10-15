---
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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

Creates, updates, deletes, gets or lists a <code>restore_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.restore_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_points', value: 'view', },
        { label: 'restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="consistency_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclude_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorePointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_restore_point" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The restore point properties. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to get the restore point. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to create the restore point. Updating properties of an existing restore point is not allowed |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to delete the restore point. |

## `SELECT` examples

The operation to get the restore point.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restore_points', value: 'view', },
        { label: 'restore_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
consistency_mode,
exclude_disks,
instance_view,
provisioning_state,
resourceGroupName,
restorePointCollectionName,
restorePointName,
source_metadata,
source_restore_point,
subscriptionId,
time_created,
type
FROM azure.compute.vw_restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND restorePointName = '{{ restorePointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.compute.restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND restorePointName = '{{ restorePointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restore_points</code> resource.

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
INSERT INTO azure.compute.restore_points (
resourceGroupName,
restorePointCollectionName,
restorePointName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ restorePointCollectionName }}',
'{{ restorePointName }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>restore_points</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.restore_points
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND restorePointCollectionName = '{{ restorePointCollectionName }}'
AND restorePointName = '{{ restorePointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
